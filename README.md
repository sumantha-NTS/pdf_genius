# PDF Genius 📚

PDF Genius is your one-stop solution for PDF processing. It offers a suite of powerful tools to manage your PDF documents efficiently, all within a modern, user-friendly interface.

## Features

### 🛠️ PDF Tools
- **Merge PDFs**: Combine multiple PDF files into a single document.
- **Split PDF**: Split a PDF file into individual pages and download them as a ZIP archive.
- **Cut Pages**: Remove specific pages from your PDF document.
- **Rotate PDF**: Rotate pages by 90, 180, or 270 degrees.

### 💬 Chat with PDF
- **RAG Technology**: Upload any PDF and get answers to your questions instantly using advanced Retrieval-Augmented Generation (RAG) technology.
- **Powered by OpenAI**: Utilizes GPT-4o-mini for accurate and context-aware responses.

## Getting Started

### Prerequisites
- Python 3.8+
- OpenAI API Key (for Chat feature)

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-repo/pdf_genius.git
    cd pdf_genius
    ```

2.  Install dependencies:
    ```bash
    pip install streamlit pypdf python-dotenv
    ```

3.  Set up environment variables:
    Create a `.env` file in the `src/config` directory (or root) and add your OpenAI API key:
    ```env
    OPENAI_API_KEY=your_api_key_here
    ```

### Running the App

**Standard Mode:**
```bash
streamlit run Dashboard.py
```

**Headless Mode (Deployment):**
```bash
./start.sh
```

## Usage
1.  Launch the app.
2.  Use the sidebar to navigate between different tools.
3.  Upload your PDF files via the sidebar.
4.  Configure options (e.g., pages to remove, rotation angle) in the sidebar.
5.  View previews of your uploaded and processed documents in the main area.
6.  Download your results!

## License
[MIT License](LICENSE)
