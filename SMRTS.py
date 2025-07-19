#SMRTS app
run = True #will run app if true, turn off is false

#Variables to hold ticket information
Tid = 0 #ticket id
TList = [] #list to hold tickets
NamesList = [] #list to hold names
PhoneList = [] #list to hold phone numbers
ModelsList = [] #list to hold Unit models
StatusList = [] #list to hold ticket status

#functions for App UI
def spacing():
    print("\n" * 2)  # Adds two new lines for spacing








#Main loop for the app
while run == True:
    print("Welcome to SMRTS app!")
    print("1. Create Ticket")
    print("2. View Tickets")
    print("3. Resolve Ticket")
    print("4. Exit")
    print("Please select an option: ")
    choice = input()
    if choice == '1':
        print("Creating a new ticket")
        Name = input("Enter your name: ")
        Phone = input("Enter your phone number: ")
        Model = input("Enter the unit model: ")
        Status = "Open"
        Tid += 1
        TList.append(Tid)
        NamesList.append(Name)
        PhoneList.append(Phone)
        ModelsList.append(Model)
        StatusList.append(Status)
        print("Ticket created successfully!")
        spacing()
    elif choice == '2':
        print("Viewing all tickets")
        if not TList:
            print("No tickets available.")
        else:
            for i in range(len(TList)):
                print(f"Ticket ID: {TList[i]}, Name: {NamesList[i]}, Phone: {PhoneList[i]}, Model: {ModelsList[i]}, Status: {StatusList[i]}")
        spacing()
    elif choice == '3':
        print("Resolving a ticket")
        if not TList:
            print("No Tickets available to resolve.")
        else:
            ticket_id = int(input("Enter the Ticket ID to resolve: "))
            if ticket_id in TList:
                index = TList.index(ticket_id)
                StatusList[index] = input("Enter new status (In Progess, Waiting for Parts, Closed, Not Repairable): ")
                print(f"Ticket ID: {ticket_id} Status has been changed.")
            else:
                print("Ticket ID not found.")
        spacing()
    elif choice == '4':
         print("Exiting the app. Goodbye!")
         run = False # Exit the app
    else:
        print("Invalid choice. Please pick an existing option or contact support.")
