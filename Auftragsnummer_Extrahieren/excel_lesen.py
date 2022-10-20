import openpyxl as op
import os
import re

srcFile = os.getcwd() + "\\ZIR_BO_Auftragsvergleich\\Auftragsnummer_Extrahieren\\Basis_PY.xlsx"
srcList = []
srcELeList = []
columnHead = ""

reparaturAuftragsnummer = r"^[M|S]{1}[0-9]{3,3}-[0-9]{5,6}" # definiert die Suchkriterien

#Lädt das Excel File und schreibt die Werte einer bestimmten Spalte in eine Liste
def readSrcFileColumn(srcFile, dstList, srcColumn): # srcFile = Das ExcelFile | dstList = die Zielvariable | srcColumn = Index der srcSpalte
    wb = op.load_workbook(srcFile,data_only=True) # lädt das File
    ws = wb.worksheets[0]
    #schreibt die Werte in eine Liste wenn der erste value der Zeile nicht none ist
    for value in ws.iter_rows(min_row=1, values_only=True):
            if value[0] is not None:
                dstList.append(value[srcColumn])

def loadValToSrcList(base, dst):
    columnHead = base[0]  # speichert die Überschrift in einer extra Variable
    for el in base:       # Für jedes Element in der base List
        x = el.split()    # splittet das Element und speichert das resultat in Liste X
        for ele in x:     # 
            dst.append(ele)
    dst.pop(0)
    print(columnHead)
    print(dst)

readSrcFileColumn(srcFile,srcList,0)
loadValToSrcList(srcList, srcELeList)


