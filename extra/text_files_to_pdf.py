from pathlib import Path
from fpdf import FPDF
import glob

pdf = FPDF(orientation="portrait", format="A4", unit="mm")

for filepath in glob.glob("text_files/*txt"):
    with open(filepath) as file:
        pdf.add_page()
        filename = Path(filepath).stem
        pdf.set_font(family="Helvetica", style="B", size=16)
        pdf.cell(w=50, h=10, txt=filename.capitalize(), ln=1)
        text = file.read()
        pdf.set_font(family="Helvetica", style="", size=12)
        pdf.write(h=10, txt=text)

pdf.output("output.pdf")
