import streamlit as st
from src.utils.pdf_utils import rotate_pages, display_pdf
from pypdf import PdfReader

st.set_page_config(page_title="Rotate PDF - PDF Genius", page_icon="🔄")

st.title("Rotate PDF")
st.markdown("Rotate pages in your PDF document.")

with st.sidebar:
    uploaded_file = st.file_uploader("Upload PDF file", type="pdf")

    rotation = st.selectbox("Rotation Angle (Clockwise)", [90, 180, 270])

    apply_to = st.radio("Apply rotation to:", ["All Pages", "Specific Pages"])

    pages_to_rotate = None
    if apply_to == "Specific Pages":
        pages_str = st.text_input(
            "Enter page numbers to rotate (comma separated, e.g., 1, 3, 5)",
            help="Enter the page numbers you want to rotate.",
        )
        if pages_str:
            try:
                pages_to_rotate = [
                    int(p.strip()) for p in pages_str.split(",") if p.strip().isdigit()
                ]
            except ValueError:
                pass  # Validation happens on button click

    process_button = st.button("Rotate PDF", type="primary")

if uploaded_file:
    reader = PdfReader(uploaded_file)
    total_pages = len(reader.pages)
    st.write(f"📄 {uploaded_file.name} - {total_pages} pages")

    # Display PDF
    st.markdown("### PDF Preview")
    st.markdown(display_pdf(uploaded_file), unsafe_allow_html=True)

    if process_button:
        # Re-validate pages if specific
        valid_input = True
        if apply_to == "Specific Pages":
            if not pages_to_rotate:
                st.warning("Please enter valid page numbers to rotate.")
                valid_input = False
            else:
                invalid_pages = [p for p in pages_to_rotate if p < 1 or p > total_pages]
                if invalid_pages:
                    st.error(
                        f"Invalid page numbers: {invalid_pages}. Please enter numbers between 1 and {total_pages}."
                    )
                    valid_input = False

        if valid_input:
            with st.spinner("Rotating pages..."):
                try:
                    rotated_pdf = rotate_pages(uploaded_file, rotation, pages_to_rotate)
                    st.success("Pages rotated successfully!")

                    # Display Result
                    st.markdown("### Rotated PDF Preview")
                    st.markdown(display_pdf(rotated_pdf), unsafe_allow_html=True)

                    st.download_button(
                        label="Download Rotated PDF",
                        data=rotated_pdf,
                        file_name="rotated_document.pdf",
                        mime="application/pdf",
                    )
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
