from scripte.LIEFERANT.Variablen_LIEFERANT import *
from scripte.ExcelOeffnenUndLesen import *
from scripte.ExcelSchreiben import *
from scripte.LIEFERANT.Regexp_Lieferant import *


# Ab hier werden die Funktionen aufgerufen >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
readSrc(srcFile, dstList, maxColumn)
rxRepNr(dstList, idx, sapNridx)
createDstFile(dstFile, dstList)
input("Wir sind fertig 'ENTER' schliesst dieses Fenster ")