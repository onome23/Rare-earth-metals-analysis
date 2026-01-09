from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib import colors
import markdown
import re

# ------------------------------
# 🔧 Markdown Parsing Helpers
# ------------------------------

def parse_markdown(md_text):
    """
    Convert Markdown into structured blocks (headings, text, list items, tables).
    Returns a list of (type, content) tuples.
    """
    blocks = []
    lines = md_text.split("\n")

    table_buffer = []

    for line in lines:
        line = line.rstrip()

        # Headings
        if line.startswith("# "):
            blocks.append(("h1", line[2:]))
        elif line.startswith("## "):
            blocks.append(("h2", line[3:]))
        elif line.startswith("### "):
            blocks.append(("h3", line[4:]))

        # Lists
        elif line.strip().startswith("* "):
            blocks.append(("li", line.strip()[2:]))

        # Tables
        elif "|" in line and "---" not in line:
            table_buffer.append(line)
        elif table_buffer:
            blocks.append(("table", table_buffer.copy()))
            table_buffer = []

        # Normal text
        else:
            if line.strip():
                blocks.append(("p", line))

    if table_buffer:
        blocks.append(("table", table_buffer))

    return blocks


# ------------------------------
# 🧩 PDF Builder
# ------------------------------

def build_pdf(input_md="README.md", output_pdf="REE_Project_Report_Pro.pdf"):

    with open(input_md, "r", encoding="utf-8") as f:
        md_raw = f.read()

    blocks = parse_markdown(md_raw)

    doc = SimpleDocTemplate(
        output_pdf,
        pagesize=letter,
        title="REE Market Analysis Report",
        author="Your Name"
    )

    styles = getSampleStyleSheet()

    # Custom styles
    h1 = ParagraphStyle("Heading1", parent=styles["Heading1"], fontSize=20, leading=26)
    h2 = ParagraphStyle("Heading2", parent=styles["Heading2"], fontSize=16, leading=22)
    h3 = ParagraphStyle("Heading3", parent=styles["Heading3"], fontSize=13, leading=18)

    body = ParagraphStyle("Body", parent=styles["Normal"], fontSize=11, leading=16)
    bullet = ParagraphStyle("Bullet", parent=styles["Normal"], leftIndent=20, bulletIndent=10)

    story = []

    # ------------------------------
    # COVER PAGE
    # ------------------------------
    story.append(Spacer(1, 150))
    story.append(Paragraph("<b>Rare Earth Elements (REE)</b>", h1))
    story.append(Paragraph("Production & Market Concentration Analysis", h2))
    story.append(Spacer(1, 20))
    story.append(Paragraph("Comprehensive Analysis Report", body))
    story.append(Spacer(1, 250))
    story.append(Paragraph("Generated Automatically via ReportLab", body))
    story.append(PageBreak())

    # ------------------------------
    # TABLE OF CONTENTS
    # ------------------------------
    toc = TableOfContents()
    toc.levelStyles = [h1, h2, h3]
    story.append(Paragraph("<b>Table of Contents</b>", h1))
    story.append(Spacer(1, 20))
    story.append(toc)
    story.append(PageBreak())

    # ------------------------------
    # MAIN REPORT CONTENT
    # ------------------------------
    for block_type, content in blocks:

        if block_type == "h1":
            story.append(Paragraph(content, h1))
            story.append(Spacer(1, 12))

        elif block_type == "h2":
            story.append(Paragraph(content, h2))
            story.append(Spacer(1, 10))

        elif block_type == "h3":
            story.append(Paragraph(content, h3))
            story.append(Spacer(1, 8))

        elif block_type == "p":
            story.append(Paragraph(content, body))
            story.append(Spacer(1, 8))

        elif block_type == "li":
            story.append(Paragraph(f"• {content}", bullet))

        elif block_type == "table":
            table_data = [row.split("|") for row in content]
            table = Table(table_data, repeatRows=1)
            table.setStyle(TableStyle([
                ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
                ("GRID", (0,0), (-1,-1), 0.5, colors.black),
                ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
                ("ALIGN", (0,0), (-1,-1), "LEFT"),
            ]))
            story.append(table)
            story.append(Spacer(1, 12))

    # ------------------------------
    # FOOTER PAGE NUMBERS
    # ------------------------------
    def add_page_number(canvas, doc):
        canvas.setFont("Helvetica", 9)
        canvas.drawString(500, 20, f"Page {doc.page}")

    doc.build(story, onLaterPages=add_page_number)
    print(f"\n🎉 Professional PDF generated: {output_pdf}\n")


if __name__ == "__main__":
    build_pdf()