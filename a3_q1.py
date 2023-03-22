'''
CISC-121 2023W
Name: Haani Syed
Student Number: 20331181
Email: 21ahs7@queensu.ca
Date: 2023-03-08
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity.
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