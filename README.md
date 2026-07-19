# 🎙️ Audio Translator using Groq Whisper & Flask
## 📸 Screenshots

<p align="center">
  <img src="https://github.com/user-attachments/assets/aafec7a2-cd01-4a5f-a3b7-2e9dd80089ab" width="300"/>
  <img src="https://github.com/user-attachments/assets/51f19626-0097-4930-a117-1bca0168ebaf" width="300"/>
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/1ccb2a80-4b8e-49f3-8d23-02a1c16a5b4a" width="300"/>
  <img src="https://github.com/user-attachments/assets/71a6d46b-3a8a-43a0-bda7-946e233a2c21" width="300"/>
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/2bead338-616c-431c-a03c-b39bc2e93cfc" width="300"/>
  <img src="https://github.com/user-attachments/assets/9a0e6246-b7c1-41e4-95d6-ea28e9ea6b88" width="300"/>
</p>

A simple and fast web application that converts speech from audio files into text using **Groq's Whisper Large V3 Turbo** model. The application is built with **Python, Flask, Bootstrap 5**, and the **Groq API**.

---

## 🚀 Features

- 🎤 Upload audio files (`.mp3`, `.wav`, `.m4a`)
- 🌍 Supports multiple languages
- 📝 Speech-to-Text transcription
- ⚡ Fast transcription using Groq Whisper API
- 💻 Clean and responsive Bootstrap 5 interface
- 🔒 Secure API key management using `.env`

---

## 🛠️ Tech Stack

- Python
- Flask
- Groq API
- Whisper Large V3 Turbo
- Bootstrap 5
- HTML5
- CSS3

---

## 📂 Project Structure

```text
Audio-Translator/
│
├── app.py
├── demo.py
├── requirements.txt
├── .env
├── .gitignore
│
├── static/
│
└── templates/
    └── index.html
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/LOHITHVATTAM1628/audio-translator-groq.git
```

### 2. Navigate to the Project

```bash
cd audio-translator-groq
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Environment (Windows - Git Bash)

```bash
source venv/Scripts/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
```

### 6. Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 🎯 How to Use

1. Open the web application.
2. Upload an audio file.
3. Select the language.
4. Click **Transcribe**.
5. View the transcribed text instantly.

---

## 📌 Supported Audio Formats

- MP3
- WAV
- M4A
- FLAC
- OGG
- WEBM

---

## 🤖 AI Model

This project uses:

```
whisper-large-v3-turbo
```

The model provides multilingual speech recognition with low latency and high transcription accuracy.

---

## 📚 Resources

### Groq Speech-to-Text Documentation

https://console.groq.com/docs/speech-to-text

### Groq API Reference

https://console.groq.com/docs/api-reference

### Bootstrap 5 Documentation

https://getbootstrap.com/docs/5.3/getting-started/introduction/

---

## 📦 Requirements

```
Flask
groq
python-dotenv
```

Install using:

```bash
pip install -r requirements.txt
```

---

## 📸 Screenshots

Add screenshots of your application here.

---

## 👨‍💻 Author

**Lohith Vattam**

- GitHub: https://github.com/LOHITHVATTAM1628

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
