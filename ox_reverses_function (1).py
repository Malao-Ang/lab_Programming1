# -*- coding: utf-8 -*-
"""OX Reverses Function.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NfP1hi2gaR1jxlOy0H0_bS5EfpGQTczs
"""

def String_Input(Row,Column):
  tic = [[0 for j in range(Column)] for i in range(Row)]
  for i in range(Row):
    for j in range(Column):
      tic[i][j] = input().strip()
  return tic
  
def  String_Show(tic,Row,Column):
  print('Normal')
  for i in range(Row):
    for j in range(Column):
      print(tic[i][j],end=' ')
    print()

def String_Check(tic,Row,Column):
  print('Reverses')
  for i in range(Row):
    for j in range(Column):
      if tic[i][j] =='x':
        tic[i][j] ='o'
      else:
        tic[i][j] ='x'
      print(tic[i][j],end=' ')
    print()

#main program
Row = int(input())
Column =int(input())
tic=String_Input(Row,Column)
String_Show(tic,Row,Column)
String_Check(tic,Row,Column)