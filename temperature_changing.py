# -*- coding: utf-8 -*-
"""Temperature Changing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sNcPpe4axkG_-KWNLKN2_wKwuCJJ14YI
"""

import math
def cf ():
  C = float(input())
  F = (9/5*C)+32
  print(round(F,2))
  return C
def fc ():
  F = float(input())
  C = (5/9)*(F-32)
  print(round(C,2))
  return F
#main
num = int(input())
if num == 1:
  cf()
elif num == 2:
  fc()