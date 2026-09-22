import streamlit as st
import json
import os

from chatbot import ChatBot


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="SPMVV AI Assistant",
    page_icon="assets/logo.png",
    layout="wide"
)


# --------------------------------------------------
# INITIALIZE CHATBOT
# --------------------------------------------------

bot = ChatBot()


# --------------------------------------------------
# LOGO PATH
# --------------------------------------------------

logo_path = "assets/logo.png"


# --------------------------------------------------
# SAVE CHAT HISTORY
# --------------------------------------------------

def save_chat_history():

    with open(
        "chat_history.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            st.session_state.messages,
            file,
            indent=4
        )


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    # Sidebar logo
    if os.path.exists(logo_path):

        col1, col2, col3 = st.columns(
            [1, 2, 1]
        )

        with col2:

            st.image(
                logo_path,
                width=120
            )

    # Sidebar title
    st.title(
        "🎓 SPMVV AI Assistant"
    )

    st.markdown("---")

    st.write(
        "Ask questions about:"
    )

    st.write("✅ SPMVV")
    st.write("✅ B.Tech")
    st.write("✅ CSE")
    st.write("✅ Placements")
    st.write("✅ Internships")

    st.markdown("---")

    # --------------------------------------------------
    # CLEAR CHAT
    # --------------------------------------------------

    if st.button(
        "🗑 Clear Chat"
    ):

        st.session_state.messages = []

        st.rerun()

    # --------------------------------------------------
    # DOWNLOAD CHAT
    # --------------------------------------------------

    chat_text = ""

    if "messages" in st.session_state:

        for msg in st.session_state.messages:

            chat_text += (
                f"{msg['role']}: "
                f"{msg['content']}\n"
            )

    st.download_button(
        label="📥 Download Chat",
        data=chat_text,
        file_name="chat_history.txt",
        mime="text/plain"
    )


# --------------------------------------------------
# INITIALIZE CHAT HISTORY
# --------------------------------------------------

if "messages" not in st.session_state:

    st.session_state.messages = []


# --------------------------------------------------
# MAIN PAGE HEADER
# --------------------------------------------------

col1, col2, col3 = st.columns(
    [1, 3, 1]
)

with col2:

    # ----------------------------------------------
    # CENTER LOGO
    # ----------------------------------------------

    logo_col1, logo_col2, logo_col3 = st.columns(
        [1, 1, 1]
    )

    with logo_col2:

        st.image(
            logo_path,
            width=150
        )

    # ----------------------------------------------
    # CENTER TITLE
    # ----------------------------------------------

    st.markdown(
        """
        <h1 style="
            text-align: center;
            margin-top: 5px;
            margin-bottom: 5px;
        ">
            🎓 SPMVV AI Assistant
        </h1>
        """,
        unsafe_allow_html=True
    )

    # ----------------------------------------------
    # CENTER SUBTITLE
    # ----------------------------------------------

    st.markdown(
        """
        <p style="
            text-align: center;
            margin-top: 10px;
            margin-bottom: 30px;
        ">
            College Information & B.Tech Guidance Chatbot
        </p>
        """,
        unsafe_allow_html=True
    )


# --------------------------------------------------
# DISPLAY PREVIOUS MESSAGES
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.write(
            message["content"]
        )


# --------------------------------------------------
# CHAT INPUT
# --------------------------------------------------

user_input = st.chat_input(
    "Ask about SPMVV or B.Tech..."
)


# --------------------------------------------------
# PROCESS USER QUESTION
# --------------------------------------------------

if user_input:

    # Add user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Get chatbot response
    response = bot.get_response(
        user_input
    )

    # Add chatbot response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    # Save conversation
    save_chat_history()

    # Refresh application
    st.rerun()