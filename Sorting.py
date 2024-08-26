def sortIntoAlphabetFile():
    f=open('dataScraped.txt', 'r')

    fA=open('scrapedData/A_name.txt', 'a')
    fB=open('scrapedData/B_name.txt', 'a')
    fC=open('scrapedData/C_name.txt', 'a')
    fD=open('scrapedData/D_name.txt', 'a')
    fE=open('scrapedData/E_name.txt', 'a')
    fF=open('scrapedData/F_name.txt', 'a')
    fG=open('scrapedData/G_name.txt', 'a')
    fH=open('scrapedData/H_name.txt', 'a')
    fI=open('scrapedData/I_name.txt', 'a')
    fJ=open('scrapedData/J_name.txt', 'a')
    fK=open('scrapedData/K_name.txt', 'a')
    fL=open('scrapedData/L_name.txt', 'a')
    fM=open('scrapedData/M_name.txt', 'a')
    fN=open('scrapedData/N_name.txt', 'a')
    fO=open('scrapedData/O_name.txt', 'a')
    fP=open('scrapedData/P_name.txt', 'a')
    fQ=open('scrapedData/Q_name.txt', 'a')
    fR=open('scrapedData/R_name.txt', 'a')
    fS=open('scrapedData/S_name.txt', 'a')
    fT=open('scrapedData/T_name.txt', 'a')
    fU=open('scrapedData/U_name.txt', 'a')
    fV=open('scrapedData/V_name.txt', 'a')
    fW=open('scrapedData/W_name.txt', 'a')
    fX=open('scrapedData/X_name.txt', 'a')
    fY=open('scrapedData/Y_name.txt', 'a')
    fZ=open('scrapedData/Z_name.txt', 'a')
    fMisc=open('scrapedData/Misc_name.txt', 'a')

    alphabet=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for line in f.readlines(): 
        if (len(line)<5):
            continue
        line=line.lower()
        if line[5] == "a":
            fA.write(line)
        elif line[5] == "b":
            fB.write(line)
        elif line[5] == "c":
            fC.write(line)
        elif line[5] == "d":
            fD.write(line)
        elif line[5] == "e":
            fE.write(line)
        elif line[5] == "f":
            fF.write(line)
        elif line[5] == "g":
            fG.write(line)
        elif line[5] == "h":
            fH.write(line)
        elif line[5] == "i":
            fI.write(line)
        elif line[5] == "j":
            fJ.write(line)
        elif line[5] == "k":
            fK.write(line)
        elif line[5] == "l":
            fL.write(line)
        elif line[5] == "m":
            fM.write(line)
        elif line[5] == "n":
            fN.write(line)
        elif line[5] == "o":
            fO.write(line)
        elif line[5] == "p":
            fP.write(line)
        elif line[5] == "q":
            fQ.write(line)
        elif line[5] == "r":
            fR.write(line)
        elif line[5] == "s":
            fS.write(line)
        elif line[5] == "t":
            fT.write(line)
        elif line[5] == "u":
            fU.write(line)
        elif line[5] == "v":
            fV.write(line)
        elif line[5] == "w":
            fW.write(line)
        elif line[5] == "x":
            fX.write(line)
        elif line[5] == "y":
            fY.write(line)
        elif line[5] == "z":
            fZ.write(line)
        else:
            fMisc.write(line)
#sortIntoAlphabetFile()

def sortFile(fileName):
    f=open(fileName, "r")
    sortArray=[]
    for line in f.readlines():
        sortArray.append(line)
    f.close()
    f=open(fileName, "w")
    sortArray.sort()
    #f2=open("sortedDataScraped.txt", "a")
    for i in sortArray:
        f.write(i)
    f.close()

#sortFile("scrapedData/Z_name.txt")

def sortIntoSQLFormat():
    f=open('test.txt', 'r')
    f2=open('test3.txt', 'a')
    for line in f.readlines():
        newline=line.replace("name:", "#")
        newline=newline.replace("|school:", "#")
        newline=newline.replace("|url:", "#")
        f2.write(newline)
    f.close()
    f2.close()
sortIntoSQLFormat()