from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")

pdf = FPDF(orientation="portrait", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for idx, row in df.iterrows():
    for i in range(row['Pages']):
        pdf.add_page()
        pdf.set_font(family="Times", style="", size=20)
        txt = f"{int(idx) + 1}. {row['Topic']}"
        pdf.cell(w=0, h=10, txt=txt, ln=1)
        pdf.set_line_width(0.6)
        pdf.line(10, 20, 200, 20)
        pdf.set_line_width(0.3)

        for i in range(25):
            pdf.line(10, 31 + (i * 10), 200, 31 + (i * 10))

        pdf.ln(260)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.cell(w=0, h=10, txt=row['Topic'], ln=1, align="R")

pdf.output("output.pdf")
