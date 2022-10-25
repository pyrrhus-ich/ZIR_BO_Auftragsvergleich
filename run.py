from scripte.Variablen import *
from scripte.ExcelOeffnenUndLesen import *
from scripte.ExcelSchreiben import *
#from scripte.Reparaturnummer_extrahieren import *
from scripte.Regexp_Test import *


# Ab hier werden die Funktionen aufgerufen >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
readSrc(srcFile, dstList, maxColumn)
rxRepNr(dstList, idx, sapNridx)
createDstFile(dstFile, dstList)
input("Wir sind fertig 'ENTER' schliesst dieses Fenster ")