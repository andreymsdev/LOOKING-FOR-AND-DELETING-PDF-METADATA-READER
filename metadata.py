# ========================
#  LOOKING FOR METADATAS
# ========================

import PyPDF2

def show_metadata(pdf_file):
    # Open the PDF file
    with open(pdf_file, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        meta = reader.metadata

    # Display PDF metadata
    print("Metadatas:")
    print(f"Author: {meta.author}")
    print(f"Title: {meta.title}")
    print(f"Subject: {meta.subject}")
    print(f"Creator: {meta.creator}")
    print(f"Producer: {meta.producer}")
    print(f"Creation Date: {meta.creation_date}")
    print(f"Modification Date: {meta.modification_date}")


# --- Logging output section ---
import sys  # Import sys before using it

class DualOutput:
    def __init__(self, file):
        self.terminal = sys.stdout
        self.log = open(file, "w", encoding="utf-8")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        self.terminal.flush()
        self.log.flush()


# Redirect print() to both terminal and file
sys.stdout = DualOutput("output.txt")

# Run the function
show_metadata("/home/andrey/Downloads/1761572574145.pdf")

print("\nSaved to the file!")
