'''
Python 121 Assignment 3 Q1
Name: Haani Syed
Date: 2023-03-08
'''
import csv #imports csv file with data set
from functions3 import conversion, menu, displayInfo, uniqueDistricts, totalVotes, findMax, findMin, totalVotes, selectionSort, bubbleSort, binarySearch
#above line imports functions from functions3

def main():
    '''
    Main function allows Program to run once called.
    :return: none. Allows program to run.
    '''
    try:
        conversion() #ensures data from CSV file can be accessed by user
        menu()
    except KeyboardInterrupt:
        print('Program Interrupted by User')


main()
