from scripte.LIEFERANT.LIEF_VAR import *
from scripte.ExcelOeffnenUndLesen import *
from scripte.ExcelSchreiben import *
from scripte.LIEFERANT.LIEF_REGEX import *


# Ab hier werden die Funktionen aufgerufen >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
readSrc(srcFile, dstList, maxColumn)
rxRepNr(dstList, idx)
createDstFile(dstFile, dstList)
input("Wir sind fertig 'ENTER' schliesst dieses Fenster ")