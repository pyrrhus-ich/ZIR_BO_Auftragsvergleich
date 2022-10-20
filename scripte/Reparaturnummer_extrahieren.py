import re
from colorama import *
init(autoreset=True)

# Sucht nach ZIR oder PP Aufträgen und druckt diese aus. 
def rxRepNr(suchString):
    if suchString is not None:
        match = re.search("[M | S | m | s]" "\d{3}""-""\d{5,6}", suchString) #Sucht alle Aufträge die mit großem oder kleinem m oder s anfangen und dann 3 Zahlen
                                                                            # gefolgt von einem Bindestrich plus 5 oder 6 weitere Zahlen
        if match :
            return match.group()
        else:
            match = re.search("[M|S|m|s]" "\d{8,9}" , suchString) # sucht nach allen Reparaturnummern die keinen Bindestrich in der Mitte haben
            if match :
                x = match.group()
                y = []
                for el in x: y.append(el)
                y.insert(4, "-")
                x = "".join(y)
                return x
            else:
                return "1_Nichts gefunden"
    else:
        return "1_Suchfeld ist leer"

 

# Ruft die vorherige Funktion rxRepNr() auf und schreibt die Werte auf Index 0 des jeweiligen Listelementes
# Zum Schluss ändert die Funktion noch die Spaltenbezeichnung
def writeRepNr(srcList , idx):
    print("Starte mit dem Vergleichen der Werte writeRepNr() ")
    for el in srcList:
        val = el[idx]
        newVal = rxRepNr(val)
        el.insert(0,newVal)
    print(Fore.GREEN + "Vergleich der Werte ist abgeschlossen writeRepNr() ")
    srcList[0][0]="Auftragsnummer"
   



    

    
    
    
    