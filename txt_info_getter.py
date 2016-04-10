
#
# Author Jeff Kropelnicki
# Date created February 28, 2016
#
#
# This is code a reading text files to look for the occurrence of words. 
# For this project I will be using the words to build a database of locations 
# to be used for making a map using ArcGIS. The code will also return a list of 
# all words used in the document and the number of times they occure.


# I added a fuction that will take a loction and print the address and latitude and longitude.


import csv
from geopy.geocoders import Nominatim
import operator 

    
def read_file(file):
    '''
        This is a function that asks the user to input a file path, 
        asks the user to input the word they are looking for in the file, 
        print the lines where the work occurs. 
        It then give an output of all of the words in the user inputted text file 
        with the number of times the word occurs.
        It then counts the number of times the user chosen word is used in the file.
        
    '''
    #reads in the file, asks users for a word they 
    #are searching for then print the lines that have to word.
    #followed by all of the words in the file and how many times 
    #each word is used.
    file_name = raw_input("Enter the .txt file path: ")
    with open(file_name) as f:
        the_word = raw_input("Enter the word you are searching for: ")
        print ""
        for line in f:
            if the_word in line:
                print line 
                
                
    #Assigns each word in the txt document to a list, converts to
    #lower case, splits and appends each word.    
    with open(file_name) as f:
        word_list = []
        for words in f:
            content = str(words)
            word_f = content.lower().split()
            for each_word in word_f:
                word_list.append(each_word)
     
                      
    #Count and prints the number of times user given word occurs.
    total = 0
    with open(file_name) as f:
        for line in f:
            word_count = line.find(the_word)
            if word_count != -1 and word_count != 0:
                total += 1
    print "The word", str(the_word), "occurs", total, "times\n"
    
    
    #Names for the below functions geopy and clean_list to call.
    geopy(the_word)
    clean_list(word_list)    

    

    
    
def geopy(the_word): 
    
    """ This function returns the address with 
    city, zip code, state, county and country.
    It also provides latitude and longitude of 
    the user inputted word from above."""
    
    geolocator = Nominatim()
    location = geolocator.geocode(the_word)
    Address = location.address
    lat_long = (location.latitude,location.longitude)
    print Address
    print lat_long
    print""
 

def clean_list(word_list):
    
    """This function take the list of words in 
    the above list and replaces
    and thing that is not a letter or number 
    with a empty. It then creates a new list"""
    
    clean_word_list = []
    for word in word_list:
        symbols = "!@#$%^&*()_+={}|\/?><,.-- \" \' \" \' "
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            clean_word_list.append(word)
    
    
    create_dict(clean_word_list)
            

def create_dict(clean_word_list):
    
    """Creates a new dictionary of the cleaned 
    list of words from the text document
    and counts the number of times the word occurs."""
    
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for key, value in sorted(word_count.items(), key= operator.itemgetter(1)):
        print key, value
    





read_file(file)    
    
    
    #with open(r"/Users/jeffkropelnicki/Desktop/test.csv", 'w') as fp:
        #a = csv.writer(fp)
        #data = location
        #a.writerow(data)  




                  
                    

