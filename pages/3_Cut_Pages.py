import streamlit as st
from src.utils.pdf_utils import remove_pages, display_pdf
from pypdf import PdfReader

st.set_page_config(page_title="Cut Pages - PDF Genius", page_icon="✂️")

st.title("Cut Pages")
st.markdown("Remove specific pages from your PDF.")

with st.sidebar:
    uploaded_file = st.file_uploader("Upload PDF file", type="pdf")

    pages_to_remove_str = st.text_input(
        "Enter page numbers to remove (comma separated, e.g., 1, 3, 5)",
        help="Enter the page numbers you want to delete.",
    )

    process_button = st.button("Remove Pages", type="primary")

if uploaded_file:
    reader = PdfReader(uploaded_file)
    total_pages = len(reader.pages)
    st.write(f"📄 {uploaded_file.name} - {total_pages} pages")

    # Display PDF
    st.markdown("### PDF Preview")
    st.markdown(display_pdf(uploaded_file), unsafe_allow_html=True)

    if process_button:
        if not pages_to_remove_str:
            st.warning("Please enter page numbers to remove.")
        else:
            try:
                # Parse input
                pages_to_remove = [
                    int(p.strip())
                    for p in pages_to_remove_str.split(",")
                    if p.strip().isdigit()
                ]

                # Validate pages
                invalid_pages = [p for p in pages_to_remove if p < 1 or p > total_pages]
                if invalid_pages:
                    st.error(
                        f"Invalid page numbers: {invalid_pages}. Please enter numbers between 1 and {total_pages}."
                    )
                else:
                    with st.spinner("Removing pages..."):
                        new_pdf = remove_pages(uploaded_file, pages_to_remove)
                        st.success("Pages removed successfully!")

                        # Display Result
                        st.markdown("### Processed PDF Preview")
                        st.markdown(display_pdf(new_pdf), unsafe_allow_html=True)

                        st.download_button(
                            label="Download Processed PDF",
                            data=new_pdf,
                            file_name="cut_document.pdf",
                            mime="application/pdf",
                        )
            except ValueError:
                st.error("Invalid input. Please enter numbers separated by commas.")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
