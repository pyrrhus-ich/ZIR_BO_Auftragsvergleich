import os

from colorama import *
init(autoreset=True)

"""
print("Ist das Source File geöffnet. Wenn nicht, bitte jetzt öffnen - Danach mit Enter bestätigen  \n" , end='')
launch = input()
# ANZUPASSENDE VARIABLEN <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
letzteSpalte = input("Gib den Buchstaben der letzten beschriebenen Spalte ein >>>  \n").lower() # letzte befüllte Spalte 
suchSpalte = input(" Gib den Buchstaben der Spalte ein, die die zu suchenden Werte enthält >>>  \n" ).lower()# Spalte in der nach der Reparaturnummer gesucht werden soll.
sapSpalte = input("Gib den Buchstaben der Spalte ein, die die SAP Nr. enthält >>> \n ").lower()
"""

letzteSpalte = "d"
suchSpalte = "d"
sapSpalte = "b"


# <<<<<<< Feste Variablen - Werden nicht geändert >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
srcFile = os.getcwd()+"\\src\\srcFile_WWS.xlsx"    # Definiert das Excel file das gelesen werden soll
dstFile = os.getcwd()+"\\dst\\dstFile_WWS.xlsx"    # Definiert das Excel file das geschrieben werden soll
srcLstExcel = []                                   # In diese Liste schreibt readSrc() die ausgelesenen Daten
resultList = []                                    # enthält die Elemente mit einem Match
idx = ord(suchSpalte) - 96                # idx legt den Index fest der bearbeitet werden soll
maxColumn = ord(letzteSpalte) - 96             # maxColumn legt fest, bis zu welcher Spalte das File ausgelesen wird
sapNridx = ord(sapSpalte) - 96



