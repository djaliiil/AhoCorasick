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
def mp_table_bords(mot):
    m = len(mot)
    bords = [-1]
    bords.extend([0]*m)
    i = -1

    for j in range(m):
        while ((i >= 0) & (mot[i] != mot[j])):
            i = bords[i]
        i = i + 1
        bords[j + 1] = i

    print(">>>>> Bords : " , bords)
    return bords

#>>>>>>>> Algorithme de recherche
def morris_pratt_algorithm(texte, mot):
    i = 0
    j = 0
    m = len(mot)
    n = len(texte)
    result = []
    bords = mp_table_bords(mot)

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


#>>>>>>>> Algorithme de recherche version 2
def knuth_morris_pratt_algorithm(texte, mot):
    i = 0
    j = 0
    m = len(mot)
    n = len(texte)
    result = []
    bords = kmp_table_bords(mot)

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




def myhash(t):
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

def Rabin_Karp_Generale(texte, mot):
    n = len(texte)
    m = len(mot)
    hm = myhash(mot)
    ht = myhash(texte[0:m])
    result = []

    for i in range(n - m + 1):
        if (hm == ht):
            if (mot[0:m] == texte[i - 1:i + m - 1]):
                result.append(i-1)
        if (i < (n - m + 1)):
            ht = myhash(texte[i:i + m])
    
    return result
