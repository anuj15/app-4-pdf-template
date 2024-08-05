import pandas as pd
from fpdf import FPDF

df = pd.read_csv('topics.csv')
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)
for index, row in df.iterrows():
    for i in range(row.Pages):
        pdf.add_page()
        for j in range(21, 285, 8):
            pdf.line(x1=10, y1=j, x2=200, y2=j)
        if i == 0:
            pdf.set_font(family='Times', style='B', size=20)
            pdf.set_text_color(100, 100, 100)
            pdf.cell(w=0, h=12, txt=row.Topic, border=0, ln=1, align='L')
            pdf.ln(260)
        else:
            pdf.ln(270)
        pdf.set_font(family='Times', style='I', size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=12, txt=row.Topic, border=0, ln=1, align='R')

pdf.output(name='output.pdf')
