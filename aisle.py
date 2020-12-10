#!/usr/bin/env python3
import math


def aisle_count(aisleName):
    #aisleTotal = 0
    while True:
        
        input_total = input(f"How many cases are on the aisle {aisleName}?: ").strip()

        if input_total == "":
            print("No input given")
        else:
            print(input_total)
            return input_total
        
        
    



aisle_count("17")