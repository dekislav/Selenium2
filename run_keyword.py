import csv
from selenium import webdriver 
from keyword_libary import KeywordLibary

def run_test(csv_file):
    driver = webdriver.Chrome()
    keywords =KeywordLibary(driver)

    #open or read the csv file
    with open(csv_file, newline="")as file:
        reader = csv.DictReader(file)
        #create a loop
        for row in reader:
            keyword = row ["Keyword"]
            loacator_type = row["LocatorType"]
            locator_value = row["LocatorValue"]
            data = row["Data"]
            #check the existence of the method in the keyword libary
            if hasattr(keywords,keyword):
                method = getattr # getattr -gets the actual function so that we can cal it later
            if loacator_type and locator_value and data:
                method(locator_value,locator_value,data)
            elif loacator_type and locator_value:
                method(loacator_type,locator_value)
            elif data:
                method(data)
            else:
                method()
        else:
            print(f"Keyword is unknown:{keyword}")        

                
                       
