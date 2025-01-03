import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv
from PyPDF2 import PdfReader

# Load environment variables
load_dotenv()

# Initialize Groq API client
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),  # Ensure this is defined in your .env file
)

# Function to summarize text using Groq API
def summarize_text_groq(input_text, model="llama-3.3-70b-versatile", max_tokens=150):
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant.",
                },
                {
                    "role": "user",
                    "content": f"Summarize the following text:\n\n{input_text}",
                },
            ],
            model=model,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        raise RuntimeError(f"API call failed: {e}")

# Function to extract text from a PDF file
def extract_text_from_pdf(uploaded_pdf):
    try:
        pdf_reader = PdfReader(uploaded_pdf)
        if pdf_reader.is_encrypted:
            st.error("❌ The uploaded PDF is encrypted and cannot be processed.")
            return ""
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() or ""  # Handle pages with no text gracefully
        if not text.strip():
            raise RuntimeError("No extractable text found in the PDF.")
        return text
    except Exception as e:
        raise RuntimeError(f"Failed to extract text from PDF: {e}")

# Streamlit App Setup
st.set_page_config(page_title="Text Summarization App", page_icon="📚", layout="wide")
st.title("📚 Text Summarization App")

# Custom CSS styling
st.markdown("""
    <style>
    .main {
        background-color: #f4f7fc;
        padding: 20px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 15px 32px;
        font-size: 16px;
        cursor: pointer;
        border-radius: 5px;
        margin-top: 20px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stTextInput>div>div>input {
        font-size: 16px;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #ccc;
    }
    </style>
    """, unsafe_allow_html=True)

# Instructions or greeting
st.markdown("""
    <div style="font-size: 18px; color: #444;">
    Upload a PDF to extract and summarize its content.
    </div>
    """, unsafe_allow_html=True)

# PDF Upload Tab
st.subheader("📤 Upload a PDF for Summarization")
uploaded_pdf = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_pdf is not None:
    with st.spinner("Extracting text from PDF..."):
        try:
            extracted_text = extract_text_from_pdf(uploaded_pdf)
            st.success("✅ Text extracted from PDF.")
            st.text_area("📄 Extracted Text:", extracted_text, height=200)
            
            if st.button("🔍 Summarize PDF"):
                with st.spinner("Summarizing the extracted text..."):
                    try:
                        summary = summarize_text_groq(extracted_text)
                        st.success("✅ PDF Summary:")
                        st.write(summary)
                    except Exception as e:
                        st.error(f"❌ An error occurred: {e}")
        except RuntimeError as e:
            st.error(f"❌ {e}")
