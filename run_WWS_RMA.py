from scripte.WWS_Retoure.Variablen_WWSRetoure import *
from scripte.ExcelOeffnenUndLesen import *
from scripte.ExcelSchreiben import *
#from scripte.WWS_Retoure.Regexp_WWSRetoure import *
from scripte.WWS_Retoure.NEW_Regexp_WWSRetoure import *
from scripte.HifsScripte import printLen, srcListExcelInsertColumn



# Ab hier werden die Funktionen aufgerufen >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
readSrc(srcFile, srcLstExcel, maxColumn)
printLen(srcLstExcel, resultList)
srcListExcelInsertColumn(srcLstExcel, resultList)
searchSR(srcLstExcel, idx, resultList)
printLen(srcLstExcel, resultList)
searchSRohneBuchstaben(srcLstExcel, idx, resultList, sapNridx)
printLen(srcLstExcel, resultList)
#for el in resultList: print(el)
createDstFile(dstFile, resultList)
#input("Wir sind fertig 'ENTER' schliesst dieses Fenster ")