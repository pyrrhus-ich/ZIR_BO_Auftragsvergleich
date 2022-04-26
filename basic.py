import os
from tkinter import W

# Definiert die Basisvariablen


src = "Rep-Nummern.xlsx"
valList = []
valList_BO = []
valList_ZIR = []
valLstZIRInBO = []
dstFile ="MissingOr"

workDir = os.getcwd()           
srcFld=workDir + "\\srcZir\\"    
srcFile = srcFld + os.listdir(srcFld)[0]  
print(srcFile)