import fitz
import re

def extract_text(file_path):
  doc = fitz.open(file_path) 
  text = "" 
  for page in doc: 
    text+=page.get_text() 
  text = text.replace("\n", "")
  return text