import re
from colorama import *
init(autoreset=True)

# Sucht nach ZIR oder PP Aufträgen und druckt diese aus. 
def rxRepNr(srcLst, idx):  # srcList = Jede Line im Excel ist ein Listenelement | idx = der Index an dem das zu durchsuchende Listelement sich befindet
    cntSrcLst = len(srcLst)
    cntLelNotNone = 0
    cntMatch = 0
    cntNoMatch = 0
    cntNoHyphen = 0
    
    print("Starte mit dem suchen der Reparaturnummern rxRepNr()")
    matchResult = ""
    for line in srcLst:
        lineEl = str(line[idx])
        match = re.findall(r"[MSms]""\d{3}"" ?" "-?"" ?""\d{5,6}", lineEl)
        if lineEl is not None :
            cntLelNotNone +=1
            if match:
                cntMatch +=1
                matchResult = match[0].replace(" ", "") # Löscht alle Freizeichen im Result
                #Ab hier wird der fehlende Bindestrich eingefügt
                if matchResult.find("-")== -1 :          # Wenn kein Bindestrich vorhanden ist
                    cntNoHyphen += 1
                    matchResult = list(matchResult)      # mache aus dem Element eine Liste
                    matchResult.insert(4,"-")            # füge an Index 4 einen Bindestrich ein
                    matchResult = ''.join(matchResult)   # füge die einzelnen Listenelement wieder zu einem String zusammen
                    matchResult = matchResult.capitalize()
            else:
                cntNoMatch += 1
                matchResult = "1_Nichts gefunden"
        else:
            matchResult = "1_Suchspalte Leer"
        matchResult = matchResult.capitalize()   # Macht den Anfangsbuchstaben immer Groß unabhängig davon ob er vorher schon Groß war
        line.insert(0, matchResult)              # füge das neu zusammengebaute Element an Index 0 ein 
    srcLst[0][0] = "Suchergebnis"            # Ändere die Spaltenbezeichnung des Index 0
    # Die folgenden Zeilen sind nur für die Konsolenausgabe
    difCnt = cntSrcLst - (cntMatch + cntNoMatch)
    cntResult = "Alle Zeilen ausgewertet" if cntMatch + cntNoMatch == cntSrcLst else Fore.RED+"{} Zeilen wurden nicht ausgewertet".format(difCnt)
    print(Fore.GREEN + "Vergleich der Reparaturnummern abgeschlossen :")
    print("Lines SrcLst: {}\nLines not None: {}\nMatches: {}\nNo Hyphen {}\nNo Match: {}".format(cntSrcLst,cntLelNotNone, cntMatch,cntNoHyphen ,cntNoMatch))
    print(Fore.GREEN+"{}\n".format(cntResult))
                
                
       
 