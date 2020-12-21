# Created by Ethan Korte for Honors College Racing Crew use
# This program is to be used as a way to show how we will be utilizing files and parsing through the data
# This is just an example program so feel free to download this and try things out.

import csv

counter = 0
# Setup Code, will import the csv library which will be used to parse through the data in the file_1
# Counter variable is used to go for when you need to count in a loop to find data

# file_name_1 = input("Enter the CSV data file_1 name: ")
# this is just an example of how you can have all of the code be based off of user input
# for the sake of this code I am just redefining the actual file_1 name below, in the future
# that input statement will be used to make it easier, but for now its just easier to have in
# hard coded in, if you are using PyCharm that weird comment below just suppresses an annoying error
# since it was redeclared without usage

# noinspection PyRedeclaration
file_name_1 = "Guido_17_2018_03_30_Run_1.csv"
file_name_2 = "Combined_Data.csv"
file_1 = open(file_name_1, "r")
file_2 = open(file_name_2, "a", newline='')

csv_1 = csv.reader(file_1)
csv_2 = csv.reader(file_2)

writer_1 = csv.writer(file_1)
writer_2 = csv.writer(file_2)
# This block opens the file_1 as read only, then using a csv function, turns the file_1 into a list\


column = int(input("Which column of data do you want to retrieve: "))
print("")  # this is just a way to make the output look neater
# This block is to allow the user to input which column of data they want to retrieve

for row in csv_1:  # this row allows you to loop through each row in the file_1 without knowing
    # how many rows there are

    writer_2.writerow([file_name_1])

    counter = counter + 1  # this allows you to control what data you want to manipulate without
    # having to deal with the whole document

    if counter == 13:
        # print("The following data is:", row[column])
        writer_2.writerow([row[column]])
        data_list = [row[row[column]]]


    if counter == 15:
        # print("Units:", row[column])
        writer_2.writerow([row[column]])
        # print("")  # this is just a formatting trick to make it easier to read the output
    # the if statements above serve to inform us what data we are printing and what unit it is using
    # they simply just locate the row of the data that has the relevant, data, then print from the row
    # we want to

    if 18 <= counter:  # this waits until you hit the data part of the file_1, which is the 18th row
        # till the 35th row

        writer_2.writerow([row[column]])
        print(1)  # this ensures that you only print a certain columns data
        # the column of data that we chose to print is the Exhaust Temperature
    else:
        print(0)

file_2.close()
file_1.close()  # this closes the file_1, it is good practice to close files when you are done with them
# it helps for when you are using multiple open files at once so you don't mix up the files in the code
# if you no longer need a file_1 you should always close it
