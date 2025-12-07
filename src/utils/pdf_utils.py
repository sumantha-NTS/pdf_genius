import io
from pypdf import PdfReader, PdfWriter
from typing import List, Union, BinaryIO
import base64


def merge_pdfs(files: List[BinaryIO]) -> io.BytesIO:
    """Merge multiple PDF files into a single PDF."""
    merger = PdfWriter()
    for file in files:
        merger.append(file)

    output = io.BytesIO()
    merger.write(output)
    merger.close()
    output.seek(0)
    return output


def split_pdf(file: BinaryIO) -> List[io.BytesIO]:
    """Split a PDF into individual pages."""
    reader = PdfReader(file)
    output_files = []

    for i in range(len(reader.pages)):
        writer = PdfWriter()
        writer.add_page(reader.pages[i])
        output = io.BytesIO()
        writer.write(output)
        writer.close()
        output.seek(0)
        output_files.append(output)

    return output_files


def remove_pages(file: BinaryIO, pages_to_remove: List[int]) -> io.BytesIO:
    """
    Remove specific pages from a PDF.
    pages_to_remove: List of 1-based page numbers to remove.
    """
    reader = PdfReader(file)
    writer = PdfWriter()

    # Convert 1-based to 0-based
    pages_to_remove_0 = [p - 1 for p in pages_to_remove]

    for i in range(len(reader.pages)):
        if i not in pages_to_remove_0:
            writer.add_page(reader.pages[i])

    output = io.BytesIO()
    writer.write(output)
    writer.close()
    output.seek(0)
    return output


def rotate_pages(
    file: BinaryIO, rotation: int, pages: Union[List[int], None] = None
) -> io.BytesIO:
    """
    Rotate pages in a PDF.
    rotation: Degrees to rotate (90, 180, 270).
    pages: List of 1-based page numbers to rotate. If None, rotate all.
    """
    reader = PdfReader(file)
    writer = PdfWriter()

    # Convert 1-based to 0-based if pages provided
    pages_0 = [p - 1 for p in pages] if pages else None

    for i in range(len(reader.pages)):
        page = reader.pages[i]
        if pages_0 is None or i in pages_0:
            page.rotate(rotation)
        writer.add_page(page)

    output = io.BytesIO()
    writer.write(output)
    writer.close()
    output.seek(0)
    return output


def display_pdf(file: BinaryIO):
    """
    Display PDF in Streamlit app using an iframe.
    """
    # Read file as bytes:
    bytes_data = file.getvalue()

    # Convert to base64
    base64_pdf = base64.b64encode(bytes_data).decode("utf-8")

    # Embed PDF in HTML
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600" type="application/pdf"></iframe>'

    return pdf_display
