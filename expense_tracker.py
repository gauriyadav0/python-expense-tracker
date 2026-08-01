from datetime import datetime

expenseList = []
print("Welcome to our Expense Tracker")

while True:
    print("-------------Welcome to Menu-------------")
    print("Add you expense")
    print("View all expense")
    print("View total spend")
    print("Exit")

    choice = int(input("Kindly enter your choice: "))

    # ADD EXPENSE
    if(choice==1):
        date = input("Date of spent (DD/MM/YY): ") 
        try:
            datetime.strptime(date, "%d/%m/%y")
        except ValueError:
            print("Invalid date! Please use DD/MM/YY format.")

            continue

        category = input("Category like (food, travel, books etc.): ")
        discription = input("Discription: ")
        amount = input("Amount: ")

        expense ={

            "date": date,
            "category" : category,
            "discription" : discription,
            "amount" : amount

        }

        expenseList.append(expense)
        print("Yeah, your all expanses are added")

        # View all expense
    elif (choice==2):
        if(len(expenseList)==0):
            print("You dont spend anything, spend first")
        else:
            print("This is all your expense")
            count =1
            for eachSpend in expenseList:
                print(f"eachSpend {count} -> {eachSpend['date']}, {eachSpend['category']},{eachSpend['discription']},{eachSpend['amount']}")

                count= count+1

# View Total spending
 
    elif(count==3):
        total = 0
        for eachSpend in expenseList:
            total = total + eachSpend['amount']

            print("\n Total spend =", total)

# Exit
    elif(choice==4):
        print("Thank you for choosing our Finance Tracker")
    else:
        print("Invalid choice, try again")
