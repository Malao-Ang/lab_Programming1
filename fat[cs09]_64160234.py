# -*- coding: utf-8 -*-
"""Fat[cs09]_64160234.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19Derv_qg92zCUAVsRaYocBv7UBsHLso5
"""

sex = int(input())
weight = int(input())
if sex == 1:
  if weight > 20:
    print('FAT')
  else:
    print('OK')
else:
  if weight > 15:
    print('FAT')
  else:
    print('OK')