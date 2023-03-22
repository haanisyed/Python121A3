'''
CISC-121 2023W
Name: Haani Syed
Student Number: 20331181
Email: 21ahs7@queensu.ca
Date: 2023-03-08
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity.
'''
import csv
def conversion():
    '''
    This function takes the CSV file and using its copied path, removes BOM characters from file, converts the data into a list of dictionaries to be used by functions (339 dictionaries)
    :return: returns list of dictionaries. No parameters.
    '''
    list_with_data = [] #empty list which will take in data to create list of dictionaries
    with open(r'table_tableau11.csv', 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row = {key.replace('\ufeff', ''): value for key, value in row.items()}
            list_with_data.append(row)
    return list_with_data

def displayInfo(list_with_data): #linear search
    '''
    This function prints the important values (Polling Stations, Valid Ballots, Total Ballots Cast, Percentage of Voter Turnout) of dictionary containing user inputted Electoral District Number (electoral_district_num).
    :param list_with_data: list of dictionaries is parameter
    :return: will print the polling stations, valid ballots, total ballots cast, percentage of voter turnout
    '''
    electoral_district_num = input('Please enter an Electoral District Number: ')
    for dictionary in list_with_data:
        if electoral_district_num in dictionary.values():
            print('Polling Stations:', dictionary['Polling Stations']+ ',' 'Valid Ballots:',dictionary['Valid Ballots']+',' 'Total Ballots Cast:',dictionary['Total Ballots Cast']+',' 'Percentage of Voter Turnout:',dictionary['Percentage of Voter Turnout'] +'%' )


def uniqueDistricts(list_with_data, Province): #user would mention province when calling the function
    '''
    This function returns the filtered list (names of electoral districts aka cities/towns/villages) after user mentions the specific province needed.
    :param list_with_data: list of dictionaries (339 dictionaries)
    :param Province: specific province entered by user
    :return: returns a list of the names of the electoral districts in that province.
    '''
    filtered_list = [] #filtered list initialized, to be returned with names of electoral districts.
    for dictionary in list_with_data: #for dictionary in list of dictionaries.
        if dictionary['Province'] == Province:
            filtered_list.append(dictionary['Electoral District Name'])
    return filtered_list #returns


def findMax(list_with_data, key): # Linear Search.
    '''
    This function returns the max value and electoral district name for the entered key from(Electors, Population, Polling Stations, Valid Ballots, Rejected Ballots, Percentage of Rejected Ballots, Total Ballots Cast, Percentage of Voter Turnout)
    :param list_with_data: list of dictionaries
    :param key: One of entered by user: Electors, Population, Polling Stations, Valid Ballots, Rejected Ballots, Percentage of Rejected Ballots, Total Ballots Cast, Percentage of Voter Turnout
    :return:Max Value: Associate Electoral District Name
    '''
    max_dict = None #variable for electoral district name used later
    max_val = float('-inf')
    if not list_with_data:
        return None, None
    for dictionary in list_with_data: #for dictionary in list of dictionaries
        if key in dictionary: #if the key mentioned by user is in dictionary
            val = float(dictionary[key]) #turning the value into float for efficiency purposes
            if val > max_val: #for max
                max_val = val #max value is the value at dictionary[key] in float form.
                max_dict = dictionary['Electoral District Name'] #max_dict variable for Electoral District Name
    return f"{max_val}: {max_dict}" #returns max val: electoral district name


def findMin(list_with_data, key): #Linear Search.
    '''
    :param list_with_data:
    :param key: One of entered by user: Electors, Population, Polling Stations, Valid Ballots, Rejected Ballots, Percentage of Rejected Ballots, Total Ballots Cast, Percentage of Voter Turnout
    :return: Min Value: Associated Electoral District Name
    '''
    min_dict = None #variable for electoral district name used later
    min_val = float('inf')
    for dictionary in list_with_data: #for dictionary in list of dictionaries
        for x in dictionary:
            if x == key:
                val = float(dictionary[key])
                if val < min_val: #for min
                    min_val = val
                    min_dict = dictionary['Electoral District Name'] #returns max val: electoral district name
    if min_dict == None:
        return None
    else:
        return f"{min_val}: {min_dict}" #returns max val: electoral district name

def totalVotes(list_with_data):
    '''
    accepts the list of dictionaries as its parameter and prints out the 13 province/territory: total votes
    fulfills the requirements released for Autograder on 7th March
    :param list_with_data: list of dictionaries
    :return: prints out the 13 province/territory: total votes. In form: province name: #
    '''
    provinces = [] #initalized
    alberta_votes = 0 #initialized
    bc_votes = 0
    mb_votes = 0
    nb_votes = 0
    nfl_votes = 0
    nwt_votes = 0
    ns_votes = 0
    nunavut_votes = 0
    on_votes = 0
    pei_votes = 0
    qc_votes = 0
    sk_votes = 0
    yk_votes = 0
    for dictionary in list_with_data:
        if dictionary['Province'] not in provinces:
            provinces.append(dictionary['Province'])
    for province_territory in provinces:
        province_votes = 0
        for dictionary in list_with_data:
            if dictionary['Province'] == province_territory:
                province_votes = province_votes + int(dictionary['Total Ballots Cast']) #allows addition of total province votes
        if province_territory == 'Alberta':
            alberta_votes = province_votes #total votes for Alberta
        if province_territory == 'British Columbia/Colombie-Britannique':
            bc_votes = province_votes #total votes for British Columbia
        if province_territory == 'Manitoba':
            mb_votes = province_votes #total votes for Manitoba
        if province_territory == 'New Brunswick/Nouveau-Brunswick':
            nb_votes = province_votes #total votes for New Brunwick
        if province_territory == 'Newfoundland and Labrador/Terre-Neuve-et-Labrador':
            nfl_votes = province_votes #total votes for Newfoundland and Labrador
        if province_territory == 'Northwest Territories/Territoires du Nord-Ouest':
            nwt_votes = province_votes #total votes for Northwest Territories
        if province_territory == 'Nova Scotia/Nouvelle-Écosse':
            ns_votes = province_votes #total votes for Nova Scotia
        if province_territory == 'Nunavut':
            nunavut_votes = province_votes #total votes for Nunavut
        if province_territory == 'Ontario':
            on_votes = province_votes #total votes for Ontario
        if province_territory == 'Prince Edward Island/Île-du-Prince-Édouard':
            pei_votes = province_votes #total votes Prince Edward Island
        if province_territory == 'Quebec/Québec':
            qc_votes = province_votes #total votes for Quebec
        if province_territory == 'Saskatchewan':
            sk_votes = province_votes #total votes for saskatchewan
        if province_territory == 'Yukon':
            yk_votes = province_votes #total votes for yukon
    print('Total Votes:') #prints in alphabetical order as required for Autograder
    print('Alberta:', alberta_votes)
    print('British Columbia/Colombie-Britannique:', bc_votes)
    print('Manitoba:', mb_votes)
    print('New Brunswick/Nouveau-Brunswick:', nb_votes)
    print('Newfoundland and Labrador/Terre-Neuve-et-Labrador:', nfl_votes)
    print('Northwest Territories/Territoires du Nord-Ouest:', nwt_votes)
    print('Nova Scotia/Nouvelle-Écosse:', ns_votes)
    print('Nunavut:', nunavut_votes)
    print('Ontario:', on_votes)
    print('Prince Edward Island/Île-du-Prince-Édouard:', pei_votes)
    print('Quebec/Québec:', qc_votes)
    print('Saskatchewan:', sk_votes)
    print('Yukon:', yk_votes)


def selectionSort(list_with_data, key): #selection sort
    '''
    accepts list of dictionaries + a key,
    then sorts the supplied list of dictionaries in increasing order
    based on the specified key
    :param list_with_data: list of dictionaries
    :param key: entered by user, 1 of(Valid Ballots, Total Ballots Cast, Polling Stations, Rejected Ballots, Percentage of Rejected Ballots, Total Ballots Cast, Percentage of Voter Turnout)
    :return:  dictionaries sorted into increasing order based on key used.
    '''
    #selection sort implementation adjusted to suit list of dictionaries (list_with_data)
    m = len(list_with_data)
    for i in range(m):
        min_index = i
        for j in range(i+1, m):
            if list_with_data[j][key] < list_with_data[min_index][key]:
                min_index = j
        if min_index != i:
            list_with_data[i], list_with_data[min_index] = list_with_data[min_index], list_with_data[i]
    return list_with_data



def bubbleSort(list_with_data, key):
    '''
    Bubble Sorts list of dictionaries to be used in Binary Search.
    :param list_with_data: list of dictionaries
    :param key: Electoral District Number
    :return: list of dictionaries bubble sorted by electoral district number
    '''
    #bubble sort implementation adjusted to suit list of dictionaries (list_with_data)
    for i in range(len(list_with_data) - 1):
        for j in range(i + 1, len(list_with_data)):
            if list_with_data[j][key] < list_with_data[i][key]:
                list_with_data[i], list_with_data[j] = list_with_data[j], list_with_data[i]

def binarySearch(list_with_data,key): #call to bubble sort to sort and then binary implemented on data structure
    '''
    Fulfills Requirement 7, searches for an electoral district based on
    electoral district number and returns the percentage of voter turnout in that district.
    calls bubble sort(list_with_data, 'Electoral District Number') so this way its sorted before search starts.
    :param list_with_data: list of dictionaries
    :param key:Electoral District Number
    :return: None, will give 'found: #' when call to function with key printed.
    '''
    bubbleSort(list_with_data, 'Electoral District Number') #call to bubbleSort, ensuring data is sorted before search.
    #binary search implementation adjusted to suit list of dictionaries (list_with_data)
    left = 0
    right = len(list_with_data) - 1
    while left <= right:
        mid = (left + right) // 2
        if list_with_data[mid]['Electoral District Number'] < str(key):
            left = mid + 1
        elif list_with_data[mid]['Electoral District Number'] == str(key):
            return list_with_data[mid]['Percentage of Voter Turnout']
        else:
            right = mid - 1
    return None


def menu():
    '''
    fulfills requirement #8 of creating an interactive menu for the user: (by selecting a respective number for the functions(1-7)).
    :return: none directly. It calls all other functions (1-7) which carry out different analysis on the data as required.
    '''
    list_with_data = conversion()
    user_response = input('Would you like to see the Elections Canada Dataset Analysis (yes/no): ')
    while user_response == 'yes':
        user_number = int(input('Enter a number corresponding to one of the 7 functions: '))
        if user_number == 1:
            print('Display the information for an electoral district')
            displayInfo(list_with_data)
        elif user_number == 2:
            print('Show the unique districts by the given province')
            Province = input('Enter a Province: ')
            print(uniqueDistricts(list_with_data, Province))
        elif user_number == 3: #must fix the errors
            print('Display the maximum value for a key from among(Electors, Population, Polling Stations, Valid Ballots, Rejected Ballots, Percentage of Rejected Ballots, Total Ballots Cast, Percentage of Voter Turnout) ')
            key = input('Enter a key from among (Electors, Population, Polling Stations, Valid Ballots, Rejected Ballots, Percentage of Rejected Ballots, Total Ballots Cast, Percentage of Voter Turnout) : ')
            print(findMax(list_with_data, key))
        elif user_number == 4: #must fix the errors
            print('Display the minimum value for a key from among(Electors, Population, Polling Stations, Valid Ballots, Rejected Ballots, Percentage of Rejected Ballots, Total Ballots Cast, Percentage of Voter Turnout)')
            key = input('Enter a key from among (Electors, Population, Polling Stations, Valid Ballots, Rejected Ballots, Percentage of Rejected Ballots,  Total Ballots Cast, Percentage of Voter Turnout) : ')
            print(findMin(list_with_data, key))
        elif user_number == 5:
            print(totalVotes(list_with_data))
        elif user_number == 6:
            key = input("Enter the key to sort (selection sort) by (Valid Ballots, Total Ballots Cast, Polling Stations, Rejected Ballots, Percentage of Rejected Ballots, Total Ballots Cast, Percentage of Voter Turnout): ")
            print(selectionSort(list_with_data, key))
        elif user_number == 7:
            key = input("Enter the key to search (binary search) by (Electoral District Number): ")
            result = binarySearch(list_with_data, key)
            if result == None:
                print('Item was not found')
            else:
                print('Found:', result) #in alignment with Autograder requirement, prints Found:
        else:
            print('This is an invalid Entry unfortunately. Try again please')
        user_response = input('Would you like to see the Elections Canada Dataset Analysis again? (yes/no): ')
