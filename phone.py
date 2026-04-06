import sys

def initial_phonebook():
    rows, cols = int(input("Please enter inital number of contacts: ")), 5
    phone_book = []
    print(phone_book)
    for i in range(rows):
        print("\nEnter contact %d details in the following order(ONLY!):" % (i+1))
        temp = []
        for j in range(cols):
            if j == 0:
                temp.append(str(input("Enter name: ")))
                if temp[j] == '' or temp[j] == ' ':
                    sys.exit("Name is a mandatory filed. Process exiting due to blank field...")
            if j == 1:
                temp.append(int(input("Enter Number: ")))

            if j == 2:
                temp.append(str(input("Enter e-mail address: ")))
                if temp[j] == "" or temp[j] == ' ':
                    temp[j] = None

            if j == 3:
                temp.append(str(input("Enter the date of birth (dd/mm/yy): ")))
                if temp[j] == "" or temp[j] == ' ':
                    temp[j] = None

            if j == 4:
                temp.append(str(input("Enter category(Family/Friends/Work/Other): ")))
                if temp[j] == "" or temp[j] == ' ':
                    temp[j] = None
        phone_book.append(temp)
    print(phone_book)
    return (phone_book)

def menu():
    print("\t\t\Smartphone Directory", flush=False)
    print("\tYou can now perform the operationd displayed on this phonebook\n")
    print("1. Add a new contact")
    print("2. Remove an existing contact")
    print("3. Delete all contacts")
    print("4. Search for a contact")
    print("5. Displau all contacts")
    print("6. Exit phonebook")

    choice = int(input("Please enter your choice here: "))
    return choice
def add_contact(pb):
    dip = []
    for i in range(len(pb[0])):
        if i == 0:
            dip.append(str(input("Enter name: ")))
        if i == 1:
            dip.append(str(input("Enter number: ")))
        if i == 2:
            dip.append(str(input("Enter email address: ")))
        if i == 3:
            dip.append(str(input("Enter date of birth(dd/mm/yyyy): ")))
        if i == 4:
            dip.append(str(input("Enter category of contact(Family/Friends/Work/other): ")))
    pb.append(dip)
    return pb
def remove_existing(pb):
    query = str(input("Please enter the contact you want to delete: "))
    temp = 0

    for i in range(len(pb)):
        if query == pb[1][0]:
            temp += 1

            print(pb.pop(i))
            print("This contact has now been removed")

            return pb
    if temp == 0:
        print("Sorry, you have entered an invalid contact.\nPlease look over try again later.")
        return pb
    
def delete_all(pb):
    return pb.clear()
def search_existing(pb):
    choice = int(input("Enter search criteria\n1. Name\n2. Number\n3. Email id\n4. DOB(date of birth)\n"))
    temp = []
    check = -1

    if choice == 1:
        query = str(input("PLease enter the name of contact to want to search: "))
        for i in range(len(pb)):
            if query == pb[i][0]
            check = i
            temp.append(pb[i])
    
    elif choice == 2:
        query = int(input("Please enter the number of the contact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][1]
            check = i
            temp.append(pb[i])

    elif choice == 3:
        query = int(input("Please enter the e-mail ID of the contact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][2]
            check = i
            temp.append(pb[i])

    elif choice == 4:
        query = int(input("Please enter the DOB (in dd/mm/yyyy format ONLY)\ of the contact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][3]
            check = i
            temp.append(pb[i])
    
    elif choice == 5:
        query = int(input("Please enter the category of the coontact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][4]
            check = i
            temp.append(pb[i])

    else:
        print("Invalid search criteria")
        return -1
    
    if check == -1:
        return -1
    else:
        display_all(temp)
        return check
    
def display_all(pb):
    if not pb: 
        print("List is empty: []") 
    else: 
		    for i in range(len(pb)):
		        print(pb[i]) 

def thanks():
    print("Thank you for using the Smartphone Directory system!!")
    print("Please visit again")

print("Hello dear user, welcome to our Smartphone Directory system")
print("You may proceed to explore this directory")

ch = 1
pb = initial_phonebook()
while ch in (1, 2, 3, 4, 5):
    ch = menu()
    if ch == 1:
        pb = add_contact(pb)
    elif ch == 2: 
		    pb = remove_existing(pb) 
	elif ch == 3:
         pb = delete_all(pb)
    elif ch == 4:
         d = search_existing(pb)
         if d == -1:
              print("This contact does not exist. PLease try again")
    elif ch == 5:
         display_all(pb)
    else:
         thanks()