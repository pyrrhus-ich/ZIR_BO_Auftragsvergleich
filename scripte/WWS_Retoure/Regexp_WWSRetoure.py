import re
from colorama import *
init(autoreset=True)




# Sucht nach ZIR oder PP Aufträgen und druckt diese aus. 
def rxRepNr(srcLst, idx, sap):  # srcList = Jede Line im Excel ist ein Listenelement | idx = der Index an dem das zu durchsuchende Listelement sich befindet
    print("Starte mit dem suchen der Reparaturnummern rxRepNr()")
    for line in srcLst:
        lineEl = str(line[idx])
        matchResult = ""
        matchRMA = ""
        nummerSap = line[sap][1:] # die Zahlen der Sap Nr aus M199 wird 199
        if lineEl is not None :
            match = re.findall(r"[MSms]" " ?" "\d{3}"" ?""-?" " ?" "\d{5,6}", lineEl)
            if match:
                #print("So sieht der Match aus => {}".format(match[0]))
                #matchResult = match[0].capitalize() # Macht den Anfangsbuchstaben immer Groß unabhängig davon ob er vorher schon Groß war
                print("21 - match nach match {}".format(matchResult))
                #print("Match sollte jetzt Grossen Anfangsbuchstaben haben {}".format(matchResult))
                matchResult = match[0].replace(" ", "") # Löscht alle Freizeichen im Result
                matchResult = match[0].capitalize()
                print("24 - Match nach Entfernen der Freizeichen {}".format(matchResult))
                #Ab hier wird der fehlende Bindestrich eingefügt
                if matchResult.find("-")== -1 :          # Wenn kein Bindestrich vorhanden ist
                    print("28 - Hier ist kein Bindestrich vorhanden {}".format(matchResult))
                    matchResult = list(matchResult)      # mache aus dem Element eine Liste
                    print("30 - Dies sollte eine Liste sein {}".format(matchResult))
                    matchResult.remove(" ")  # Entfernt die Freizeichen aus der Liste
                    print("32 - Dies sollte eine Liste ohne Freizeichen sein {}".format(matchResult))
                    lstCoc = matchResult[0:4]            # Schneide aus der MatchResult Liste die ersten 4 elemente. Ist immer noch ne Liste
                    ind1LstCoc = int(lstCoc[1])          # Dient der Prüfung ob die Zahl nach den Buschstaben ins Muster passt (im nächsten if)
                    lstCoc = ''.join(lstCoc)             # Macht aus der lstDoc einen String z.B M390
                    if lstCoc == "M860" or lstCoc == "S802" or (ind1LstCoc >= int(1) and ind1LstCoc <= int(2)): # M860 oder S802 sind die beiden Online Märkte
                        matchResult.insert(4,"-")            # füge an Index 4 einen Bindestrich ein
                        matchResult = ''.join(matchResult)   # füge die einzelnen Listenelement wieder zu einem String zusammen
                        matchResult = matchResult.capitalize()
                        print("35 - Match sollte jetzt Bindestrich haben {}".format(matchResult))
                    else:
                        pass
                else:
                    pass
            
            else:
                match = re.findall(r"\d{3}""-""\d{5,6}", lineEl) # Suche nach Nr wo der Marktbuchstabe fehlt
                if match:
                    matchResult = match[0]
                    
                    buchstabeSAP = line[sap][:1]
                    compare = matchResult[:3] # die ersten 3 Stellen der gefundenen Nr
                    #print("Buchstabe fehlt im Infofeld =>")
                    #print("55 - Die letzte 3 Stellen der Marktnummer: {}".format(nummerSap))
                    #print("56 - Der Buchstabe der SAP Nr. ist {}".format(buchstabeSAP))
                    #print("57 - Die ersten drei Buchstaben aus dem Infofeld: {}".format(compare))
                    if nummerSap == compare: # wenn die beiden gleich sind handelt es sich wahrscheinlich um eine Rep.Nr der der Buchstabe fehlt
                        matchResult = line[sap]+matchResult[3:] # Dann verkette die SAP Nr des Marktes mit der gefundenen Nr ab dem Bindestrich M111 + -12345
                        print("61 - Compare passt : {}\n".format(matchResult))
                    else:                                              # Wenn es keinen Match gibt
                        matchResult = "1_Keine RepNr. gefunden" 
                        print("64 - Compare passt nicht {} <> {}\n".format(nummerSap, compare))

                else: # Ab hier suchen wir die RMA - Nr
                    match = re.findall(r" ?""[2][0-9]{6}" , lineEl)
                    if match:
                        matchRMA = match[0].replace("0", "").lstrip()
                        #print("RMA NR Suche =>")
                        #print("RMA Nr gefunden: {}".format(matchRMA))
                        lengRMA = len(matchRMA)
                        if len(matchRMA) == 7:
                            matchRMA = matchRMA
                            #print("Länge der RMA Nr. passt, {} wird übernommen ins dstFile\n".format(matchRMA))
                        else:
                            matchRMA = "-"
                            matchResult = "1_Keine RepNr. gefunden"
                            #print("RMA Nr - Länge passt nicht. Geforderte Länge 7 Tatsächlich: {}\n".format(lengRMA))
                    else:
                        matchRMA = "-" 
                        matchResult = "1_Keine RepNr. gefunden"
            
        else:                                        # wenn die Zeile leer ist       
            matchResult = "1_Das zu durchsuchende Feld ist leer"          # Wenn das lineEl (Zeile 10)  leer ist füge an Index 0 der line den entsprechenden Text ein 

   
    
    line.insert(0, matchResult)              # füge das neu zusammengebaute Element an Index 0 ein 
    line.insert(1, matchRMA)              
    srcLst[0][0] = "Suchergebnis"                                  # Ändere die Spaltenbezeichnung des Index 0
    srcLst[0][1] = "RMA WWS"
   

               
 