import sys
import streamlit as st
from streamlit import runtime
from streamlit.web import cli as stcli
from PIL import Image

st.set_page_config(
    page_title="PDF Genius",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

def main():
    with st.sidebar:
        st.title("PDF Genius")
        st.caption("Upload any PDF, and get answers to your questions instantly using advanced Retrieval-Augmented Generation (RAG) technology.")
        st.caption("Powered by OpenAI's GPT-4o-mini model")
        
        file = st.file_uploader(label="Upload PDF", type=["pdf"], accept_multiple_files=False)
        
        submit = st.button("Submit", use_container_width=True, type="primary")
        
    if file and submit:
        st.toast("File uploaded successfully", icon="👍")
    else:
        st.sidebar.warning("Please upload a PDF file and click 'Submit' to get started.")
    
if __name__ == "__main__":
    if runtime.exists():
        main()
    else:
        sys.argv = [
            "streamlit",
            "run",
            sys.argv[0],
            "--server.port",
            "8501",
            "--server.address",
            "0.0.0.0",
            "--server.headless",
            "true",
            "--theme.base",
            "dark",
        ]
        sys.exit(stcli.main())