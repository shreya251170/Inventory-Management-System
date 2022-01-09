#Inventory Management System
#Ganeshi Shreya-19PD12
#Nikila.B-19PD23

import os
import getpass

print("\n\n\n\t\tWELCOME TO INVENTORY MANAGEMENT SYSTEM\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\tBY GANESHI SHREYA-19PD12\n\t\t\t\t\t\t   NIKILA.B-19PD23")
str(input())
#Dictionaries
unit_price={}
description={}
stock={}
customer_pass={}
user_pass={"nikila":"Nikila123","shreya":"Shreya123"}

user_pass1=[]
customer_pass1=[]
l=[]

#Open file with stock
details = open("stock.txt","r")

#First line of the file is the number of items
no_items  = int((details.readline()).rstrip("\n"))

#Add items to dictionaries
for i in range(0,no_items):
    line  = (details.readline()).rstrip("\n")
    x1,x2 = line.split("#")
    x1=int(x1)
    x2=float(x2)
    unit_price.update({x1: x2})

for i in range(0,no_items):
    line  = (details.readline()).rstrip("\n")
    x1,x2 = line.split("#")
    x1=int(x1)
    description.update({x1: x2})

for i in range(0,no_items):
    line  = (details.readline()).rstrip("\n")
    x1,x2 = line.split("#")
    x1=int(x1)
    x2=int(x2)
    stock.update({x1: x2})

details.close()

user=open("passwords.txt","r")

#First line of the file is the number of registered users
no_users  = int((user.readline()).rstrip("\n"))

#Add usernames to dictionaries
for i in range(0,no_users):
    line  = (user.readline()).rstrip("\n")
    x1,x2 = line.split("#")
    x1=str(x1)
    x2=str(x2)
    customer_pass.update({x1: x2})
    customer_pass1.append(x1)
    
user.close()

#List to store the items purchased
cart=[]

c="y" #Runs the while loop as long as user wants

complete=False

#Instructions
os.system("cls")
x=int(input("\n\n\nLogin as:\n\t1.User\n\t2.Manager\nPress 3 to exit\n"))
os.system("cls")

while(x!=1 and x!=2 and x!=3):
    print("\nWrong Option!")
    x=int(input("\n\n\nLogin:\n\t1.User\n\t2.Manager\nPress 3 to exit\n"))
    os.system("cls")
if(x==1):
    a=int(input("\n\n1.Create an account\n2.Log in\n"))
    os.system("cls")
    while(a!=1 and a!=2):
        print("\nWrong Option!")
        a=int(input("\n\n1.Create an account\n2.Log in\n"))
        os.system("cls")
    if(a==1):
        u=input("\nEnter a username:")
        p = getpass.getpass(prompt='Enter a password:')
        cp = getpass.getpass(prompt='Confirm your password:')
        while(p!=cp):
            print("\nSorry!Your passwords don't match!")
            p = getpass.getpass(prompt='Enter a password:')
            cp = getpass.getpass(prompt='Confirm your password\n:')
        customer_pass.update({u:cp})
        customer_pass1.append(u)
        os.system("cls")
    elif(a==2):
        while not complete:
            username = input("\nUsername: ")
            password = getpass.getpass(prompt='Password:')
            if username == customer_pass and password == password:
                continue
            elif username not in customer_pass:
                print("This is not a valid username, input username again!")
                continue
            elif password != customer_pass[username]:
                print(f"Password is not valid for {username}. ")
                k=input("Forgot password?Press1 if yes")
                if(k==1):
                    p = getpass('Enter a password:')
                    cp = getpass('Confirm your password:')
                    while(p!=cp):
                        print("\nSorry!Your passwords don't match!")
                        p = getpass('Enter a password:')
                        cp = getpass('Confirm your password\n:')
                    customer_pass.update({username:cp})
                    customer_pass1.append(username)
                else:            
                    continue
            elif password == customer_pass[username]:
                print(f"\nWelcome {username}!")
                print("\nThank you for logging on!\n ")
                complete = True
                input()
    os.system("cls")
    print("\n\t\tL-List all items")
    print("\t\tI-Inquire about a part")
    print("\t\tP-Purchase")
    print("\t\tC-Checkout")
    print("\t\tS-Show all parts purchased")
    print("\t\tQ-Quit")
    print("\t\tremove-Remove an item from the cart")
    print("\t\thelp-See all commands again")
    c= str(input("\n\t\tWhat would you like to do? "))
    os.system("cls")
    total_cost=0 
    flag=0 #To check if they have checked out
    while(c!= "q" or c!= "Q"):
        if(c=="q" or c=="Q"):
            break
       
        if(c=="L" or c=="l"):#List all the parts
            print("\n")
            print("Products and their prices: ",unit_price)
            print("\nDescriptions: ",description)
            print("\nStock left of Item: ",stock)
            print("\n")
            input()
            os.system("cls")

        elif(c=="I" or c=="i"):#Inquire about a part
            print()
            p_no=int(input("Enter Part Number: "))
            if(p_no in unit_price):
                print(" Product number: ",p_no,"\n Description: ",description.get(p_no),"\n Price: ",unit_price.get(p_no),"\n Stock: ",stock.get(p_no))
                if(stock.get(p_no)<3 and stock.get(p_no)!=0):
                    print("Only ",stock.get(p_no)," remaining! Hurry!")
                print("\n")
            else:
                print("Sorry we don't have such an item!")
                print("\n")
            input()
            os.system("cls")
                
        elif(c=="P" or c=="p"):#Purchase a part
            print()
            p_no = int(input("Enter Product number: "))
            if(p_no in unit_price):
                if(flag==1):
                    flag=0
                stock_current = stock.get(p_no)
                if(stock_current>0):
                    stock_current = stock.get(p_no)
                    stock[p_no] = stock_current-1
                    item_price = unit_price.get(p_no)
                    total_cost = total_cost+item_price
                    print(description.get(p_no),"added to cart: ","$",item_price)
                    cart.append(p_no)#Stores item in cart
                else:
                    print("Sorry! We don't have that item in stock!")
            else:
                    print("Sorry! We don't have such an item!")
            input()
            os.system("cls")
            
        elif(c=="C" or c=="c"):#Check out
            print("\n")
            print("You bought the following parts: ",cart)
            print("Total: ","$",round(total_cost,2))
            tax= round(0.13*total_cost,2)
            print("Tax is 13%: ","$",tax)
            total = round(total_cost+tax,2)
            print("After Tax: ","$",total)
            total_cost=0
            flag=1
            print("\n")
            print("You can still purchase items after check out by pressing any key.To quit press q")
            cart=[]
            d=input()
            if(d=="q" or d=="Q"):
                break
            else:
                os.system("cls")
        
        elif(c=="help"):#Display all commands
            print("\n")
            print("Help Centre")
            print("L-List all items")
            print("I-Enquire about a product")
            print("P-Purchase")
            print("C-Checkout")
            print("S-Show all products purchased")
            print("remove-Remove an item from the cart")
            print("help-See all commands again")
            print("If you have any other questions or concerns please contact the manager.")
            print("\n")
            input()
            os.system("cls")
        
        elif(c=="remove" or c=="Remove"):#To remove an item from the cart
            print("\n")
            are_you_sure = input("Are you sure you want to remove an item from the cart(y/n)? ")
            if(are_you_sure=="y"):
                p_no = int(input("Enter product number to remove from cart: "))
                if(p_no in cart):
                    stock_current = stock.get(p_no)
                    stock[p_no] = stock_current+1
                    item_price = unit_price.get(p_no)
                    total_cost = total_cost-item_price
                    j=0
                    for i in range(0,len(cart)):#To find the index of the part in the list cart
                        if(i==p_no):
                            j=i
    
                    cart.pop(j)
                    print(description.get(p_no),"removed from cart: ")
                    print("\n")
                else:
                    print("\n")
                    print("That item is not in your cart!")
                    print("\n")
                input()
                os.system("cls")
                
        elif(c=="s" or c=="S"):#prints list cart
            if(cart==[]):
                print("Sorry!You didn't purchase anything")
            else:
                print("\n")
                print(cart)
                print("\n")
            input()
            os.system("cls")
            
        else:
            print("\n")
            print("ERROR! Contact manager for help!")
            print("\n")
            input()
            os.system("cls")
            
        print("\n\n\t\tHello ")
        print("\t\tL-List all items")
        print("\t\tI-Inquire about a part")
        print("\t\tP-Purchase")
        print("\t\tC-Checkout")
        print("\t\tS-Show all parts purchased")
        print("\t\tQ-Quit")
        print("\t\tremove-Remove an item from the cart")
        print("\t\thelp-See all commands again")
        print()
        c= input("\t\tWhat would you like to do? ")
        input()
        os.system("cls")
        
if(x==2):   
    flag=0 #To check if they have checked out
    complete=False
    while not complete:
            username = input("\nUsername: ")
            password = getpass.getpass(prompt='Password:')
            if username == user_pass and password == password:
                continue
            elif username not in user_pass:
                print("This is not a valid username, input username again!")
                continue
            elif password != user_pass[username]:
                print(f"Password is not valid for {username}. ")
                continue
            elif password == user_pass[username]:
                print(f"Welcome {username}!")
                print(f"Thank you for logging on! ")
                complete = True
    input()
    os.system("cls")
    print("\n\t\tA-Add an item")
    print("\t\tR-Remove an item")
    print("\t\tE-Edit specifics of an item")
    print("\t\tL-List all items")
    print("\t\tI-Inquire about a part")
    print("\t\tQ-Quit")
    print("\t\thelp-See all commands again")
    c= input("\n\t\tWhat would you like to do? ")
    os.system("cls")
    flag=1
    total_cost=0
    while(c!= "q" or c!= "Q"):
        if(c=="q" or c=="Q"):
            break
        elif(c=="A" or c=="a"):#Add a part
            p_no = int(input("Enter product number: "))
            while(p_no in l):
                p_no=int(input("\nThis product number already exists!Please enter another product number:"))
            p_pr = float(input("Enter product price: "))
            p_desc = input("Enter product description: ")
            p_stock = int(input("Enter product stock: "))               
            #Updating the inventory with the part given by  the user
            unit_price.update({p_no: p_pr})
            description.update({p_no: p_desc})
            if(p_stock > -1):#Checking if the user-given stock value is negative
                stock.update({p_no: p_stock})
            else:
                p_stock = 0
                stock.update({p_no: p_stock})
                print("The stock of an item cannot be negative, the stock has been set to 0.")
            print(" Product number: ",p_no,"\n Description: ",description.get(p_no),"\n Price: ",unit_price.get(p_no),"\n Stock: ",stock.get(p_no))
            print("Product was added successfully!")
            input()
            os.system("cls")
            
        elif(c=="E" or c=="e"):#Edit a part
            print()
            p_no = int(input("Enter product number: "))
            if(p_no in unit_price):
                
                #Getting the values which the user wants to appear after editing
                p_pr = float(input("Enter product price: "))
                p_desc = input("Enter product description: ")
                p_stock = int(input("Enter product stock: "))
                
                #Updating the part details with the new values
                unit_price.update({p_no: p_pr})
                description.update({p_no: p_desc})
                stock.update({p_no: p_stock})
                
            else:
                print("That item does not exist, to add an item use a")
            print()
            input()
            os.system("cls")
        
                
        elif(c=="R" or c=="r"):#Remove a part
            print()
            p_no = int(input("Enter part number: "))
            if(p_no in unit_price):
                are_you_sure = input("Are you sure you want to remove that item(y/n)? ")
                if(are_you_sure=="y" or are_you_sure=="Y"):
                    unit_price.pop(p_no)
                    description.pop(p_no)
                    stock.pop(p_no)
                    print("Item successfully removed!")
                print()
            else:
                print("Sorry, we don't have such an item!")
                print()
            input()
            os.system("cls")
            
        elif(c=="L" or c=="l"):#List all the parts
            print()
            print("Products and their prices: ",unit_price)
            print("\nDescriptions: ",description)
            print("\nStock left of Item: ",stock)
            input()
            os.system("cls")
    
        elif(c=="I" or c=="i"):#Inquire about a part
            print()
            p_no=int(input("Enter product Number: "))
            if(p_no in unit_price):
                print()
                print("Product number: ",p_no," Description: ",description.get(p_no)," Price: ",unit_price.get(p_no)," Stock: ",stock.get(p_no))
                if(stock.get(p_no)<3 and stock.get(p_no)!=0):
                    print("Only ",stock.get(p_no)," remaining! Hurry!")
                print()
            else:
                print("Sorry we don't have such an item!")
                print()
            input()
            os.system("cls")
                
        elif(c=="help"):#Display all commands
            print("\n")
            print("Help Centre")
            print("A-Add an item")
            print("R-Remove an item")
            print("E-Edit specifics of an item")
            print("L-List all items")
            print("I-Enquire about a product")
            print("help-See all commands again")
            input()
            os.system("cls")
        else:
            print("\n")
            print("ERROR!")
            print("\n")
            input()
            os.system("cls")
        print("\n\n\t\tHello",)
        print("\n\t\tA-Add an item")
        print("\t\tR-Remove an item")
        print("\t\tE-Edit specifics of an item")
        print("\t\tL-List all items")
        print("\t\tI-Inquire about a part")
        print("\t\tQ-Quit")
        print("\t\thelp-See all commands again")
        c= input("\t\tWhat would you like to do? ")
        os.system("cls")
#Outputs total if the user quits without checking out
os.system("cls")
if(x==3):
    flag=1
    total_cost=0
if(total_cost>0 and flag==0):
    print()
    print("You bought: ",cart)
    print("Total: ","$",round(total_cost,2))
    tax= round(0.13*total_cost,2)
    print("Tax is 13%: ","$",tax)
    total = round(total_cost+tax,2)
    print("After Tax: ","$",total)
    cart=[]
    
print("Thank you!")

for key in unit_price.keys():
    l.append(key)

#Write the updated inventory to the file
details = open("stock.txt","w")
no_items=len(unit_price)
details.write(str(no_items)+"\n")
for i in range(0,no_items):
    details.write(str(l[i])+"#"+str(unit_price[l[i]])+"\n")
    
for i in range(0,no_items):
    details.write(str(l[i])+"#"+description[l[i]]+"\n")
    
for i in range(0,no_items):
     details.write(str(l[i])+"#"+str(stock[l[i]])+"\n")
    
details.close()

user=open("passwords.txt","w")
no_users=len(customer_pass1)
j=0
user.write(str(no_users)+"\n")
for i in customer_pass:
    user.write(str(customer_pass1[j])+"#"+str(customer_pass[i])+"\n")
    j+=1
user.close()    


