# Mandisa's Basic LLM Chat App

A simple conversational AI application built with Python, Streamlit and the OpenAI API.

The application allows users to interact with an AI language model through a chat interface. It maintains conversation history using Streamlit session state and displays responses as they are generated.

**[Open the Live Application](https://llmchatapp-mandilovet.streamlit.app/)**

*Note: The application is deployed, but AI responses are temporarily unavailable while API credits are exhausted.*

## Features

- Interactive chat interface built with Streamlit.
- Integration with the OpenAI API.
- Conversational history maintained using session state.
- Streaming AI-generated responses.
- Secure API key configuration using Streamlit Secrets.

## Technologies Used

- Python
- Streamlit
- OpenAI API

## Project Structure

```text
llm_chat_app/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Mandisalovet/llm_chat_app.git
cd llm_chat_app
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure your API key

Create a `.streamlit/secrets.toml` file and add your OpenAI API key:

```toml
OPENAI_API_KEY = "your-api-key"
```

Never commit your API key to GitHub.

### 4. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## Deployment

The application is deployed using Streamlit Community Cloud and connected to this GitHub repository.

- **Repository:** https://github.com/Mandisalovet/llm_chat_app
- **Live application:** https://llmchatapp-mandilovet.streamlit.app/

## What I Learned

Through this project, I explored how to:

- Build an interactive application using Streamlit.
- Integrate an external AI service through an API.
- Manage conversation history using session state.
- Handle API credentials through environment-specific secrets.
- Deploy a Python application using GitHub and Streamlit Community Cloud.

## Author

**Mandisa Love Tshabalala**

[GitHub](https://github.com/Mandisalovet)
