from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    # Set the Header
    pdf.add_page()
    pdf.set_font(family='Helvetica', size=24)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L')
    pdf.line(10, 21, 200, 21)

    # Set the footer
    pdf.ln(270)
    pdf.set_font(family='Helvetica', size=10)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='R')

    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # Set the footer
        pdf.ln(270)
        pdf.set_font(family='Helvetica', size=10)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=12, txt=row['Topic'], align='R')


pdf.output('output.pdf')