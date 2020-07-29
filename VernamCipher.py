#!/usr/bin/env/ python
# -*- coding: utf-8 -*-
# Author: Nolan Wang
# Implementation of Vernam Cipher


def encvernam():
    print("Please input Plaintext")
    pt = str(input()).lower().replace(" ", "")  # make the input in lower case
    print("Please input Key")
    k = str(input()).lower().replace(" ", "")
    encryption = ""
    if len(pt) != len(k):
        print("Please make sure they are the same length")
        return encvernam()
    for i in range(len(pt)):
        plaintext = ord((pt[i])) - 97  # range 0 to 25 since they are all in lower case, for a = 97
        key = ord((k[i])) - 97  # same reason
        plaintext = (plaintext + key) % 26 + 97  # instead of using if statement
        encryption += chr(plaintext)
    return encryption.lower()


def decvernam():
    print("Please input Cipher")
    c = str(input()).lower().replace(" ", "")
    print("Please input Key")
    k = str(input()).lower().replace(" ", "")
    decryption = ""
    if len(c) != len(k):
        print("Please make sure they are the same length")
        return decvernam()
    for i in range(len(c)):
        cipher = ord((c[i])) - 97
        key = ord((k[i])) - 97
        cipher = (cipher - key) % 26 + 97
        decryption += chr(cipher)
    return decryption.lower()


print("Please choose encryption(1) or decryption(0)")
flag = input()
if flag == "1":
    print("The cipher is " + encvernam())
elif flag == "0":
    print("The plaintext is " + decvernam())
