# **Basic LLM Chat App**
# 
# This is a chat application built with Streamlit and OpenAI.
# It lets you interact with a large language model (LLM) in a simple web interface.


# **Installation**

# Clone the repository:
git clone https://github.com/Mandisalovet/llm_chat_app.git
cd llm_chat_app

# Create and activate a Conda environment:
conda create -n astro_env python=3.9 -y
conda activate astro_env

# Install dependencies:
pip install streamlit openai

# Add your OpenAI API key:
# Create a secrets file at .streamlit/secrets.toml and paste the following:
echo 'OPENAI_API_KEY = "your-api-key-here"' > .streamlit/secrets.toml

# Run the app locally:
streamlit run app.py

# Deploy on Streamlit Cloud
