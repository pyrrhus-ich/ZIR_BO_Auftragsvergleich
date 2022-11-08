import re
from colorama import *
init(autoreset=True)
from .HifsScripte import hs_workWithMatch


 
# sucht nach dem Muster Mxxx-xxxxxx
def searchSR(srcLst, idx, resultList):
    print("Starte mit dem suchen der Reparaturnummern searchSR()")
    for line in srcLst:
        match = re.findall(r"[MSms]""\d{3}""-""\d{5,6}", line[idx])
        if match:
            match = match[0]
            hs_workWithMatch(match, line, srcLst, resultList)

# sucht nach dem Muster xxx-xxxxxx           
def searchSRohneBuchstaben(srcLst, idx,resultList, sapIdx):
    print("Starte mit dem suchen der Reparaturnummern searchSRohneBuchstaben()")
    for line in srcLst:
        match = re.findall(r"\d{3}""-""\d{5,6}", line[idx])
        if match:
            match = match[0]
            first3Match = match[0:3]
            sapNr = line[sapIdx][1:4]
            if first3Match == sapNr:
                match=line[sapIdx][:1]+ match
                hs_workWithMatch(match, line, srcLst, resultList)
                








   
               
 