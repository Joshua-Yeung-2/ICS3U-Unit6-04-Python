# !/usr/bin/env python3

# Created by Joshua Yeung
# Created on October 2021
# This program is to test 2D array

import random


def average(array):
    # this function is to calculate the average of the random number
    average_number = 0
    for row_value in array:
        for columns_value in row_value:
            average_number = average_number + columns_value
    average_number = average_number / (len(array) * len(array[0]))
    
    return average_number
    

def main():
    # this function is to test 2D array
    array = []
    # input
    rows = input("How many row would you like: ")
    columns = input("How many columns would you like: ")
    print("")

    try:
        rows_int = int(rows)
        columns_int = int(columns)
        for loop_counter_rows in range(0, rows_int):
            temp_column = []
            for loop_counter_columns in range(0, columns_int):
                random_number = random.randint(0,10)
                temp_column.append(random_number)
                print("{0} ".format(random_number), end="")
            array.append(temp_column)
            print("")
        average_2 = average(array)
        print("")
        print("The average of all the numbers is: {0} ".format(average_2))
    except Exception:
        print("sorry, this is not a valid number")
        print("please try again")


if __name__ == "__main__":
    main()