import re
from colorama import *
init(autoreset=True)

# Sucht nach ZIR oder PP Aufträgen und druckt diese aus. 
def rxRepNr(srcLst, idx, sap):  # srcList = Jede Line im Excel ist ein Listenelement | idx = der Index an dem das zu durchsuchende Listelement sich befindet
    print("Starte mit dem suchen der Reparaturnummern rxRepNr()")
    matchResult = ""
    for line in srcLst:
        lineEl = str(line[idx])
        if lineEl is not None :
            match = re.findall(r"[MSms]" " ?" "\d{3}"" ?""-?" " ?" "\d{5,6}", lineEl)
            if match:
                #print("So sieht der Match aus => {}".format(match[0]))
                matchResult = match[0].capitalize() # Macht den Anfangsbuchstaben immer Groß unabhängig davon ob er vorher schon Groß war
                #print("Match sollte jetzt Grossen Anfangsbuchstaben haben {}".format(matchResult))
                matchResult = match[0].replace(" ", "") # Löscht alle Freizeichen im Result
                #print("Match sollte jetzt keine Freizeichen haben {}".format(matchResult))
                #Ab hier wird der fehlende Bindestrich eingefügt
                if matchResult.find("-")== -1 :          # Wenn kein Bindestrich vorhanden ist
                    matchResult = list(matchResult)      # mache aus dem Element eine Liste
                    matchResult.insert(4,"-")            # füge an Index 4 einen Bindestrich ein
                    matchResult = ''.join(matchResult)   # füge die einzelnen Listenelement wieder zu einem String zusammen
                    matchResult = matchResult.capitalize()
                    #print("Match sollte jetzt Bindestrich haben {}".format(matchResult))
            else:
                match = re.findall(r"\d{3}"" ?""-" " ?" "\d{5,6}", lineEl)
                if match:
                    matchResult = match[0]
                    nummerSap = line[sap][1:]
                    compare = matchResult[:3]
                    if nummerSap == compare:
                        matchResult = line[sap]+matchResult[3:]
                    else:                                              # Wenn es keinen Match gibt
                        matchResult = "1_Keine RepNr. gefunden"  
                else:                                              # Wenn es keinen Match gibt
                    matchResult = "1_Keine RepNr. gefunden" 
            matchResult = matchResult.capitalize()   
            line.insert(0, matchResult)              # füge das neu zusammengebaute Element an Index 0 ein
        else: 
                    
            line.insert(0, "1_Das zu durchsuchende Feld ist leer")            # Wenn das lineEl (Zeile 10)  leer ist füge an Index 0 der line den entsprechenden Text ein                
    srcLst[0][0] = "Suchergebnis"                                  # Ändere die Spaltenbezeichnung des Index 0
   

               
 