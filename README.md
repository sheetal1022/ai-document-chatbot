<img width="1249" height="810" alt="Screenshot 2026-03-13 at 11 49 48 PM" src="https://github.com/user-attachments/assets/56d54137-0131-4a87-b2cb-a2b37461ae85" />

<img width="1237" height="791" alt="Screenshot 2026-03-13 at 11 54 20 PM" src="https://github.com/user-attachments/assets/a0ef45d6-ecee-426f-bacb-cbfad0d4bbb6" />

--------------------------------------------------
ai-document-chatbot
│
├── backend
│   ├── app.py
│   ├── requirements.txt
│   ├── docs
│   └── db
│
└── frontend
-----------------------------------------------------

1. Python

Install Python 3.10+
Check:
python --version

2. Create Project Folder
ai-document-chatbot

Inside:
backend
frontend

3. Backend Setup
Go inside backend:
cd backend

4. Create virtual environment:
python -m venv venv

Activate it

Mac/Linux:
source venv/bin/activate

Windows:
venv\Scripts\activate

5. Install Required Libraries
Run:
pip install langchain
pip install chromadb
pip install fastapi
pip install uvicorn
pip install pypdf
pip install google-generativeai
pip install langchain-community
pip install langchain-google-genai

6. Get Gemini API Key
Go to:
Google AI Studio
Create API key for Google Gemini
Save it.

7.  Create Backend File
Create:
app.py

8. Run Backend
Run:
uvicorn app:app --reload

Open:
http://127.0.0.1:8000/docs

You will see Swagger UI.
You can test:
upload PDF
ask question
