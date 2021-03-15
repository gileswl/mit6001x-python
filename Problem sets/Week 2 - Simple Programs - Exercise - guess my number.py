# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 14:26:39 2019

This script is for 
MITx: 6.00.1x Introduction to Computer Science and Programming Using Python 

Course Week 2: Simple Programs: Exercise: guess my number

@author: giles
"""

print("Please think of an integer between 0 and 100!")

high = 100
low = 0

while True:
    guess = int((high+low)/2)
    print("Is your secret number ", guess, "?")
    reply = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    
    if reply == str("h"):
        high = guess
    elif reply == str("l"):
        low = guess
    elif reply == str("c"):
        print("Game over. Your secret number was:", guess)
        break
    else:
        print("Sorry, I didn't understand that!")