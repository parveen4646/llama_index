import streamlit as st
import os

from app import parse_pdf, get_indexing
from llama_index import download_loader

# Load PDFPlumberReader
PDFPlumberReader = download_loader("PDFPlumberReader")

# Initialize PDFPlumberReader
loader = PDFPlumberReader()

# Custom CSS for styling
st.markdown("""
    <style>
        /* Main title */
        .title {
            color: #317C6E;
            font-size: 36px;
            text-align: center;
            padding: 20px;
            margin-bottom: 30px;
            border-bottom: 2px solid #317C6E;
        }

        /* Sidebar title */
        .sidebar-title {
            color: #317C6E;
            font-size: 24px;
            margin-top: 20px;
            margin-bottom: 10px;
        }

        /* File uploader label */
        .file-uploader-label {
            color: #317C6E;
            font-size: 18px;
        }

        /* Input text area */
        .input-text {
            color: #317C6E;
            font-size: 16px;
            padding: 10px;
            margin-bottom: 20px;
            border: 2px solid #317C6E;
            border-radius: 5px;
            width: 100%;
        }

        /* Output section */
        .output-section {
            margin-top: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# Main title
st.markdown('<h1 class="title">PDF Query & Extraction</h1>', unsafe_allow_html=True)

# Sidebar title
st.sidebar.markdown('<h2 class="sidebar-title">Upload PDF File</h2>', unsafe_allow_html=True)

# File uploader
upload_file = st.sidebar.file_uploader('', type='pdf', help='Only PDF files allowed')

# Input text area for query
input_text = st.sidebar.text_area('Write your query here', height=100)

if upload_file is not None:
    # Parse the PDF file
    document = parse_pdf(upload_file)

    if input_text:
        # Perform indexing
        st.sidebar.markdown('<h2 class="sidebar-title">Output</h2>', unsafe_allow_html=True)
        index = get_indexing(documents=document, input_text=input_text)
        st.markdown('<div class="output-section">{}</div>'.format(index), unsafe_allow_html=True)
