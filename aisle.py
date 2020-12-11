#!/usr/bin/env python3
import math, string


def aisle_count(aisleName):
    #invalidChars = set(string.punctuation.replace("_", ""))
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
        
def count_all():
    a17 = aisle_count("17")
    a16 = aisle_count("16")
    a15 = aisle_count("15")
    a14 = aisle_count("14")
    a13 = aisle_count("13")
    a12 = aisle_count("12")
    a9 = aisle_count("9")
    a8 = aisle_count("8")
    a7 = aisle_count("7")
    a6 = aisle_count("6")

    loadTotal = a17 + a16 + a15 + a14 + a13 + a12 + a9 + a8 + a7 + a6

    return loadTotal



while True:
    print()
    print("1) Start Count")
    print("2) Change Count")
    print()
    choice = input("Choose option: ")

    if choice == "1":
        print("Total cases: ", count_all())

    elif choice == "2":
        change_count()
    elif choice == "q":
        quit()
    else:
        print(f"{choice} is not an option")