from fpdf import FPDF
import pandas

topics_csv = pandas.read_csv("topics.csv", sep=",")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(False, margin=0)

for index, row in topics_csv.iterrows():
    topic = row["Topic"]
    pages = row["Pages"] - 1
    #Set the header
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=topic, border=0, ln=1, align="L")
    pdf.line(x1=10, y1=21, x2=200, y2=21)

    # Set the footer
    pdf.ln(258)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=topic, align="R")

    if pages:
        for i in range(pages):
            pdf.add_page()

            #Set the footer
            pdf.ln(270)
            pdf.set_font(family="Times", style="I", size=8)
            pdf.set_text_color(180, 180, 180)
            pdf.cell(w=0, h=10, txt=topic, align="R")

pdf.output("my_file.pdf")