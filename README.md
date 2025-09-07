# 🗣️ Text-to-Speech  

A simple Python application that converts written text into natural-sounding speech using the **pyttsx3** library.  
Built with a lightweight **Tkinter GUI**, it’s ideal for accessibility, language learning, or just having your computer talk back to you.  

---

## Features
- Convert any text to speech instantly  
- User-friendly Tkinter interface  
- Error handling with popup messages (e.g., when no text is entered)  
- Works offline on Windows, macOS, and Linux  

---

## Getting Started  

### 1. Clone the repository  
```bash
git clone <repo-url>
```
```bash
cd Text-to-Speech
```
## 2. Create and activate a virtual environment
```bash
python -m venv venv
```
- On Windows
```bash
venv\Scripts\activate
```
- On macOS/Linux
```bash
source venv/bin/activate  # to activate venv
```
## 3. Install dependencies
```bash
pip install -r requirements.txt
```
## 4. Run the app
```bash
python text_to_speech.py
```
## Usage 
- Type your text in the input field
- Click Speak
- The app will read the text aloud 🎙️
- If you click Speak with an empty field, a popup error will appear

## Tech Stack
- Python 3
- kinter (GUI)
- pyttsx3 (text-to-speech engine)
