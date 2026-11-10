# PDF Audiobook

A Python script that turns any PDF into an audiobook by reading it aloud, page by page.

## How it works

1. A file picker opens so you can choose a PDF.
2. [PyPDF2](https://pypi.org/project/PyPDF2/) extracts the text from each page.
3. [pyttsx3](https://pypi.org/project/pyttsx3/) reads the text aloud using your computer's built-in text-to-speech voice, so it works offline.

If the PDF can't be read (for example, a corrupted file), the script prints an error and exits.

## How to run

Requires Python 3 with Tkinter (included with most Python installs).

```bash
pip install -r requirements.txt
python3 pdf_to_audio.py
```

## Notes

- Scanned PDFs (images of text) have no text layer, so there's nothing to read aloud.

## Built with

- Python 3, PyPDF2, pyttsx3, Tkinter
