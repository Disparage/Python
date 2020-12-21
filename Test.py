import csv

file_2 = open("Test.csv", "a", newline='')

file_2.writelines("hi \n")
file_2.writelines("hello")
file_2.close()