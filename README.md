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
