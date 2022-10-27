
#  Fügt in eine gegebene Liste eine Spalte ein | Schreibt die Überschrift in die Spalte | Kopiert dann die erste Zeile
#  in die zukünftige Resultliste
def srcListExcelInsertColumn(list, resultList): 
    for el in list:
        el.insert(0, "-") # fügt eine erste Spalte ein und belegt diese mit "-"
    list[0][0]="Suchergebnis" # schreibt die Spaltenüberschrift für die erste Spalte
    resultList.append(list[0])

# Bearbeitet den Match Value | löscht die Zeile mit dem Match aus der srcList | Fügt die Zeile mit dem Match
# in die Resultlist ein. So wird die srcList immer kürzer & Result immer länger
# Argumente: matchValue - der mit Regex ermittelte Wert | line - die Zeile in der der Wert steht
def workWithMatch(matchValue, line, srcLst, resLst):
    matchValue = matchValue.capitalize() # Macht den Anfangsbuchstaben immer Groß unabhängig davon ob er vorher schon Groß war
    line[0]=matchValue
    resLst.append(line)
    srcLst.remove(line)


# druckt die Länge der beiden Listen aus. - Erfolgskontrolle 
def printLen(srcLst, resLst):
    src = len(srcLst)
    res = len(resLst)
    print("Länge der SrcLst = {}".format(src))
    print("Länge der resLst = {}\n".format(res))
