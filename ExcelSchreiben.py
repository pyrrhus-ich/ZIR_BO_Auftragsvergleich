import xlsxwriter 


  
def createDstFile(dstFile, list0):
    print("Beginne das schreiben der Excel Datei")
    workbook = xlsxwriter.Workbook(dstFile) 
    worksheet = workbook.add_worksheet() 
    row = 0
    column = 0
    content = list0
    for item in content : 
     worksheet.write(row, column, item) 
     row += 1  
     print(item)
    workbook.close() 
    print("Datei geschrieben")

 