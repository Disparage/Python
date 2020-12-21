# Title     : Learning Code
# Objective : A Code that can be used to learn R
# Created by: Ethan
# Created on: 10/27/2020

variable_n <- 1:100
# In the consol you will notice the 2nd printed line starts with [38], that is the place in the vector it printing from
variable_inf <- Inf
# Inf is for infinity
variable_vector <- c(1.7,"Hello") # since you put a character class with a numeric class 1.7 is converted to a character
# to force it to become some other type of class, if possible, use as.numeric() or as.character() or as.logical()
# if it isn't possible, you will be a vector of NA and a warning
# c() can be used to create vectors of objects

x <- list("hi", 1, TRUE, 1+4i, 5, 6, 7, "Eight", TRUE*9, FALSE + 10)
# print out the list to notice how it formats the printout of the list, use the list() command to make a list
print(x)

learning_matrix <- matrix(1:6, nrow = 2, ncol = 3)
# the standard way to create a matrix with the values of the matrix first, the number of rows next, then the number of
# columns following

x <- 1:10       # comment this out to see how the following comand affects a list with multiple classes
dim(x) <- c(2,5)

print(x)
# this is another way to create a matrix but instead this time you use a vector or list, if you want to see how it
# would order the list just comment out the x<- 1:10 and run the code again

x <- 1:3
y <- 10:12
cbind(x, y)
print (x)
rbind(x, y)

# another way to create a matrix using multiple vectors, as you notice when I print x, it doesn't reformat the existing
# vector, just formats the print out, so you can then save the cbind or rbind function to a variable to create your
# matrix

c <- factor(c("yes", "yes", "no", "yes", "no"), levels = c("yes", "no"))
print(c)
table(c)
unclass(c)
attr(c,"levels")

# factors are vectors with data labels, like python dictionaries in the factor command you create the vector first
# then with the levels command you can set the order that the labels are stored in the vector (I'm still figuring this out)

# is.na() or is.nan() can be used to check if there are any missing values in a vector (use is.na()) or if there are any
# values in the vector that aren't a number (is.nan())


x <- data.frame(foo = 1:4, bar = c(T, T, F, F))
x

nrow(x)
ncol(x)
# data frames are good ways to organize tables, we will be using these to handle the csv files and store the data
# that we need to so that we can export it into another file.