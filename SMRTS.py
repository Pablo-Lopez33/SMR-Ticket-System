#SMRTS app
run = True #will run app if true, turn off is false

#Variables to hold ticket information
Tid = 0 #ticket id
TList = [] #list to hold tickets
NamesList = [] #list to hold names
PhoneList = [] #list to hold phone numbers
ModelsList = [] #list to hold Unit models
StatusList = [] #list to hold ticket status
CheckInDateList = [] #list to hold check-in dates
CheckOutDateList = [] #list to hold check-out dates
TicketParts = {} #dict to hold parts used      key: Ticket ID, value: list of parts
TicketCost = {} #dict to hold parts costs key: Ticket ID, value: list of costs
Tax = .0775 #tax rate for parts
# possibly make a open tickets, closed tickets and all time tickets list all sperate by status?

#functions for App UI
def spacing():
    print("\n")  # Adds a new line for spacing

def borders():
    print("-" * 30)  # Prints a border line for better UI

def space():
    print(" ")  # Adds a single space for better readability


# defined fuinctions for the app 


# Option 1: Create Ticket
def CreateTicket():
    global Tid, TList, NamesList, PhoneList, ModelsList, StatusList, CheckInDateList
    print("Creating a new ticket")
    Name = input("Enter your name: ")
    Phone = input("Enter your phone number (XXX-XXX-XXXX): ")
    Model = input("Enter the unit model: ")
    Status = "Open"
    CheckinDate = input("Enter the check-in date (MM-DD-YYYY): ") # Assuming date format is MM-DD-YYYY (US format)
    Tid += 1
    TList.append(Tid)
    NamesList.append(Name)
    PhoneList.append(Phone)
    ModelsList.append(Model)
    StatusList.append(Status)
    CheckInDateList.append(CheckinDate)
    spacing()
    borders()
    print("Ticket created successfully!")
    print(f" Your Ticket ID is: {Tid}")
    borders()
    spacing()

# Option 2: Add Parts to Ticket
def AddPart():
    global TList, TicketParts, TicketCost
    ticket_id = int(input("Enter the Ticket ID to add part to: "))
    if ticket_id in TList:
        part = input("Enter part name: ")
        cost = float(input("Enter part cost: "))

        if ticket_id not in TicketParts:
            TicketParts[ticket_id] = []
            TicketCost[ticket_id] = []

        TicketParts[ticket_id].append(part)
        TicketCost[ticket_id].append(cost)

        spacing()
        borders()
        print(f"Part '{part}' added to Ticket {ticket_id} for ${cost:.2f}")
        borders()
    else:
        spacing()
        borders()
        print("Ticket ID not found.")
        borders()
    spacing()



# Option 3: Update Ticket Status
def UpdateStatus():
    global Tid, TList, StatusList
    print("Updating a ticket")
    if not TList:
        space()
        borders()
        print("No Tickets available to update.")
        borders()
        

    else:
        ticket_id = int(input("Enter the Ticket ID to update: "))
        if ticket_id in TList:
            index = TList.index(ticket_id)
            StatusList[index] = input("Enter new status (In Progress, Waiting for Parts, Closed, Not Repairable): ")
            spacing()
            borders()
            print(f"Ticket ID: {ticket_id} Status has been changed.")
            borders()
            
        else:
            spacing()
            borders()
            print("Ticket ID not found.")
            borders()
    spacing()

# Option 4: View Ticket Status
def StatusCheck():
    global Tid, TList, StatusList
    print("Viewing ticket status")
    if not TList:
        spacing()
        borders()
        print("No tickets available.")
        borders()
    else:
        ticket_id = int(input("Enter the Ticket ID to check status: "))
        if ticket_id in TList:
            index = TList.index(ticket_id)
            spacing()
            borders()
            print(f"Ticket ID: {ticket_id}, Status: {StatusList[index]}")
            borders()
        else:
            spacing()
            borders()
            print("Ticket ID not found.")
            borders()
    spacing()

# Option 5: Lookup Ticket by ID
def LookupTicket():
    global Tid, TList, NamesList, PhoneList, ModelsList, StatusList, CheckInDateList
    print("Looking up a ticket by ID")
    if not TList:
        spacing()
        borders()
        print("No tickets available.")
        borders()
    else:
        ticket_id = int(input("Enter the Ticket ID to lookup: "))
        if ticket_id in TList:
            index = TList.index(ticket_id)
            spacing()
            borders()
            print(f"Ticket ID: {TList[index]}, Name: {NamesList[index]}, Phone: {PhoneList[index]}, Model: {ModelsList[index]}, Status: {StatusList[index]}, Check-in Date: {CheckInDateList[index]}")
            borders()
        else:
            spacing()
            borders()
            print("Ticket ID not found.")
            borders()
    spacing()

# Option 6: View All Tickets
def ViewAllTickets():
    global Tid, TList, NamesList, PhoneList, ModelsList, StatusList, CheckInDateList
    print("Viewing all tickets")
    if not TList:
        spacing()
        borders()
        print("No tickets available.")
        borders()
    else:
        for i in range(len(TList)):
            borders()
            print(f"Ticket ID: {TList[i]}, Name: {NamesList[i]}, Phone: {PhoneList[i]}, Model: {ModelsList[i]}, Status: {StatusList[i]}, Check-in Date: {CheckInDateList[i]}")
    spacing()

# Option 7: View Closed Tickets
def ViewClosedTickets():
    global Tid, TList, NamesList, PhoneList, ModelsList, StatusList, CheckInDateList
    print("Viewing closed tickets")
    closed_tickets = [i for i in range(len(StatusList)) if StatusList[i] == "Closed"]
    if not closed_tickets:
        spacing()
        borders()
        print("No closed tickets available.")
        borders()
    else:
        for i in closed_tickets:
            borders()
            print(f"Ticket ID: {TList[i]}, Name: {NamesList[i]}, Phone: {PhoneList[i]}, Model: {ModelsList[i]}, Status: {StatusList[i]}, Check-in Date: {CheckInDateList[i]}")
    spacing()

# Option 8: Print Invoice
def PrintInvoice():
    global Tid, TList, NamesList, PhoneList, ModelsList, StatusList, CheckInDateList, TicketParts, TicketCost, Tax 
    print("Printing invoice")
    if not TList:
        spacing()
        borders()
        print("No tickets available to print invoice.")
        borders()
    else:
        ticket_id = int(input("Enter the Ticket ID to print invoice: "))
        if ticket_id in TList:
            index = TList.index(ticket_id)
            print(f"Invoice for Ticket ID: {TList[index]}")
            space()
            #print(f"Name: {NamesList[index]}, Phone: {PhoneList[index]}, Model: {ModelsList[index]}, Check-in Date: {CheckInDateList[index]}")
            print('Customer Information:')
            borders()
            print(f"Name: {NamesList[index]}")
            print(f"Phone: {PhoneList[index]}")
            print(f"Model: {ModelsList[index]}")
            print(f"Check-in Date: {CheckInDateList[index]}")
            space()

            parts = TicketParts.get(ticket_id, [])
            costs = TicketCost.get(ticket_id, [])

            if parts:
                print("Parts Used:")
                borders()
                for part in parts:
                    print(f"- {part} (${costs[parts.index(part)]:.2f})")
                total = sum(costs) * (1 + Tax)
                space()
                borders()
                print("Invoice Summary:")
                borders()
                print(f"Subtotal: ${sum(costs):.2f}")
                print(f"Tax (7.75%): ${sum(costs) * Tax:.2f}")
                print(f"Total Cost (with tax): ${total:.2f}")
                print("Thank you for choosing us!")
            else:
                print("No parts used.")
        else:
            print("Ticket ID not found.")
    spacing()



#Main loop for the app
while run == True:
    
    #Main Menu + Options
    print("Welcome to SMRTS app!")
    borders()
    space()
    print("Please select an option: ")
    print("1. Create Ticket")
    print("2. Add Parts to Ticket") 
    print("3. Update Ticket Status") 
    print("4. View Ticket Status")
    print("5. Lookup Ticket by ID")
    print("6. View All Tickets") 
    print("7. View Closed Tickets")
    print("8. Print Invoice")
    print("86. Exit") # Play on words since 86 is the number for "no more" in restaurant lingo, "86 SMRTS app"


    # Choice loop
    choice = input()
    
    # Choice 1: Create Ticket
    if choice == '1':
        CreateTicket()

    # Choice 2: Add Parts to Ticket
    elif choice == '2':
        AddPart()
    
    # Choice 3: Update Ticket Status
    elif choice == '3':
        UpdateStatus()

    # Choice 4: View Ticket Status
    elif choice == '4':
        StatusCheck()

    # Choice 5: Lookup Ticket by ID
    elif choice == '5':
        LookupTicket()

    # Choice 6: View All Tickets
    elif choice == '6':
        ViewAllTickets()

    # Choice 7: View Closed Tickets
    elif choice == '7':
        ViewClosedTickets() 

    # Choice 8: Print Invoice
    elif choice == '8':
        PrintInvoice()

    # Choice 86: Exit the app
    elif choice == '86':
         print("Exiting the app. Goodbye!")
         run = False # Exit the app

    # Invalid choice handling
    else:
        print("Invalid choice. Please pick an existing option.")


# End of main loop
