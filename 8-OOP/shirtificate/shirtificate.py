from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 15)
        # Calculating width of title and setting cursor position:
        width = self.get_string_width(self.title) + 6
        self.set_x((210 - width) / 2)
        # Setting colors for frame, background and text:
        self.set_draw_color(0, 80, 180)
        self.set_fill_color(230, 230, 0)
        self.set_text_color(220, 50, 50)
        # Setting thickness of the frame (1 mm)
        self.set_line_width(1)
        # Printing title:
        self.cell(width, 9, self.title, 0, 1, "C", 1)
        # Performing a line break:
        self.ln(10)

    def footer(
        self,
    ):
        # pdf.set_margins(0)
        # Ensure the image path is correct and the method is called correctly
        pX = (210 * 0.75) / 2
        pY = (297 * 0.75) / 2
        iX = 50
        iY = 50
        X = pX - iX
        Y = pY - iY
        self.image("8-OOP/images/shirtificate.png", Align="C", y=50)
        # Adjusted y position to not overlap with content
        self.set_y(-15)  # Position at 15 mm from bottom
        self.set_font("helvetica", "I", 8)


student = input("What's your name? ")
pdf = PDF()
pdf.set_title("CS50 Shirtificate")
pdf.set_author(student)
pdf.add_page()
pdf.output("tuto3.pdf")
