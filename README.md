# 🎙️ AI Voice Assistant - VS Code

Ye repository ek **Voice Assistant** ke liye hai jo **VS Code** me bana hai aur **Gemini API** aur **LiveKit** ka use karta hai.  
Assistant user ke questions ka jawab deta hai aur voice output ke saath interact karta hai.

---

## 🚀 Features

- 🗣️ Voice-based interaction with AI  
- 🤖 Answers user questions in real-time  
- 🔊 Text-to-Speech output using LiveKit  
- 🌐 Powered by Gemini API for intelligent responses  
- ⚡ Fully runnable in VS Code  

---

## 🗂 Project Details

- **Main Script:** `Main.py`  
- **Platform:** VS Code / Python  
- **Core Functionality:** Voice assistant capable of answering questions and speaking responses  

---

## 🏁 Getting Started :


1) Create a .env file in the same folder and put your keys there in the format:

OPENAI_API_KEY=
GOOGLE_API_KEY=
GOOGLE_SEARCH_API_KEY=
SEARCH_ENGINE_ID=
OPENWEATHER_API_KEY=
GROQ_API_KEY=
DEEPGRAM_API_KEY=
LIVEKIT_API_KEY=
LIVEKIT_API_SECRET=

(You can get these api keys for free on their respective websites.)


 
2) Create a virtual environment (optional but recommended):

Run these commands on Terminal : 

python -m venv venv
venv\Scripts\activate     # Windows



3) Run this command to Install required packages:


pip install -r requirements.txt


4) To run the project type in the terminal :

python agent.py console



