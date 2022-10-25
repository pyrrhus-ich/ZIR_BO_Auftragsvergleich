import os
from colorama import *
init(autoreset=True)


print("Ist das Source File geöffnet. Wenn nicht, bitte jetzt öffnen - Danach mit Enter bestätigen  \n" , end='')
launch = input()
# ANZUPASSENDE VARIABLEN <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
letzteSpalte = input("Gib den Buchstaben der letzten beschriebenen Spalte ein >>>  \n").lower() # letzte befüllte Spalte 
suchSpalte = input(" Gib den Buchstaben der Spalte ein, die die zu suchenden Werte enthält >>>  \n" ).lower()# Spalte in der nach der Reparaturnummer gesucht werden soll.
sapSpalte = input("Gib den Buchstaben der Spalte ein, die die SAP Nr. enthält >>> \n ").lower()

# <<<<<<< Feste Variablen - Werden nicht geändert >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
srcFile = os.getcwd()+"\\src\\srcFile.xlsx"    # Definiert das Excel file das gelesen werden soll
dstFile = os.getcwd()+"\\dst\\dstFile.xlsx"    # Definiert das Excel file das geschrieben werden soll
dstList = []                                   # In diese Liste schreibt readSrc() die ausgelesenen Daten
idx = ord(suchSpalte) - 96  - 1                # idx legt den Index fest der bearbeitet werden soll
maxColumn = ord(letzteSpalte) - 96             # maxColumn legt fest, bis zu welcher Spalte das File ausgelesen wird
sapNridx = ord(sapSpalte) - 96 - 1


