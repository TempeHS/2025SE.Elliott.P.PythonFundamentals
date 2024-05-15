[Home](../README.md) | [Lecture 8](8-OOP.md) | [Problem 8.1](PROBLEM8.1.md) | [Problem 8.2](PROBLEM8.2.md) | Problem 8.3

# CS50 Shirtificate
<img src="images/jharvard.png" width="300" />  

Suppose that you’d like to implement a CS50 “shirtificate,” a PDF with an image of an I took [CS50 t-shirt](https://cs50.harvardshop.com/collections/print/products/i-took-cs50-unisex-t-shirt), [shirtificate.png](images/shirtificate.png), customized with a user’s own name.

In a file called `shirtificate.py`, implement a program that prompts the user for their name and outputs, using [fpdf2](https://pypi.org/project/fpdf2/), a CS50 shirtificate in a file called `shirtificate.pdf` similar to this [one for John Harvard](files/jharvard.pdf), with these specifications:
- The `orientation` of the PDF should be Portrait.
- The `format` of the PDF should be A4, which is 210mm wide by 297mm tall.
- The top of the PDF should say “CS50 Shirtificate” as [text](https://py-pdf.github.io/fpdf2/Text.html), centered horizontally.
- The shirt’s [image](https://py-pdf.g297ithub.io/fpdf2/Images.html) should be centered horizontally.
- The user’s name should be on top of the shirt, in white [text](https://py-pdf.github.io/fpdf2/TextStyling.html).

All other details we leave to you. You’re even welcome to add borders, colors, and [lines](https://py-pdf.github.io/fpdf2/Shapes.html#lines). Your shirtificate needn’t match John Harvard’s precisely. And no need to wrap long names across multiple lines.

Before writing any code, do read through fpdf2’s [tutorial](https://py-pdf.github.io/fpdf2/Tutorial.html) to learn how to use it. Then skim fpdf2’s [API](https://py-pdf.github.io/fpdf2/fpdf/) (application programming interface) to see all of its functions and parameters therefor.

## Hints
- Note that fpdf2 comes with a `class` called `FPDF`, which has quite a few methods, per [py-pdf.github.io/fpdf2/fpdf/#fpdf.FPDF](https://py-pdf.github.io/fpdf2/fpdf/#fpdf.FPDF). You can install it with:

		pip install fpdf2
- Note that you can extend `FPDF` and instantiate your own subclass thereof in order to add a header to every page of a PDF, per [py-pdf.github.io/fpdf2/Tutorial.html#tuto-2-header-footer-page-break-and-image](https://py-pdf.github.io/fpdf2/Tutorial.html#tuto-2-header-footer-page-break-and-image). Or you can add it as text yourself.
- Note that you can disable automatic page breaks, which might otherwise cause your PDF to overflow from one page to two, with `set_auto_page_break`, per [py-pdf.github.io/fpdf2/Margins.html](https://py-pdf.github.io/fpdf2/Margins.html).
- Note that a [cell](https://py-pdf.github.io/fpdf2/Text.html#cell)’s height can be negative, to move it upward.
You can open `shirtificate.pdf`, once outputted, by clicking it in VS Code’s file explorer.

## Before You Begin
From the root of your repository execute `cd 8-OOP` So your current working directory is ...		

		/8-OOP $:
Next execute

		mkdir shirtificate
to make a folder called `shirtificate` in your codespace.

Then execute

		cd shirtificate
to change directories into that folder. You should now see your terminal prompt as `/8-OOP/shirtificate $`. You can now execute

		code shirtificate.py
to make a file called `shirtificate.py` where you’ll write your program.

# How to Test
Here’s how to test your code manually:
1. Run your program with `shirtificate.py`. Make sure your program prompts you for a name. Enter your own name and press Enter. Your program should create a file, `shirtificate.pdf`, containing the name you entered as input overlaid on a rendering of `shirtificate.png`.
2. Try a few other names for good measure, too!

# Commit your program to GITHUB
At the `/8-OOP/shirtificate $` prompt in your terminal:

		git add -A 
Add all changed files in the repository to be committed

		git commit -m “Upload completed shirtificate.py“
Commit all changes in the REPO with the comment “Upload completed shirtificate.py“
*note: If the file is not complete, adjust the comment to describes what is being commited*

		git push 
Push all changes to the REPO