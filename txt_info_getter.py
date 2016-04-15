
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
from geopy.geocoders import GoogleV3
import operator 
import ogr, os
import osgeo.osr as osr   


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
    #lower case, splits and appends each word. It then prints the number
    #of words the in the inputed text file.
    count = 0
    with open(file_name) as f:
        word_list = []
        for words in f:
            content = str(words)
            word_f = content.lower().split()
            for each_word in word_f:
                word_list.append(each_word)
                if word_list != -1 and word_list != 0:
                    count += 1
    print "The text file you entered has", count, "words"
                    
     
                      
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
    
def geopy(the_word): 

    geolocator =  GoogleV3()
    mycsv = open(r"/Users/jeffkropelnicki/Desktop/addresses.csv", "a")
    location = geolocator.geocode(the_word, exactly_one=True) 
    if location != None:
        Address = location.address
        lat_long = location.latitude, location.longitude
        latitude = str(location.latitude)
        longitude = str(location.longitude)  
        print Address, latitude, longitude
        print""

        list_lat = []
        for i in range(1):
            list_lat.append(lat_long)
        for line in list_lat:
            print(line)   
            
        mycsv.writelines(("\n" + "%s" + ",") %(Address))
        mycsv.writelines(("%s"+",") %(latitude))
        mycsv.writelines(("%s"+"\n") %(longitude))
    
        mycsv.close()    

    shapefile(line)

def shapefile(line):
    
    
    # Input data
    pointCoord = line
    fieldName = 'Lat'
    fieldType = ogr.OFTString
    fieldValue = 'test'
    outSHPfn = "/Users/jeffkropelnicki/Desktop/Test_shapefile/address.shp"

    # create the spatial reference, WGS84
    srs = osr.SpatialReference()
    srs.ImportFromEPSG(4326)


    # Create the output shapefile
    shpDriver = ogr.GetDriverByName("ESRI Shapefile")
    
    if os.path.exists(outSHPfn):
        shpDriver.DeleteDataSource(outSHPfn)
    outDataSource = shpDriver.CreateDataSource(outSHPfn)
    outLayer = outDataSource.CreateLayer(outSHPfn, srs, geom_type = ogr.wkbPoint )

    #create point geometry
    point = ogr.Geometry(ogr.wkbPoint)
    point.AddPoint(pointCoord[0],pointCoord[1])

    # create a field
    idField = ogr.FieldDefn(fieldName, fieldType)
    outLayer.CreateField(idField)

    # Create the feature and set values
    featureDefn = outLayer.GetLayerDefn()
    outFeature = ogr.Feature(featureDefn)
    outFeature.SetGeometry(point)
    outFeature.SetField(fieldName, fieldValue)
    outLayer.CreateFeature(outFeature)    
    

read_file(file)    
    
    




                  
                    

