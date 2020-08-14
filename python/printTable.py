#! /usr/bin/env python3
#project printTable

tableData=[['apples','oranges','cherries','bananas'],
           ['Alice','Bob','Carol','David'],
           ['dogs','cats','moose','goose']]


def printTable(table):
    colwidth=[0]*len(tableData)
    for a in range(len(table)):
        for i in table[a]:
            if colwidth[a]<len(i):
                colwidth[a]=len(i)
    for j in range(4):
        for a in range(len(table)):
            print(table[a][j].rjust(colwidth[a]+1),end='')
        print()

printTable(tableData)
    
