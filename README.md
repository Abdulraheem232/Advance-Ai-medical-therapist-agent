

---

# 🧠 Advance AI Medical Therapist Agent

An **AI-powered therapeutic chatbot** that provides **empathetic mental health support**, helps users **find nearby therapists**, and can **trigger an emergency safety call** if someone expresses suicidal thoughts or self-harm intentions.

This project is built using **LangChain**, **LangGraph**, and **Groq LLMs**, with **Twilio integration** for emergency calls.

---

## 🚀 Features

* 🤝 **Therapeutic Conversations**
  Responds to emotional or psychological queries with warmth and evidence-based guidance.

* 🧑‍⚕️ **Find Nearby Therapists**
  Suggests licensed therapists and counseling centers near a user’s location.

* 🚨 **Emergency Response**
  If a user expresses suicidal intent or a mental health crisis, the chatbot **triggers an emergency call (via Twilio)** and responds compassionately.

* 🔗 **Agentic AI Design**
  Uses LangGraph’s ReAct agent to dynamically decide when to:

  * Chat with the user
  * Look up therapists
  * Call emergency services

---

## 🛠️ Tech Stack

* [LangChain](https://www.langchain.com/) – Orchestrates tools and reasoning
* [LangGraph](https://github.com/langchain-ai/langgraph) – Agent execution framework
* [Groq LLM](https://console.groq.com/) – Fast inference with `openai/gpt-oss-120b`
* [Twilio](https://www.twilio.com/) – Emergency call integration
* Python 3.10+

---

## ⚙️ Setup

### 1. Clone Repository

```bash
git clone https://github.com/Abdulraheem232/Advance-Ai-medical-therapist-agent.git
cd Advance-Ai-medical-therapist-agent
```

### 2. Install Dependencies

Install required Python packages manually:

```bash
pip install langchain langgraph langchain_groq twilio python-dotenv
```

*(You can later create a `requirements.txt` by running `pip freeze > requirements.txt` for easier installs.)*

### 3. Get API Keys

* **Groq API Key** → Get it from the [Groq Console](https://console.groq.com/).
* **Twilio Credentials** → Get your `ACCOUNT_SID` and `AUTH_TOKEN` from the [Twilio Console](https://www.twilio.com/console).

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
EMERGENCY_PHONE_NUMBER=+923219160283
```

### 5. Run the Agent

```bash
python ai_agent.py
```

---

## 🧩 Example Usage

```python
from ai_agent import ask_question

print(ask_question("I feel really anxious and can't calm down."))
# -> Empathetic therapeutic guidance

print(ask_question("Find me therapists near Lahore."))
# -> Therapist list for Lahore

print(ask_question("I am going to harm myself, please help me!"))
# -> Emergency call triggered + supportive response
```

---

## 🔒 Safety Notice

⚠️ **This project is for educational and prototyping purposes only.**
It should **not replace professional mental health care.**
If you or someone you know is in crisis, please **call your local emergency number immediately.**

---

## 🤝 Contributing

Contributions are welcome!

* Open an issue for suggestions or bug reports
* Submit a pull request with improvements

---

## 📜 License

MIT License © 2025 [Abdulraheem232](https://github.com/Abdulraheem232)

---

👉 Do you want me to also add a **section on deploying this chatbot as an API (FastAPI/Flask)** so people can interact with it over HTTP instead of just running `python ai_agent.py`?
