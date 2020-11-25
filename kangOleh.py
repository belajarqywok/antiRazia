#!/bin/env python3
import os
import sys
import hashlib
os.system("clear")
chrLow=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
chrUpr=[]
number=[]
symbol=['`','~','!','@','#','$','%','&','^','*','(',')','-','_','=','+','?',',','<','>','.',';',':','"',"'",'{','}','[',']']
for Case in range(len(chrLow)):
    chrUpr.append(chrLow[Case].upper())
for num in range(10):
    number.append(str(num))
kamus=[chrLow,chrUpr,number,symbol]
for indexKamus in range(len(kamus)):
    kamus[indexKamus].reverse()
plainText=str(sys.argv[1])
extRev=[]
nameFile=[]
def key(text):
    formatReversed=[]
    formatVideo=['.mp4','.3gp','.avi','.swf','.raw','.mkv','.abc']
    for indexFormatVideo in range(len(formatVideo)):
        if text[len(text)-4:len(text)]==formatVideo[indexFormatVideo]:
            indexFormat=formatVideo[indexFormatVideo]
            for indRev in range(len(indexFormat)):
                if indRev%2==0:
                    formatReversed.append(indexFormat[indRev].upper())
                else:
                    formatReversed.append(indexFormat[indRev].lower())
    formatReversed.reverse()
    for inxExtRev in range(len(formatReversed)):
        extRev.append(formatReversed[inxExtRev])
key(plainText)
def cipherText(text2):
    fileReversed=[]
    for indexTimeRev in range(len(text2)-4):
        if indexTimeRev%2==0:
            fileReversed.append(text2[indexTimeRev:indexTimeRev+1].lower())
        else:
            fileReversed.append(text2[indexTimeRev:indexTimeRev+1].upper())
    fileReversed.reverse()
    for indexNameFile in range(len(fileReversed)):
        nameFile.append(fileReversed[indexNameFile])
cipherText(plainText)
resExtRev=extRev[0]
resNameFile=nameFile[0]
for indexResExtRev in range(len(extRev)-1):
    resExtRev=resExtRev+extRev[indexResExtRev+1]
for indexCipher in range(len(nameFile)-1):
    resNameFile=resNameFile+nameFile[indexCipher+1]
def acak(res1,res2):
    kamusAlphaLower=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    kamusAlphaUpper=[]
    kamusAngka=[]
    kamusSymbol=['`','~','!','@','#','$','%','&','^','*','(',')','-','_','=','+','?',',','<','>','.',';',':','"',"'",'{','}','[',']']
    for indexUpper in range(len(chrLow)):
        kamusAlphaUpper.append(kamusAlphaLower[indexUpper].upper())
    for angka in range(10):
        kamusAngka.append(str(angka))
    kunciArr=[]
    cipherArr=[]
    def acakKunci(acak1):
        for indexLowerAlpha in range(len(acak1)):
            for alphaLowerIndex in range(len(kamusAlphaLower)):
                if acak1[indexLowerAlpha]==kamusAlphaLower[alphaLowerIndex]:
                    kunciArr.append(chrLow[alphaLowerIndex])
            for angkaKamusIndex in range(len(kamusAngka)):
                if acak1[indexLowerAlpha]==kamusAngka[angkaKamusIndex]:
                    kunciArr.append(number[angkaKamusIndex])
            for alphaUpperIndex in range(len(kamusAlphaUpper)):
                if acak1[indexLowerAlpha]==kamusAlphaUpper[alphaUpperIndex]:
                    kunciArr.append(chrUpr[alphaUpperIndex])
            for symbolIndex in range(len(kamusSymbol)):
                if acak1[indexLowerAlpha]==kamusSymbol[symbolIndex]:
                    kunciArr.append(symbol[symbolIndex])
    acakKunci(res1)
    def acakKunci1(acak2):
        for indexLowerAlpha1 in range(len(acak2)):
            for alphaLowerIndex1 in range(len(kamusAlphaLower)):
                if acak2[indexLowerAlpha1]==kamusAlphaLower[alphaLowerIndex1]:
                    cipherArr.append(chrLow[alphaLowerIndex1])
            for angkaKamusIndex1 in range(len(kamusAngka)):
                if acak2[indexLowerAlpha1]==kamusAngka[angkaKamusIndex1]:
                    cipherArr.append(number[angkaKamusIndex1])
            for alphaUpperIndex1 in range(len(kamusAlphaUpper)):
                if acak2[indexLowerAlpha1]==kamusAlphaUpper[alphaUpperIndex1]:
                    cipherArr.append(chrUpr[alphaUpperIndex1])
            for symbolIndex1 in range(len(kamusSymbol)):
                if acak2[indexLowerAlpha1]==kamusSymbol[symbolIndex1]:
                    cipherArr.append(symbol[symbolIndex1])
    acakKunci1(res2)
    resKunciArr=kunciArr[0]
    resCipherArr=cipherArr[0]
    for indexKunciArr in range(len(kunciArr)-1):
        resKunciArr+=kunciArr[indexKunciArr+1]
    for indexCipherArr in range(len(cipherArr)-1):
        resCipherArr+=cipherArr[indexCipherArr+1]
    resultArr=[resKunciArr,resCipherArr]
    result=resultArr[0]
    for resIndex in range(len(resultArr)-1):
        result=result+resultArr[resIndex+1]
    os.system('mv '+plainText+" "+result+".bin")
    print("nama file : "+plainText)
    print("="*30)
    print("hasil enkripsi : "+result)
acak(resExtRev,resNameFile)