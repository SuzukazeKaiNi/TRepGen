from docx import Document
import os
inputPath=r'/input'
print(inputPath)
docuName=os.listdir(inputPath)
print(docuName)
#document = Document(inputPath+docuName)
#FileRename=input('请输入单号（如20220202-02DT）')
#document.save('/output/'+FileRename+'.docx')