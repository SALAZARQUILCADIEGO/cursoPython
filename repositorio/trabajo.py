import aspose.words as aw
# load the PDF file
doc = aw.Document("semana.pdf")
# convertir PDF a Word en formato DOCX 
doc.save("semanadoc.docx")
