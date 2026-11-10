import pyttsx3 # pip install pyttsx3 that is used to convert text to speech
import PyPDF2 # pip install PyPDF2 that is used to read PDF files
from tkinter.filedialog import * # pip install tk that is used to open a file dialog to select the PDF file

book = askopenfilename()   # Open a file dialog to select the PDF file

try: # Try to read the PDF file using PyPDF2
    pdfreader = PyPDF2.PdfReader(book) 
except PyPDF2.errors.PdfReadError: # If the PDF file cannot be read, print an error message and exit the program
    print("Could not read the PDF. The file may be corrupted.")
    exit()

pages = len(pdfreader.pages) 
speaker = pyttsx3.init() 

for num in range(0, pages): # Loop through each page of the PDF file and extract the text, then use pyttsx3 to convert the text to speech
    page = pdfreader.pages[num]
    text = page.extract_text()
    speaker.say(text)
    speaker.runAndWait()
