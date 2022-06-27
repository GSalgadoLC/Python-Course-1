import PyPDF2

with open("ImpostersHandbook.pdf", "rb") as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    page = reader.getPage(1)
    page.rotateClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)

    with open("rotated.pdf", "wb") as output:
        writer.write(output)

merger = PyPDF2.PdfFileMerger()
file_names = ["ImpostersHandbook.pdf", "rotated.pdf"]
for file_name in file_names:
    merger.append(file_name)
merger.write("combined.pdf")
