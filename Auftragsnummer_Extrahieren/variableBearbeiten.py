import re

varLst = ['M017-25388,', 'R9YRC0THJDZ', 'm199-123456-r-c-rd', "M9999999999KL125",'M171-245606-R-SD,', '0HBJ3HYRB03034W', 's31723553-S-R-SD,', '0FQS3HUNB01591V', 'S327-18626', 'S058-25019-R-SD', 'M087-19383', 'RFANA3A076D,', 'S036-17239', 'RFAMB3289YV,', 'M053-19219-R-C', '0FQS3HUNB01591V,', 'S317-23553-S-R-SD,']

# hier wird von jedem Element in varLst wenn vorhanden das Komma entfernt, anschliessend werden die Elemente
# am entsprechenden Index der varList überschrieben. Das Ergebnis ist eine neue Liste mit den selben Werten ohne die Kommas am Ende
def kommaEntfernen(ListName):
    for el in ListName:
        x = ListName.index(el)
        ListName[x] = el[:-1] if el.endswith(",") else el

# Sucht nach ZIR oder PP Aufträgen und druckt diese aus. 
def rxRepNr(suchString):
    treffer = re.search("[M | S | m | s]" "\d{3}""-""\d{5,6}", suchString) #Sucht alle Aufträge die mit großem oder kleinem m oder s anfangen und dann 3 Zahlen
    # gefolgt von einem Bindestrich plus 5 oder 6 weitere Zahlen
    if treffer :
        if len(treffer.group()) < 11:
            print("ZIR Order Nr ", treffer.group())
        else:
            print("PP Order Nr : " + treffer.group())
    
    

kommaEntfernen(varLst)
for el in varLst:
    rxRepNr(el)
    


   



    

    
    
    
    