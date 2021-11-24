List = ["Append an element", "Insert an element", "Append a list to the given list", "Modify an existing element",
        "Delete an existing element from its position", "Delete an existing element with a given value",
        "Sort the list in the ascending order", "Sort the list in descending order", "Display the list"]

default = ["a", "b", "c", "d"]
while True:
    for i in range(len(List)):
        print(str(i + 1) + ". " + List[i])
    input_txt = int(input("Please enter your choice (1-9): "))
    print("*" * 50)
    if input_txt == 1:
        added = input("Append element to list: ")
        default.append(added)
    elif input_txt == 2:
        string = input("Insert element to list: ")
        pos = int(input("Enter position: "))
        default.insert(pos, string)
    elif input_txt == 3:
        list_input = list(input("Enter List: "))
        default += list_input
    elif input_txt == 4:
        pos = int(input("Enter position to replace: "))
        element = input("Enter new element: ")
        default[pos] = element
    elif input_txt == 5:
        pos = int(input("Enter position to delete: "))
        del default[pos]
    elif input_txt == 6:
        el = input("Enter element to delete: ")
        default.remove(el)
    elif input_txt == 7:    
        print(sorted(default))
    elif input_txt == 8:
        print(sorted(default, reverse=True))
    elif input_txt == 9:
        print(default)
    else:
        pass
        
    
    