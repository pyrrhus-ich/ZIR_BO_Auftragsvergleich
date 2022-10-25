import re
from colorama import *
init(autoreset=True)

# Sucht nach ZIR oder PP Aufträgen und druckt diese aus. 
def rxRepNr(srcLst, idx):  # srcList = Jede Line im Excel ist ein Listenelement | idx = der Index an dem das zu durchsuchende Listelement sich befindet
    print("Starte mit dem suchen der Reparaturnummern rxRepNr()")
    lensrcList = len(srcLst)
    cnt = 0
    for line in srcLst:
        lineEl = line[idx]
        matchResult = ""
        if lineEl is not None:
        
            searchList = lineEl.split(" ")                             # Trennt den Text bei jedem Freizeichen
            lenSearchList = len(searchList)                            # Anzahl der zu durchsuchenden Elemente
            countNoEl = 0                                              # Wird bei jedem nicht gefundenem Element 1 hochgezählt
            for el in searchList:
                match = re.findall("[MSms]" "\d{3}""-?""\d{5,6}", el) #Sucht alle Aufträge die mit großem oder kleinem m oder s anfangen und dann 3 Zahlen
                                                                       # gefolgt von einem oder keinem Bindestrich plus 5 oder 6 weitere Zahlen
                if match :
                    matchResult = match[0].capitalize() # Macht den Anfangsbuchstaben immer Groß unabhängig davon ob er vorher schon Groß war
                    #Ab hier wird der fehlende Bindestrich eingefügt
                    if matchResult.find("-")== -1 :          # Wenn kein Bindestrich vorhanden ist
                        matchResult = list(matchResult)      # mache aus dem Element eine Liste
                        matchResult.insert(4,"-")            # füge an Index 4 einen Bindestrich ein
                        matchResult = ''.join(matchResult)   # füge die einzelnen Listenelement wieder zu einem String zusammen
                    line.insert(0, matchResult)              # füge das neu zusammengebaute Element an Index 0 ein
                    cnt += 1                                 # zähle einen hoch (Nur für Statistik)
                      
                else:                                              # Wenn es keinen Match gibt
                    countNoEl += 1                                 # zähle die Variable 'countNoEl' um einen hoch       
            if lenSearchList == countNoEl:                         # vergleiche die Länge der Suchliste mit der Anzahl der nicht gefundenen Elemente
                line.insert(0, "1_Keine Reparaturnummer gefunden") # Wenn die Länge gleich ist gab es keinen Match also füge an Index 0 den Text ein
        else:                                                      # Wenn das lineEl (Zeile 10)  leer ist füge an Index 0 der line den entsprechenden Text ein
            line.insert(0, "1_Das zu durchsuchende Feld ist leer")                            
    srcLst[0][0] = "Suchergebnis"                                  # Ändere die Spaltenbezeichnung des Index 0
    print(Fore.GREEN + "Vergleich der Reparaturnummern ist abgeschlossen rxRepNr(). Zeilen gelesen : {} Reparaturnummern gefunden {}\n".format(lensrcList, cnt))
    
