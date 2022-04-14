def shopping_cart():
    cart = {} # 2) Stores user input into a dictionary or list 
    while True: 
        user_opt = input("What would you like to do? (Type in one of these options [Show/Add/Delete/Quit]) ").strip() # 1) Takes in options input'food' input # Ask the user four bits of input: Do you want to : Show/Add/Delete or Quit?
        if user_opt.lower() == 'show': # If user option is 'show' # 4) The User can see current shopping list
            print(cart)
        elif user_opt.lower() == 'add': # If user option is 'add' # 3) The User can add 
            food = input(f"What would you like to add? ").strip()
            quantity = input(f"How many {food} would you like to add? ").strip()
            print(f"Great! I have added a total of {quantity} {food} to your cart!")
        elif user_opt.lower() == 'delete': # If user option is 'delete' # 3) The User can add or delete items # 8) Ask how many items they want to remove 
            print(cart)
            food_edit = input(f"Which item would you like to remove? ").strip()
            quantity_edit = input(f"How many {food} would you like to keep? ").strip() 
            if food_edit in cart.keys():                                           
                cart.update({food_edit:quantity_edit})
                cart[food_edit]=quantity_edit
                print(cart)
                print("didn't break")    
            else:
                print("Not in your cart")                                              
        elif user_opt.lower() == 'quit':   # If user option is 'quit' # 5) The program Loops until user 'quits'
            print("Thank you for the monies", cart )
            break
        else: 
            print("Sorry I didn't get that!")
        cart[food]=quantity #2) Stores user input into a dictionary or list
    return cart # 6) Upon quiting the program, print out all items in the user's list
        
        
            
shopping_cart()
