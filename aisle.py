#!/usr/bin/env python3
import math, string


def aisle_count(aisleName):
    invalidChars = set(string.punctuation.replace("_", ""))
    while True:
        
        input_total = input(f"How many cases are on the aisle {aisleName}?: ")
        
        try:
            val = int(input_total)
            #print("Input is an integer number.")
            print("Input number is: ", val)
            return val
        except ValueError:
            try:
                float(input_total)
                #print("Input is an float number.")
                print("Input number is: ", val)
                return val
            except ValueError:
                print("This is not a number. Please enter a valid number")

        #if input_total == "": 
        #    print("No input given")
        #elif str.isdigit(input_total):
            #print("Give a number")
        #elif any(char in invalidChars for char in input_total):
        #    print("No special characters")
        #else:
            #input_total = float(input_total)
        #    return input_total
def change_count():
    print("=-=-=-=- Aisles -=-=-=-=-=")
    print("1) Aisle 17")
    print("2) Aisle 16")
    change_aisle = input("What aisle do you want to change?: ")

    if change_aisle == "1":
        aisle_count("17")
    elif change_aisle == "2":
        aisle_count("16")
    else:
        print("Not a option")
        
    



