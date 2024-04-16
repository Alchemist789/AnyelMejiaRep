# Project 1
# File Name:     hw21project1.py
# Programmer:    Anyel Mejia
# Date:          April 9, 2024
#
# Problem Statement: Finding the sum and average of all numbers entered
# 
#
# Overall Plan:
# 1.Create sum and nocount with values of 0
# 2.Create a while True statement which will run until the user enters n
# 3.After n is entered, the results will be printed out from what the user entered
#
#
# 
# 

#Variables with values of 0
sum = 0.0
nocount = 0

#While true statement which ask user for numbers until n is entered
while True:
  number = float(input("Enter the number :"))
  sum += number
  nocount += 1

  #If n is entered, the results will be printed out
  choice = input("Would you like to enter another number? (y/n): ")
  if choice.casefold() == 'n':
    break

#Average variable
average = sum / nocount

#Printing out the results
print(f"sum : {sum}")
print(F"average : {average}")