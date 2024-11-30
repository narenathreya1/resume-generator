from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase.pdfmetrics import stringWidth
import io
import json

# ============================ DEV - 1 ====================================================
class resume_generator:
    def __init__(self):
        self.file_name = "resume.pdf"
        self.page_width, self.page_height = A4
        self.bold_font                    = "Helvetica-Bold"
        self.body_font                    = "Times-Roman"
        self.header_font_size             = 24
        self.section_header_font_size     = 16
        self.body_font_size               = 12
        self.small_font_size              = 10
        self.highlight_color              = "#1F4E79"
        self.text_color                   = colors.black
        self.margin                       = 50
        self.line_spacing                 = 15
        self.pdf_canvas                   = canvas.Canvas(self.file_name, pagesize=A4)
# ============================ DEV - 2 ====================================================

    def add_line_space(self, additional_space=0):
        if(self.page_height <= self.margin):
            self.pdf_canvas.showPage()
            self.page_width, self.page_height = A4
            self.page_height -= self.margin
        else:
            self.page_height -= self.line_spacing + additional_space
