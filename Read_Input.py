import os
import pandas as pd
from langchain.document_loaders import UnstructuredPDFLoader
from unstructured.partition.pdf import partition_pdf
#from pdfminer import psparser



path = 'C:\Shilz\Shilz_Experiment\Shilz_Testina\ISTQB-CTFL_Syllabus_2018_v3.1.1.pdf'

def get_input(input_path):
    data_file = UnstructuredPDFLoader(input_path)
    docs = data_file.load()

    return docs

docs = get_input(path)
print(docs)


