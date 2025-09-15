print("Welcome to the fruit app")
act = input("What do you want to do? (add, remove, edit, show, exit): ")
while act != "exit": 

    if act == "add":
        fruit = input("Enter a fruit: ")    
        with open("fruits.txt", "a") as file:
            file.write(fruit + "\n")
            print(f"Added to to-do list: '{fruit}'")
            
    elif act == "show":
        with open("fruits.txt", "r") as file:
            fruits = file.readlines()
        for index, item in enumerate(fruits, start=1):
            print(f"{index}. {item.strip()}")
            
    elif act == "remove":
        with open("fruits.txt", "r") as file:
            fruits = file.readlines()
        print("Which fruit you want to remove? ")
        for index, item in enumerate(fruits, start=1):
            print(f"{index}. {item.strip()}" )
                
        try:
            resp = int(input("Enter a number: "))
            if 1 <= resp <= len(fruits):
                with open ("fruits.txt", "r") as file:
                    fruits = file.readlines()

                remove = fruits.pop(resp -1)
                with open ("fruits.txt", "w") as file:
                    file.writelines(fruits)
                    
                print(f"Successfully removed fruit number '{resp}'")
        except ValueError:
            print("Error: Enter a valid number")

    elif act == "edit":
        with open("fruits.txt", "r") as file:
            fruits = file.readlines()
        print("Which fruit you want to edit? ")
        for index, item in enumerate(fruits, start=1):
                print(f"{index}. {item.strip()}" )  
        try:
            linetoedit = int(input("Enter a number: "))
            if 1 <= linetoedit <= len(fruits):
                newfruit = input("Write your new fruit: ")
                fruits[linetoedit - 1] = newfruit + "\n"
                with open ("fruits.txt", "w") as file: 
                    file.writelines(fruits)
                print(f"Successfully edited fruit '{linetoedit}'")
            else:
                print("Please enter a valid number")    
        except ValueError:
            print("Error: Enter only valid number")
            
    else:
        print("Error: Invalid input")


    act = input("What do you want to do? (add, remove, edit, show, exit): ")
print("Goodbye!")
