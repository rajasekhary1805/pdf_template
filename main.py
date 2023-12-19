from fpdf import FPDF
import pandas as pd


def ln_fn():
    # Set the Lines
    for i in range(20, 290, 10):
        pdf.line(10, i, 200, i)

    # Set the footer
    pdf.ln(270)
    pdf.set_font(family='Helvetica', size=10)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='R')


pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    # Set the Header
    pdf.add_page()
    pdf.set_font(family='Helvetica', size=24)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L')
    ln_fn()

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        ln_fn()

pdf.output('output.pdf')
