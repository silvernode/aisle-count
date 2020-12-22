#!/usr/bin/env python3
import math, string, time

keepGoing = True


class aisle:
    def __init__(self, name, cases):
        self.name = name
        self.cases = cases

    

def check_number(message):
#invalidChars = set(string.punctuation.replace("_", ""))
    while keepGoing == True:

        enter_number = input(message)

        try:
            cases = int(enter_number)
            #print("Input is an integer number.")
            #print("Input number is: ", val)
            return cases
        except ValueError:
            try:
                cases = float(enter_number)
                #print("Input is an float number.")
                #print("Input number is: ", val)
                return cases
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

a17 = aisle("17", 0)
a16 = aisle("16", 0)
a15 = aisle("15", 0)
a14 = aisle("14", 0)
a13 = aisle("13", 0)
a12 = aisle("12", 0)
a9 = aisle("9", 0)
a8 = aisle("8", 0)
a7 = aisle("7", 0)
a6 = aisle("6", 0)

def count_all():
    
    timestr = time.strftime("%Y%m%d-%H%M%S")
    fileName = f"aisle-check_number-{timestr}.txt"
    file = open(fileName, 'w+')

    
    a17.cases = check_number("Total cases for aisle 17: ")
    file.write(f"17 = {a17.cases}\n")

    a16.cases = check_number(f"Total cases for aisle 16: ")
    file.write(f"16 = {a16.cases}\n")

    a15.cases = check_number("Total cases for aisle 15:")
    file.write(f"15 = {a15.cases}\n")

    a14.cases = check_number("Total cases for aisle 14: ")
    file.write(f"14 = {a14.cases}\n")

    a13.cases = check_number("Total cases for aisle 13: ")
    file.write(f"13 = {a13.cases}\n")

    a12.cases = check_number("Total cases for aisle 12: ")
    file.write(f"12 = {a12.cases}\n")

    a9.cases = check_number("Total cases for aisle 9: ")
    file.write(f"9 = {a9.cases}\n")

    a8.cases = check_number("Total cases for aisle 8: ")
    file.write(f"8 = {a8.cases}\n")

    a7.cases = check_number("Total cases for aisle 7: ")
    file.write(f"7 = {a7.cases}\n")

    a6.cases = check_number("Total cases for aisle 6: ")
    file.write(f"6 = {a6.cases}\n")

    

    loadTotal = a17.cases + a16.cases + a15.cases + a14.cases + a13.cases + a12.cases + a9.cases + a8.cases + a7.cases + a6.cases
    file.write(f"Total = {loadTotal}\n")

    file.close()

    return loadTotal

def div_ppl():
    #aisleTrack = aisle("0", 0)
    ppl = check_number("How many people are working?: ")

    return ppl


while keepGoing == True:
    print()
    print("1) Start check_number")
    print()
    choice = input("Choose option: ")

    if choice == "1":
        totalCases = count_all()
        print("Total cases: ", totalCases)
        pplDiv = div_ppl() / totalCases
        print(pplDiv)
        
    elif choice == "q":
        keepGoing = False
    else:
        print(f"{choice} is not an option")