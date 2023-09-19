from dotenv import find_dotenv, load_dotenv
import requests
import streamlit as st

page_bg_img = """
<style>
body {
    background: linear-gradient(90deg, #ff6b6b, #ff8e8e);
    background-size: cover;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
load_dotenv(find_dotenv())

API_URL = "https://api-inference.huggingface.co/models/knkarthick/MEETING_SUMMARY"
HEADERS = {"Authorization": f"Bearer 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"}

st.title("Welcome to chatterbox,🤖")

user_input = st.text_area("Enter meeting notes or text:")

if st.button("Generate Summary"):
    if user_input:
        try:
            response = requests.post(API_URL, headers=HEADERS, json={"inputs": user_input})
            
            if response.status_code == 200:
                result = response.json()
                
                if result and isinstance(result, list) and len(result) > 0:
                    summary = result[0].get("summary_text", "No summary available.")
                    st.subheader("Generated Summary:")
                    st.write(summary)
                else:
                    st.warning("No summary available.")
            else:
                st.error(f"Error: {response.status_code} - {response.text}")
        
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter some text for summarization.")


# Display model information and usage instructions
#st.markdown("### Model Information:")
st.write("⭐ artificial intelligence application designed to distill lengthy texts or conversations into shorter, coherent summaries, facilitating quick comprehension and efficient information retrieval for users across various domains ⭐")



# Optionally, you can add a footer with your information
