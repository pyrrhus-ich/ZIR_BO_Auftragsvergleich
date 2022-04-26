from basic import *
from ExcelOeffnenUndLesen import *
from ExcelSchreiben import *
from compareAndClean import *

readSrc(src)
createSingleLists(valList,valList_BO, valList_ZIR)
print("valList hat die Länge {}".format(len(valList)))
print("Bo Liste hat die Lände von : {}".format(len(valList_BO)))
print("ZIR Liste hat die Länge von {}".format(len(valList_ZIR)))
cmpLst(valList_ZIR, valList_BO, valLstZIRInBO )
cleanList(valLstZIRInBO, valList_ZIR)
createDstFile(dstFile, valList_ZIR)