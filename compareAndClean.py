

#Vergleicht Liste 1 mit Liste 2
def cmpLst(list0, list1, dstLst):
    print("Vergleich der beiden Listen beginnt")
    for el in list0:
        for elm in list1:
            if(el==elm):
                dstLst.append(el)
                print(el)
    print("Zielliste enthält {} Einträge".format(len(dstLst)))
    
# säubern der ursprünglichen Liste 
def cleanList(dstLst, list0):
    for el in dstLst:
        list0.remove(el)
    print("List0 enthält {} Datensätze".format(len(list0)))