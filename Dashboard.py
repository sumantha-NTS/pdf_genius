import streamlit as st
from streamlit import runtime
from streamlit.web import cli as stcli
import sys

st.set_page_config(
    page_title="PDF Genius",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)


def main():
    st.title("Welcome to PDF Genius 📚")
    st.markdown("### Your One-Stop Solution for PDF Processing")

    st.markdown(
        """
    PDF Genius provides a suite of powerful tools to manage your PDF documents efficiently.
    Select a tool from the sidebar to get started.
    """
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
        <div class="css-1r6slb0">
            <h3>📚 Merge PDFs</h3>
            <p>Combine multiple PDF files into a single document.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
        <div class="css-1r6slb0">
            <h3>✂️ Split PDF</h3>
            <p>Split a PDF file into individual pages or ranges.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
        <div class="css-1r6slb0">
            <h3>💬 Chat with PDF</h3>
            <p>Ask questions and get answers from your documents.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.markdown("### Other Tools")

    col4, col5 = st.columns(2)

    with col4:
        st.markdown(
            """
        <div class="css-1r6slb0">
            <h3>📄 Cut Pages</h3>
            <p>Remove specific pages from your PDF.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col5:
        st.markdown(
            """
        <div class="css-1r6slb0">
            <h3>🔄 Rotate PDF</h3>
            <p>Rotate pages in your PDF document.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )


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
