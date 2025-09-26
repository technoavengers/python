## Data Processing Libraries Overview

### 📄 Text (Documents, Logs, Messy Strings)
| Library      | Purpose                                      |
|--------------|----------------------------------------------|
| `re`         | Regex for pattern matching in text            |
| `nltk`       | Natural Language Toolkit (tokenization, stemming, stopwords) |
| `spaCy`      | Industrial NLP (entities, parsing)            |
| `textblob`   | Simple sentiment and text processing          |
| `gensim`     | Topic modeling, embeddings                    |

---

### 📑 PDFs, Word, HTML
| Library            | Purpose                                         |
|--------------------|-------------------------------------------------|
| `PyPDF2` / `pypdf` | Extract text from PDFs                          |
| `pdfplumber`       | Structured PDF extraction (tables, text)        |
| `docx` / `python-docx` | Work with Word files                     |
| `beautifulsoup4`   | Parse HTML, scrape text                         |

---

### 📊 Images
| Library      | Purpose                                  |
|--------------|------------------------------------------|
| `Pillow (PIL)` | Image loading, resizing, filtering     |
| `OpenCV`     | Computer vision, feature extraction      |
| `pytesseract`| OCR (convert scanned images to text)     |

---

### 🎧 Audio / Speech
| Library            | Purpose                              |
|--------------------|--------------------------------------|
| `librosa`          | Audio feature extraction             |
| `speechrecognition`| Convert speech to text               |
| `pydub`            | Manipulate audio files               |

---

### 🌐 Unstructured Data for LLMs
If preparing messy documents for AI/RAG pipelines:

- **`langchain`**: Loaders for PDFs, HTML, Notion, etc.
- **`unstructured`**: Extracts text and metadata from PDFs, Word, PowerPoint, HTML, images (`pip install unstructured`).
