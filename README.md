# LOOKING FOR AND DELETING PDF METADATA READER

<p align="left">
  <img src="images/pingu.jpeg" alt="PDF PINGU" width="500">
</p>

Metadata plays an important role in digital documents it stores hidden information such as the author’s name, creation date, software used, and sometimes even file history.

---

***A simple Python script that reads and displays PDF metadata (author, title, subject, etc.) and saves the output to a `.txt` file***

# How does it work?

* [metadata.py](metadata.py) Reads the metadata content, such as author, title, and other fields.
* [nometadata](nometadata).py Checks if the PDF has any metadata, and if so, removes it.

---

# Requirements

Make sure you have **Python 3** and **PyPDF2** installed.

```bash
pip install PyPDF2
```

---

# How to Use

1. Place your PDF file anywhere on your system.
2. Update the file path in the code:

```python
show_metadata("/path/to/your/file.pdf")
```

---

# Hope you enjoy this!

While metadata can be useful for document management and authenticity, it can also unintentionally expose personal or sensitive information.

That’s why it’s a good practice to review and occasionally remove metadata, especially before sharing PDFs publicly or sending them to unknown recipients.

<p align="left">
  <img src="images/pingu2.jpeg" alt="PDF PINGU" width="450">
</p>
