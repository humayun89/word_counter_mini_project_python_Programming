# Print the welcome message to the user .
# Take a string (message) and a letter from the user.
#Count how many times this letter occured.
# Calculate the percentage of the letter in the message.
# Print the output to the user

print("Welcome to the first mini project! I am an application that takes a message and a letter from you . My task is to count how many times this letter occured and calculate its percentage ")

user_message= input("Please enter your message ")
user_letter = input("Please enter the letter ")
count= user_message.count("o")
print(count)
len_message=len(user_message)
print(len_message)
perc= count/ len_message * 100
print(perc)
print("The count of the letter", user_letter , "is" ,count )
print("The percentage of the letter " , user_letter, "is", perc)