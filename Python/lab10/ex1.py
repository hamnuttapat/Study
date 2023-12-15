def name_list():
    namelist = []
    count = 1
    while True:  
        name = input(f"Enter name {count} : ")
        if name != "":
            namelist.append(name)
            count += 1
        else:
            break
    print(namelist)

name_list()