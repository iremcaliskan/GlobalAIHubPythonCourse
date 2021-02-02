"""
    Create a List and swap the second half of the list with 
    the first half of the list and print this list on the screen.
"""

mylist = ["Global", "AI", "Hub", "Community", "Introduction", "to", "Python", "Programming"]
reminder = len(mylist) % 2
halfOfTheList = int(len(mylist)/2)

if  reminder == 0:
    for i in range(halfOfTheList):
        mylist[i], mylist[i + halfOfTheList] = mylist[i + halfOfTheList], mylist[i]
        
else:
    for i in range(halfOfTheList):
        mylist[i], mylist[1 + i + halfOfTheList] = mylist[1 + i + halfOfTheList], mylist[i]
print(mylist)


"""
    Ask the user to input a single digit integer to a variable 'n'.
    Then, print out all of the even numbers from 0 to n (including n).
"""
n = input("Enter a digit \n") # default str

if len(n) > 1 :
    print("Error! Only single digit is allowed. \nTry Again!")
else:
    n = int(n)
    for i in range(n+1): # n: 0,..,5
        if i%2 ==0:
            print(i)    