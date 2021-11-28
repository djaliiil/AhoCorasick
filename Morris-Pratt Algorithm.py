from os import *
from sys import *
from time import *

#>>>>>>> Algorithme de Recherche Naive
def recherche_naive(texte, mot):
    n = len(texte)
    m = len(mot)
    mot.append('')
    i = 0
    result = []

    while (i < (n-m+1)):
        j = 0
        while (j < m) & (texte[i + j] == mot[j]):
            j = j+1
        if(j==m):
            result.append(i)
        i = i+1

    mot.pop(len(mot)-1)
    return result


#>>>>>>> Table de bords / Knuth-Morris-Pratt ------
def kmp_table_bords(mot):
    m = len(mot)
    bords = [-1]
    bords.extend([0]*m)
    mot.append('')
    i = -1

    for j in range(m):
        while ((i >= 0) & (mot[i] != mot[j])):
            i = bords[i]

        i = i+1

        if((i == (m-1)) | (mot[j+1] != mot[i])):
            bords[j+1] = i
        else:
            bords[j+1] = bords[i]

    print(">>>>> Bords : " , bords)
    mot.pop(len(mot)-1)
    return bords

#>>>>>>> Table de bords ------
def table_bords(mot, m, bords): 
	j = 0

	bords[0]
	i = 1

	while i < m: 
		if mot[i]== mot[j]: 
			j += 1
			bords[i] = j
			i += 1
		else: 
			if j != 0: 
				j = bords[j-1] 
				
			else: 
				bords[i] = 0
				i += 1


#>>>>>>>> Algorithme de recherche
def algorithm1(texte, mot):
    i = 0
    j = 0
    m = len(mot)
    n = len(texte)
    result = []
    bords = [0]*m
    table_bords(mot, m, bords)

    while i < n:
        if mot[j] == texte[i]:
            i += 1
            j += 1

        if j == m:
            result.append(i-j)
            j = bords[j-1] 

        elif i < n and mot[j] != texte[i]: 
            if j != 0:
                j = bords[j-1]
            else:
                i += 1

    return result

def algorithm4(texte, mot, bords):
    i = 0
    j = 0
    m = len(mot)
    n = len(texte)
    result = []
    

    while ((i < n-m+1) & (j < m)):
        if ((j >= 0) & (texte[i] != mot[j])):
            j = bords[j]
        else:
            i = i+1
            j = j+1

    if (j == m):
        return (i-m)
    else:
        return -1

#>>>>>>>> Algorithme de recherche version 2
def algorithm2(texte, mot, bords):
    i = 0
    j = 0
    m = len(mot)
    n = len(texte)
    result = []

    while i < n:
        if mot[j] == texte[i]:
            i += 1
            j += 1

        if j == m:
            result.append(i-j)
            j = bords[j-1] 

        elif i < n and mot[j] != texte[i]: 
            if j != 0:
                j = bords[j-1]
            else:
                i += 1

    return result

# >>>>>>> Fonction prefixe
def prefixe(s):
    pref = []
    for i in range(len(s)):
        pref.append(s[0:i])
    return pref

# >>>>>>> Plus long prefixe
def plus_long_prefixe(s1, s2):
    pref = []
    for i in range(min(len(s1), len(s2))):
        if(s1[0:i] == s2[0:i]):
            pref.append(s1[0:i])
    return pref[len(pref)-1]

# >>>>>>> Fonction suffixe
def suffixe(s):
    suff = []
    for i in range(len(s)):
        suff.append(s[len(s)-1:i])
    return suff

# >>>>>>> Plus long suffixe
def plus_long_suffixe(s1, s2):
    suff = []
    i = len(s1)-1
    j = len(s2)-1
    while ((i>=0 & j>=0) & (s1[i:len(s1)] == s2[j:len(s2)])):
        suff.append(s1[i:len(s1)])
        j = j - 1
        i = i - 1
    return suff[len(suff)-1]
#   aaabbababbaaaba    bbaa
#   ctactatatatc    tata


def myhash(t):
    motif = {'a':1, 'c':2, 'g':3, 't': 4}
    key = 0
    for i in range(len(t)):
        c = t[i]
        p = int(motif[c]) * 4**(len(t)-1-i)
        key = key + p

    return key


def Rabin_Karp(texte, mot):
    n = len(texte)
    m = len(mot)
    hm = myhash(mot)
    ht = myhash(texte[0:m])
    result = []

    for i in range(n-m+1):
        if(hm == ht):
            if(mot[0:m] == texte[i-1:i+m-1]):
                result.append(i-1)
        if(i < (n-m+1)):
            ht = myhash(texte[i:i+m])
        
    return result


def myhashG(t):
    motif = {'a':1, 'b':2, 'c':3, 'd': 4, 'e':5, 'f':6, 'g':7, 'h': 8,
             'i':9, 'j':10, 'k':11, 'l': 12, 'm':13, 'n':14, 'o':15, 'p': 16,
             'q':17, 'r':18, 's':19, 't': 20, 'u':21, 'v':22, 'w':23, 'x': 24,
             'y':25, 'z':26}
    key = 0
    for i in range(len(t)):
        c = t[i]
        p = int(motif[c]) * 26**(len(t)-1-i)
        key = key + p

    return key

def Rabin_Karp_Generale(Texte, mot):
    n = len(texte)
    m = len(mot)
    hm = myhashG(mot)
    ht = myhashG(texte[0:m])
    result = []

    for i in range(n - m + 1):
        if (hm == ht):
            if (mot[0:m] == texte[i :i + m]):
                result.append(i)
        if (i+1 < (n - m + 1)):
            ht = myhashG(texte[i+1: i + m+1])
    
    return result





if __name__ == '__main__':

    rep = True

    while(rep):

        print("---------------- Menu ----------------")
        print("1) -> exercice 1 - Préfixe/Préfixe_Commun_Plus_Long")
        print("2) -> exercice 2 - Suffixe/Sufixe_Commun_Plus_Long")
        print("3) -> Algorithme de recherche - Recherche Naïve")
        print("4) -> Table de bords - Morris_Pratt_Algorithm")
        print("5) -> Morris_Pratt_Algorithm")
        print("6) -> Table de bords - Knuth_Morris_Pratt_Algorithm")
        print("7) -> Knuth_Morris_Pratt_Algorithm")
        print("*) -> Algorithme de recherche - Rabin-Karp Algorithm")
        print("   |-> 8) -> Rabin-Karp Algorithm V-ADN { 'A' , 'C' , 'G' , 'T' }")
        print("   |-> 9) -> Rabin-Karp Algorithm V-GENERALE {A..Z}")

        choix = int(input("Votre choix : "))

        if (choix == 1):
            print("Veuillez introduire le 1er mot !")
            mot1 = str(input("Mot1 : "))
            print("Veuillez introduire le 2eme mot !")
            mot2 = str(input("Mot2 : "))
            print("Les préfixe du mot : \'", mot1, "\' sont : ", prefixe(mot1))
            print("Les préfixe du mot : \'", mot2, "\' sont : ", prefixe(mot2))
            pref = plus_long_prefixe(mot1, mot2)
            print("Le préfixe commun le plus long des mots : \'", "".join(map(str, mot1)) , "\' & \'", "".join(map(str, mot2)) , "\' : ", "".join(map(str, pref)))

        if (choix == 2):
            print("Veuillez introduire le 1er mot !")
            mot1 = str(input("Mot1 : "))
            print("Veuillez introduire le 2eme mot !")
            mot2 = str(input("Mot2 : "))
            print("Les préfixe du mot : \'", mot1, "\' sont : ", suffixe(mot1))
            print("Les préfixe du mot : \'", mot2, "\' sont : ", suffixe(mot2))
            suff = plus_long_suffixe(mot1, mot2)
            print("Le préfixe commun le plus long des mots : \'", "".join(map(str, mot1)) , "\' & \'", "".join(map(str, mot2)) , "\' : ", "".join(map(str, suff)))

        if (choix == 3):
            print("Veuillez introduire le texte !")
            texte = str(input("texte : "))
            print("Veuillez introduire un motif !")
            mot = list(input("mot : "))
            tmp1 = clock()
            pos = recherche_naive(texte, mot)
            tmp2 = clock()
            if (pos == []):
                print("Le motif n\'est pas trouvé")
            else:
                print("Le motif \'", "".join(map(str, mot)) ,"\' est trouvé à la position ", pos)

            print("Le temps d\'éxecution est : %s Sec" %(tmp2-tmp1))

        if (choix == 4):
            print("Veuillez introduire un motif !")
            mot = list(input("mot : "))
            tmp1 = clock()
            """
            bords = table_bords(mot)
            tmp2 = clock()
            print("La table de bords du mot \'", "".join(map(str, mot)) ,"\' est : ", bords)
            print("Le temps d\'éxecution est : %s Sec" % (tmp2 - tmp1))
            """
        if (choix == 5):
            print("Veuillez introduire le texte !")
            texte = str(input("texte : "))
            print("Veuillez introduire un motif !")
            mot = list(input("mot : "))
            tmp1 = clock()
            #bords = table_bords(mot)
            tmp2 = clock()
            pos = algorithm1(texte, mot)
            tmp3 = clock()
            if (pos == []):
                print("Le motif n\'est pas trouvé")
            else:
                print("Le motif \'", "".join(map(str, mot)) ,"\' est trouvé à la position ", pos)

            print("Le temps d\'éxecution est : ")
            print(" > Bords : %s Sec" %(tmp2-tmp1))
            print(" > Algo-V1 : %s Sec" %(tmp3-tmp2))
            print(" > Total : %s Sec " % (tmp3-tmp1) ," <")

        if (choix == 6):
            print("Veuillez introduire un motif !")
            mot = list(input("mot : "))
            tmp1 = clock()
            bords = kmp_table_bords(mot)
            tmp2 = clock()
            print("La table de bords du mot \'", "".join(map(str, mot)) ,"\' est : ", bords)
            print("Le temps d\'éxecution est : %s Sec" % (tmp2 - tmp1))

        if (choix == 7):
            print("Veuillez introduire le texte !")
            texte = str(input("texte : "))
            print("Veuillez introduire un motif !")
            mot = list(input("mot : "))
            tmp1 = clock()
            bords = kmp_table_bords(mot)
            tmp2 = clock()
            pos = algorithm2(texte, mot, bords)
            tmp3 = clock()
            if (pos == -1):
                print("Le motif n\'est pas trouvé")
            else:
                print("Le motif \'", "".join(map(str, mot)) ,"\' est trouvé à la position ", pos)

            print("Le temps d\'éxecution est : ")
            print(" > Bords : %s Sec" %(tmp2-tmp1))
            print(" > Algo-V2 : %s Sec" %(tmp3-tmp2))
            print(" > Total : %s Sec " % (tmp3-tmp1) ," <")


        if (choix == 8):
            print("Veuillez introduire le texte !")
            texte = str(input("texte : "))
            print("Veuillez introduire un motif !")
            mot = str(input("mot : "))
            tmp1 = clock()
            pos = Rabin_Karp(texte, mot)
            tmp2 = clock()
            if (pos == -1):
                print("Le motif n\'est pas trouvé")
            else:
                print("Le motif \'", "".join(map(str, mot)), "\' est trouvé à la position ", pos)

            print("Le temps d\'éxecution est : %s Sec" % (tmp2 - tmp1))

        if (choix == 9):
            print("Veuillez introduire le texte !")
            texte = str(input("texte : "))
            print("Veuillez introduire un motif !")
            mot = str(input("mot : "))
            tmp1 = clock()
            pos = Rabin_Karp_Generale(texte, mot)
            tmp2 = clock()
            if (pos == []):
                print("Le motif n\'est pas trouvé")
            else:
                print("Le motif \'", "".join(map(str, mot)), "\' est trouvé à la position ", pos)

            print("Le temps d\'éxecution est : %s Sec" % (tmp2 - tmp1))

        a = input("Veuillez vous continuer ? [o/n]")
        if(a == 'o'):
            rep = True
        elif (a == 'n'):
            rep = False
