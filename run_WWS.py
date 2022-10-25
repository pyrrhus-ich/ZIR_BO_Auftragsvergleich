from scripte.WWS_Retoure.Variablen_WWSRetoure import *
from scripte.ExcelOeffnenUndLesen import *
from scripte.ExcelSchreiben import *
from scripte.WWS_Retoure.Regexp_WWSRetoure import *



# Ab hier werden die Funktionen aufgerufen >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
readSrc(srcFile, dstList, maxColumn)
rxRepNr(dstList, idx, sapNridx)
createDstFile(dstFile, dstList)
input("Wir sind fertig 'ENTER' schliesst dieses Fenster ")