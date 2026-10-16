
import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="Mandisa's LLM Chat App",
    page_icon="💬",
    layout="centered"
)

st.title("Mandisa's Basic LLM Chat App")
st.caption("A simple conversational AI application built with Streamlit and OpenAI.")

# Check that the API key is configured
if "OPENAI_API_KEY" not in st.secrets:
    st.error("OpenAI API key is not configured. Please add it in Streamlit Secrets.")
    st.stop()

# Initialise the OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Initialise conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Accept a new user prompt
if prompt := st.chat_input("Ask me anything"):

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            stream = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=st.session_state.messages,
                stream=True
            )

            response = st.write_stream(stream)

            st.session_state.messages.append(
                {"role": "assistant", "content": response}
            )

        except Exception as e:
            st.error(f"Something went wrong: {e}")
