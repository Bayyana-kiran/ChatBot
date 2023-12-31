 ## Project: chatterbox - A Text Summarization App with Streamlit

### Overview:
chatterbox is a user-friendly text summarization application built using Streamlit and a fine-tuned language model. It allows users to input meeting notes or any text, and generates a concise summary of the provided text. This README file provides a detailed explanation of the code, making it easy for junior developers to understand and replicate the project.

### Prerequisites:
Before you begin, ensure you have the following installed:
- Python 3 or higher
- Streamlit
- dotenv

### Step 1: Setting Up the Environment
1. Clone the project repository or download the code.
2. Open a terminal or command prompt and navigate to the project directory.
3. Create a `.env` file in the project directory. This file will store your API key.
4. Add the following line to the `.env` file:
```
API_URL=https://api-inference.huggingface.co/models/knkarthick/MEETING_SUMMARY
```
5. Replace the placeholder value with your actual API key obtained from Hugging Face.

### Step 2: Understanding the Code
The code consists of a single Python script (`app.py`) that implements the text summarization functionality. Let's break down the code step by step:

```python
# Import necessary libraries
from dotenv import find_dotenv, load_dotenv
import requests
import streamlit as st
```
- We start by importing the required libraries. `dotenv` is used to load the API key from the `.env` file, `requests` is used to make API calls, and `streamlit` is used to create the user interface.

```python
# Set page background image
page_bg_img = """
<style>
body {
    background: linear-gradient(90deg, #ff6b6b, #ff8e8e);
    background-size: cover;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
```
- This code sets a gradient background image for the Streamlit app.

```python
# Load API key from .env file
load_dotenv(find_dotenv())
API_URL = os.getenv("API_URL")
HEADERS = {"Authorization": f"Bearer {os.getenv

