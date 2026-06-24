choice= "y" 
## while loop to Enter the students quiz's mark
while choice.lower()== "y":
    # Student marks input
    quiz_1= int(input("Enter Quiz 1 mark: "))
    quiz_2 = int(input("Enter Quiz 2 mark: "))
    quiz_3 = int(input("Enter Quiz 3 mark: "))
    #formula of calculating the average mark
    average = (quiz_1+quiz_2+quiz_3)/3
    #deciding if the student fail or pass 
    if average >= 50:
        print(f"Student passed  with a mark {average:.2f}")
    else:
        print(f"student failed with a mark {average:.2f}")
        #the option for entering the next student mark
    choice = input ("Countinue? selectY/N:")
print("program ended")
