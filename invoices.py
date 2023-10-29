from fpdf import FPDF
import pandas as pd
import glob
import openpyxl


for file_path in glob.glob("data/*xlsx"):
    df = pd.read_excel(file_path, sheet_name="Sheet 1")
    print(df)
