from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path

FONT = "Helvetica"

for filepath in glob.glob("data/*xlsx"):
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    pdf = FPDF(orientation="portrait", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=False, margin=0)
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_number = filename.split('-')[0]
    pdf.set_font(family=FONT, style="B", size=20)
    pdf.cell(w=0, h=10, txt=f"Invoice {invoice_number}", ln=1)
    pdf.cell(w=0, h=10, txt="", ln=1)

    pdf.set_font(family=FONT, style="B", size=10)
    pdf.cell(w=20, h=10, txt="Index", ln=0, border=True)
    pdf.cell(w=60, h=10, txt="Product Name", ln=0, border=True)
    pdf.cell(w=40, h=10, txt="Amount Purchased", ln=0, border=True)
    pdf.cell(w=30, h=10, txt="Price per Unit", ln=0, border=True)
    pdf.cell(w=30, h=10, txt="Total Price", ln=1, border=True)

    total_price = 0.0
    for idx, row in df.iterrows():
        pdf.set_font(family=FONT, style="", size=10)
        pdf.cell(w=20, h=10, txt=str(idx), ln=0, border=True)
        pdf.cell(w=60, h=10, txt=row['product_name'], ln=0, border=True)
        pdf.cell(w=40, h=10, txt=str(row['amount_purchased']), ln=0, border=True)
        pdf.cell(w=30, h=10, txt=str(row['price_per_unit']), ln=0, border=True)
        pdf.cell(w=30, h=10, txt=str(row['total_price']), ln=1, border=True)
        total_price += float(row['total_price'])

    pdf.cell(w=0, h=10, txt="", ln=1)
    pdf.set_font(family=FONT, style="", size=12)
    pdf.cell(w=100, h=10, txt=f"Total Price to Pay: {total_price}", ln=1)

    output = Path("invoices", f"{invoice_number}.pdf")
    pdf.output(str(output))
