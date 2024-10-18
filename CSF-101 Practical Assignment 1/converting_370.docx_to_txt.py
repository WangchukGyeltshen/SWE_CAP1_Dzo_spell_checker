import docx2txt as d2t

dfile="370.docx"
tfile="370.txt"

doc=d2t.process(dfile)

file=open(tfile, "w", encoding="utf-8")
file.write(doc)
file.close()

print("file converted")