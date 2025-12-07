import streamlit as st
from src.utils.pdf_utils import split_pdf, display_pdf
import zipfile
import io

st.set_page_config(page_title="Split PDF - PDF Genius", page_icon="✂️")

st.title("Split PDF")
st.markdown("Split a PDF file into individual pages.")

with st.sidebar:
    uploaded_file = st.file_uploader("Upload PDF file", type="pdf")
    split_button = st.button("Split PDF", type="primary")

if uploaded_file:
    st.write(f"📄 {uploaded_file.name}")

    # Display PDF
    st.markdown("### PDF Preview")
    st.markdown(display_pdf(uploaded_file), unsafe_allow_html=True)

    if split_button:
        with st.spinner("Splitting PDF..."):
            try:
                split_pages = split_pdf(uploaded_file)
                st.success(f"Successfully split into {len(split_pages)} pages!")

                # Create a zip file
                zip_buffer = io.BytesIO()
                with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
                    for i, page_pdf in enumerate(split_pages):
                        zip_file.writestr(f"page_{i+1}.pdf", page_pdf.getvalue())

                zip_buffer.seek(0)

                st.download_button(
                    label="Download All Pages (ZIP)",
                    data=zip_buffer,
                    file_name="split_pages.zip",
                    mime="application/zip",
                )

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
