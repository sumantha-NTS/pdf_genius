import streamlit as st
from src.utils.pdf_utils import display_pdf

st.set_page_config(page_title="Chat with PDF - PDF Genius", page_icon="💬")

st.title("Chat with PDF")
st.caption(
    "Upload any PDF, and get answers to your questions instantly using advanced Retrieval-Augmented Generation (RAG) technology."
)
st.caption("Powered by OpenAI's GPT-4o-mini model")

with st.sidebar:
    st.header("Configuration")
    file = st.file_uploader(
        label="Upload PDF", type=["pdf"], accept_multiple_files=False
    )
    submit = st.button("Submit", use_container_width=True, type="primary")

if file and submit:
    st.toast("File uploaded successfully", icon="👍")

    # Display PDF
    with st.expander("View PDF"):
        st.markdown(display_pdf(file), unsafe_allow_html=True)

    st.info("RAG functionality is currently being integrated. Please check back soon!")

    # Placeholder for RAG logic
    # 1. Extract text from PDF
    # 2. Create embeddings
    # 3. Store in vector DB
    # 4. Chat interface

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask a question about your PDF"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response = "This is a placeholder response. RAG logic to be implemented."
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

else:
    if not file:
        st.warning("Please upload a PDF file to get started.")
