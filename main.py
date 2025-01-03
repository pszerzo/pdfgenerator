from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv", sep=",")
pdf = FPDF(orientation="P", unit="mm", format="A4") #A4 size: 298x210mm
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)  # rgb color
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)

    for k in range(23, 270, 10):
        pdf.line(10, k, 200, k)
    # A4 format: 210mm wide, (unit="mm"), x1-y1, x2-y2 coordinates)

    pdf.ln(250)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(row["Pages"]-1):
        pdf.add_page()

        for k in range(23, 270, 10):
            pdf.line(10, k, 200, k)

        pdf.ln(250+12)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("output.pdf")