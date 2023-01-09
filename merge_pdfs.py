from PyPDF2 import PdfMerger
import os
import sys

dp = sys.argv[1]

if os.path.exists(dp):
    print(f'''merging pdf in directory {dp}''')
    # file exists
else:
    print("no such directory with pdfs")
    exit()

onlyfiles = [f for f in os.listdir(dp) if os.path.isfile(os.path.join(dp, f))]

onlyfiles.sort()

pdfs = []

merger = PdfMerger()

for file in onlyfiles:
    if ".pdf" in file:
        pdfs.append(file)
        merger.append(dp+"/"+file)

merger.write(dp+"/"+"result.pdf")
merger.close()
print("following pdfs merged in to one", pdfs)
