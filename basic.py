import os


# Definiert die Basisvariablen

valList = []
valSet = ()
val=[]
lstDbl = []
counter = {}

# Verzeichnisse
workDir = os.getcwd()           
srcFld=workDir + "\\src\\"    
srcFile = srcFld + os.listdir(srcFld)[0] 
dstFile= workDir + "\\dst\\dstFile.xlsx" 
