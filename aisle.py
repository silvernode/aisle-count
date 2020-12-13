#!/usr/bin/env python3
import math, string


def aisle_count(aisleName):
    #invalidChars = set(string.punctuation.replace("_", ""))
    while True:
        
        input_total = input(f"How many cases are on the aisle {aisleName}?: ")
        
        try:
            val = int(input_total)
            #print("Input is an integer number.")
            #print("Input number is: ", val)
            return val
        except ValueError:
            try:
                float(input_total)
                #print("Input is an float number.")
                #print("Input number is: ", val)
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
    file = open('asile-count-12-12-2020.txt', 'w+')

    a17 = aisle_count("17")
    file.write(f"17 = {a17}\n")

    a16 = aisle_count("16")
    file.write(f"16 = {a16}\n")

    a15 = aisle_count("15")
    file.write(f"15 = {a15}\n")

    a14 = aisle_count("14")
    file.write(f"14 = {a14}\n")

    a13 = aisle_count("13")
    file.write(f"13 = {a13}\n")

    a12 = aisle_count("12")
    file.write(f"12 = {a12}\n")

    a9 = aisle_count("9")
    file.write(f"9 = {a9}\n")

    a8 = aisle_count("8")
    file.write(f"8 = {a8}\n")

    a7 = aisle_count("7")
    file.write(f"7 = {a7}\n")

    a6 = aisle_count("6")
    file.write(f"6 = {a6}\n")

    

    loadTotal = a17 + a16 + a15 + a14 + a13 + a12 + a9 + a8 + a7 + a6
    file.write(f"Total = {loadTotal}\n")

    file.close()

    return loadTotal



while True:
    print()
    print("1) Start Count")
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