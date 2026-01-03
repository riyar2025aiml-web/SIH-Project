# Nabha Digital Learning Chatbot

An AI-powered **Digital Learning Platform Chatbot** built with **Streamlit** and **Google Gemini API**.  
This chatbot helps rural school students in **Nabha** learn interactively by asking questions in **Math, Science, English, and more**.

---

## 🚀 Features
- 🤖 Chatbot powered by **Gemini 2.5 Flash** (free API key from Google AI Studio)  
- 📝 Student-friendly conversational interface  
- 📚 Supports general education topics (Math, Science, English, GK, etc.)  
- 💬 Maintains chat history in session  
- 🌍 Can be extended to support **Punjabi/Hindi** for rural learners  

---

## 🛠️ Tech Stack
- [Python](https://www.python.org/)  
- [Streamlit](https://streamlit.io/) – UI framework  
- [Google Generative AI SDK](https://ai.google.dev/) – Gemini API  

---

## 📦 Installation

1. **Clone this repo**
   ```bash
   git clone https://github.com/KIRIT-P-S/Nabha-Student-Chatbot-SIH.git
   cd nabha-digital-learning-chatbot
Create a virtual environment (optional but recommended)

bash
Copy code
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
Install dependencies

bash
Copy code
pip install -r requirements.txt
🔑 Setup API Key
Get your free Gemini API key from Google AI Studio.

Add it in your code (app.py) like this:

python
Copy code
GEMINI_API_KEY = "YOUR_API_KEY"
⚠️ Important: For security, avoid hardcoding your key in public repos.
Instead, use environment variables or Streamlit secrets.

▶️ Run the App
bash
Copy code
streamlit run app.py
Then open your browser at: http://localhost:8501

📁 Project Structure
bash
Copy code
nabha-digital-learning-chatbot/
│
├── app.py               # Main Streamlit chatbot code
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── venv/                # (Optional) Virtual environment
🌟 Future Enhancements
🌍 Support for Punjabi/Hindi responses

📱 Mobile-friendly deployment

🏫 Integration with digital classrooms for rural schools

📊 Student performance tracking

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

## ✍️ Author
- **Created by:** KIRIT P S  
- **Year:** 2025  

## 📜 License
This project is licensed under the **MIT License**.  

You are free to use, modify, and distribute this project, but attribution to the original author is required.  

