import os
import subprocess
import sys
import logging
from fuzzywuzzy import process
from livekit.agents import function_tool
import asyncio
try:
    import pygetwindow as gw
except ImportError:
    gw = None

if sys.version_info >= (3, 7) and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding='utf-8')  # type: ignore

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def focus_window(title_keyword: str) -> bool:
    if not gw:
        logger.warning("⚠ pygetwindow module missing.")
        return False

    await asyncio.sleep(1.5)
    title_keyword = title_keyword.lower().strip()

    for window in gw.getAllWindows():
        if title_keyword in window.title.lower():
            try:
                if window.isMinimized:
                    window.restore()
                window.activate()
                logger.info(f"Window focused: {window.title}")
                return True
            except Exception as e:
                logger.error(f"Error focusing window: {e}")
                return False
    logger.warning("⚠ No window found to focus.")
    return False

async def index_files(base_dirs: list[str]) -> list[dict]:
    file_index = []
    for base_dir in base_dirs:
        for root, dirs, files in os.walk(base_dir):
            for f in files:
                file_index.append({
                    "name": f,
                    "path": os.path.join(root, f),
                    "type": "file"
                })
    logger.info(f"Indexed {len(file_index)} files from {base_dirs}.")
    return file_index

async def search_file(query: str, index: list[dict]) -> dict | None:
    choices = [item["name"] for item in index]
    if not choices:
        logger.warning("⚠ No files to match.")
        return None

    best_match, score = process.extractOne(query, choices)  # type: ignore
    logger.info(f"Matched '{query}' to '{best_match}' with score {score}")
    if score > 70:
        for item in index:
            if item["name"] == best_match:
                return item
    return None

async def open_file(item: dict) -> str:
    try:
        logger.info(f"Opening file: {item['path']}")
        if os.name == 'nt':  # Windows
            os.startfile(item["path"])
        else:  # Mac or Linux
            opener = 'open' if sys.platform == 'darwin' else 'xdg-open'
            subprocess.call([opener, item["path"]])
        await focus_window(item["name"])
        return f"File opened: {item['name']}"
    except Exception as e:
        logger.error(f"Error opening file: {e}")
        return f"Failed to open file: {e}"

async def handle_command(command: str, index: list[dict]) -> str:
    item = await search_file(command, index)
    if item:
        return await open_file(item)
    else:
        logger.warning("File not found.")
        return "File not found."

@function_tool
async def Play_file(name: str) -> str:
    folders_to_index = ["D:/"]  
    index = await index_files(folders_to_index)
    command = name.strip()
    return await handle_command(command, index)

