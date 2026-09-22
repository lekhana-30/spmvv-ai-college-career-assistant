# 🎓 SPMVV AI College & Career Guidance Assistant

An AI-powered college information and career guidance chatbot developed specifically for **Sri Padmavati Mahila Visvavidyalayam (SPMVV)** students.

The chatbot provides general information about SPMVV and detailed guidance related to the **B.Tech department**, especially for Computer Science and Engineering students.

It helps students get information about college facilities, B.Tech programs, programming, DSA, DBMS, GitHub, projects, internships, placements, and career preparation.

---

## 📌 Project Overview

The **SPMVV AI College & Career Guidance Assistant** is a domain-specific chatbot developed using Python and Natural Language Processing techniques.

Unlike a general-purpose chatbot, this system is designed specifically around the information and guidance needs of SPMVV students.

The system uses a structured FAQ knowledge base and Natural Language Processing techniques to identify the question asked by the user and provide the most relevant predefined answer.

The application provides an interactive web interface using **Streamlit**.

---

## 🎯 Objectives

The main objectives of this project are:

- Provide students with quick access to SPMVV-related information.
- Provide detailed information and guidance for B.Tech students.
- Help CSE students understand important technical skills.
- Provide guidance about Python, DSA, DBMS, Git and GitHub.
- Guide students in building academic and resume-worthy projects.
- Provide internship preparation guidance.
- Provide placement preparation guidance.
- Help students understand different career paths in technology.
- Provide an easy-to-use chatbot interface.
- Reduce the time required to search for commonly needed information.

---

## ✨ Features

### 🏫 SPMVV Information

The chatbot can answer questions related to:

- SPMVV
- University location
- University information
- B.Tech availability
- Hostel facilities
- Library
- University facilities
- Contact information
- Official website

### 💻 B.Tech Guidance

The chatbot provides detailed guidance about:

- B.Tech and CSE
- Programming languages
- Python
- DSA
- DBMS
- Git
- GitHub
- Coding practice
- Projects
- Internships
- Placements
- Resume development
- Certifications
- Career preparation

### 🚀 Career Guidance

The system provides guidance for career paths such as:

- Software Engineer
- AI Engineer
- Data Scientist
- Web Development
- General CSE career preparation

### 💬 Chat Features

The application provides:

- Interactive chat interface
- User and assistant messages
- Chat history during the session
- Clear Chat option
- Download Chat option
- SPMVV logo integration
- Responsive Streamlit interface

---

## 🧠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| NLTK | Natural Language Processing |
| Scikit-Learn | TF-IDF and similarity calculation |
| Streamlit | Web application interface |
| NumPy | Numerical operations |
| Pandas | Data handling |
| JSON | FAQ knowledge storage |
| Git | Version control |
| GitHub | Source code repository |

---

## 🔍 Natural Language Processing

The chatbot uses Natural Language Processing to process user questions.

The preprocessing pipeline includes:

1. Converting text to lowercase.
2. Tokenizing the input.
3. Removing punctuation.
4. Applying WordNet Lemmatization.
5. Converting the processed text into a format suitable for comparison.

Example:

```text
User Input:
How can I get internships?

        ↓

Text Preprocessing

        ↓

Tokenization

        ↓

Lemmatization

        ↓

TF-IDF Vectorization

        ↓

Cosine Similarity

        ↓

Best Matching FAQ

        ↓

Chatbot Response
```
🔎 TF-IDF and Cosine Similarity

The chatbot uses TF-IDF (Term Frequency-Inverse Document Frequency) to convert questions into numerical vectors.

The system then uses Cosine Similarity to compare the user's question with questions stored in the FAQ knowledge base.

The question with the strongest relevant similarity is selected and its corresponding answer is returned.

This allows the chatbot to handle questions that are worded differently but have similar meanings.

📚 Knowledge Base

The chatbot uses JSON files as its knowledge base.

data/
│
├── spmvv_general.json
└── btech_faqs.json
spmvv_general.json

Contains general information related to SPMVV.

btech_faqs.json

Contains detailed information and career guidance related to B.Tech students.

The FAQ structure allows multiple question variations to be associated with the same answer.

Example:

{
    "questions": [
        "How can I get internships?",
        "How do I get an internship?",
        "Where can I find internships?"
    ],
    "answer": "Build projects, maintain a GitHub profile, learn DSA and apply through LinkedIn, Internshala and company career pages."
}
📂 Project Structure
chatbot_project/
│
├── assets/
│   └── logo.png
│
├── data/
│   ├── btech_faqs.json
│   └── spmvv_general.json
│
├── utils/
│   ├── __init__.py
│   └── preprocessing.py
│
├── app.py
├── chatbot.py
├── intents.json
├── preprocessing.py
├── requirements.txt
├── test_chatbot.py
├── test_nltk.py
├── .gitignore
│
└── chat_history.json

chat_history.json is used locally to store the conversation history and should normally be excluded from GitHub using .gitignore.

⚙️ Requirements

Before running the project, make sure you have:

Python 3.12 or compatible Python version
pip
Git
Internet connection for installing dependencies
📥 Installation
1. Clone the repository
git clone https://github.com/lekhana-30/spmvv-ai-college-career-assistant.git
2. Open the project directory
cd spmvv-ai-college-career-assistant
3. Install required libraries
pip install -r requirements.txt
4. Download NLTK resources

Open Python and run:

import nltk

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("wordnet")
nltk.download("omw-1.4")
▶️ Running the Application

Run the Streamlit application using:

streamlit run app.py

After starting the application, Streamlit will provide a local URL similar to:

http://localhost:8501

Open this URL in your web browser.

💬 Example Questions

You can ask questions such as:

Where is SPMVV located?
Does SPMVV offer B.Tech?
What is CSE?
What programming language should I learn first?
What is DSA?
Why should I learn DBMS?
How can I learn GitHub?
How can I get internships?
How can I prepare for placements?
How can I become an AI Engineer?
What projects should I build?
🖥️ User Interface

The application contains:

Sidebar

The sidebar provides:

SPMVV logo
Project title
Supported topics
Clear Chat button
Download Chat button
Main Interface

The main interface contains:

SPMVV logo
Chatbot title
Description
Conversation area
User input box
🧪 Testing

The chatbot can be tested using different categories of questions.

General Information Testing

Example:

Where is SPMVV located?

Expected response:

SPMVV is located in Tirupati, Andhra Pradesh.
B.Tech Testing

Example:

What is CSE?

The chatbot provides the corresponding CSE information.

Career Testing

Example:

How can I get internships?

The chatbot provides internship preparation guidance.

Unknown Query Testing

If the chatbot cannot find relevant information, it provides a fallback response asking the user to ask questions related to SPMVV or B.Tech.

🔐 Data and Privacy

The chatbot does not require users to create an account.

The application uses locally stored JSON files for its FAQ knowledge base.

Conversation history is stored locally in:

chat_history.json

Sensitive or private information should not be entered into the chatbot.

🚀 Future Enhancements

The project can be extended with:

Voice input
Voice output
More SPMVV information
More B.Tech FAQs
Improved semantic search
Retrieval-Augmented Generation (RAG)
College website integration
Database integration
Student authentication
Personalized student guidance
Course recommendations
Internship recommendation system
Placement preparation module
Resume analysis
AI-based career recommendations
Mobile-friendly interface
🎓 Academic Value

This project demonstrates practical implementation of:

Python programming
Natural Language Processing
Machine Learning techniques
Text preprocessing
TF-IDF vectorization
Cosine similarity
JSON data management
Streamlit web development
Git and GitHub
Software testing
User interface development

It also demonstrates how an AI-based system can be designed for a specific educational domain.

👩‍💻 Author

Lekhana

B.Tech – Computer Science and Engineering

Sri Padmavati Mahila Visvavidyalayam (SPMVV)

GitHub:

https://github.com/lekhana-30

📜 License

This project is developed as an academic/educational project.

You may modify and extend the project for learning and educational purposes.
