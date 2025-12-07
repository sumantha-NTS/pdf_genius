import streamlit as st
from src.utils.pdf_utils import merge_pdfs, display_pdf
import io

st.set_page_config(page_title="Merge PDFs - PDF Genius", page_icon="📚")

st.title("Merge PDFs")
st.markdown("Combine multiple PDF files into a single document.")

with st.sidebar:
    uploaded_files = st.file_uploader(
        "Upload PDF files",
        type="pdf",
        accept_multiple_files=True,
        help="Drag and drop multiple PDF files here.",
    )
    merge_button = st.button("Merge PDFs", type="primary")

if uploaded_files:
    st.write(f"Selected {len(uploaded_files)} files:")
    for file in uploaded_files:
        st.text(f"📄 {file.name}")

    if merge_button:
        if len(uploaded_files) < 2:
            st.warning("Please upload at least 2 PDF files to merge.")
        else:
            with st.spinner("Merging PDFs..."):
                try:
                    merged_pdf = merge_pdfs(uploaded_files)
                    st.success("PDFs merged successfully!")

                    # Display Result
                    st.markdown("### Merged PDF Preview")
                    st.markdown(display_pdf(merged_pdf), unsafe_allow_html=True)

                    st.download_button(
                        label="Download Merged PDF",
                        data=merged_pdf,
                        file_name="merged_document.pdf",
                        mime="application/pdf",
                    )
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
