# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 12:42:33 2023

@author: Ardya
"""
text = input("Enter some text: \n")

text1 = text.replace("a", "4")
text2 = text1.replace("b", "8")
text3 = text2.replace("e", "3")
text4 = text3.replace("l", "1")
text5 = text4.replace("o", "0")
text6 = text5.replace("s", "5")
text7 = text6.replace("t", "7")

print(f"The text translated to leetspeak becomes :\n{text7}")