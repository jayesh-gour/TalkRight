# 💬 TalkRight

An AI-powered chatbot that helps you practice conversational English. Type naturally — mistakes and all — and TalkRight will gently correct your grammar/phrasing while replying like a supportive friend, not a strict teacher.

Built as a personal project to make English practice feel low-pressure and encouraging, rather than clinical or judgmental.

---

## ✨ What It Does

- Takes user input in natural, casual English (typos and grammar mistakes included)
- Corrects grammar/phrasing in a warm, encouraging tone — never robotic or harsh
- Replies conversationally, like chatting with a close friend
- Designed for non-native English speakers who want to practice without fear of judgment

**Example:**
```
You: i hungy
TalkRight:
Correction: Almost! It's "I am hungry" — you got this!
Reply: Same here honestly! What are you thinking of eating?
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | FastAPI (Python) |
| AI Model | Google Gemini API (`gemini-flash-latest`) |
| Frontend | Streamlit |
| Config Management | python-dotenv |
| Data Validation | Pydantic |

---

## 📐 Architecture

```
User (Streamlit UI)
      │
      ▼
FastAPI Backend (/chat endpoint)
      │
      ▼
Prompt Engineering Layer (system prompt)
      │
      ▼
Google Gemini API
      │
      ▼
Response (Correction + Friendly Reply)
      │
      ▼
Back to Streamlit UI
```

---

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/jayesh-gour/TalkRight.git
cd TalkRight
```

### 2. Set up the backend
```bash
cd backend
python -m venv venv

# Activate the virtual environment
venv\Scripts\activate       # Windows
source venv/bin/activate    # Mac/Linux

pip install -r requirements.txt
```

### 3. Add your Gemini API key
Create a `.env` file inside the `backend/` folder:
```
GEMINI_API_KEY=your_key_here
```
> Get a free API key at [Google AI Studio](https://aistudio.google.com/apikey)

### 4. Run the backend server
```bash
uvicorn main:app --reload
```
Backend will be live at `http://127.0.0.1:8000`
API docs available at `http://127.0.0.1:8000/docs`

### 5. Run the frontend (in a new terminal)
```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

---

## 📂 Project Structure

```
TalkRight/
│
├── backend/
│   ├── main.py            # FastAPI app and /chat endpoint
│   ├── gemini_client.py   # Gemini API integration + error handling
│   ├── prompts.py         # System prompt (correction + reply logic)
│   ├── requirements.txt
│   └── .env                # API key (not committed to Git)
│
├── frontend/
│   ├── app.py              # Streamlit chat interface
│   └── requirements.txt
│
├── .gitignore
└── README.md
```

---

## 🧠 What I Learned

- Building and structuring a full-stack AI application from scratch
- **Prompt engineering** — designing prompts that consistently produce a specific tone and output format
- Error handling at the right architectural layer (catching errors at the API-call level instead of duplicating handling everywhere)
- Maintaining a **consistent response schema** between backend and frontend so the UI never breaks unexpectedly
- Connecting a Python backend (FastAPI) with a Python frontend (Streamlit) via REST calls
- Adapting to real-world API changes — Gemini deprecated multiple model versions during development, which required debugging and switching to a stable model alias (`gemini-flash-latest`)

---

## 🔮 Future Improvements

- [ ] Add side-by-side comparison with OpenAI and DeepSeek APIs
- [ ] Add multi-turn conversation memory (context across messages)
- [ ] Deploy live on Render.com (backend) + Streamlit Cloud (frontend)
- [ ] Add a "difficulty level" setting (beginner / intermediate / advanced corrections)
- [ ] Voice input/output support

---

## 👤 Author

**Jayesh Gour**
[GitHub](https://github.com/jayesh-gour) · [LinkedIn](https://www.linkedin.com/in/jayesh-gour)

---

*Built as part of a self-directed Applied AI/ML Engineering learning roadmap.*
