#3. Write a program to read the age of a candidate and determine whether he is eligible to cast his/her own vote.
#Test Data : 21
#Expected Output :
#Congratulation! You are eligible for casting your vote.

age = int(input("Enter your Age"))

if (age < 18):
    print("You are not  eligible for casting your vote.")

elif (age >= 18):
    print("You are not  eligible for casting your vote.")

else:
    print("oops please enter valid age")