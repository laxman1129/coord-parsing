with open("coordinates.log", "r") as file:
    parsing = False
    count = 1
    temp = ''
    for line in file:
        if line.__contains__('CURRENT STRUCTURE'):
            parsing = True
            file = open(r"./out/" + str(count)+'.dat', "w+")

        if line.__contains__('CHANGE IN THE REACTION COORDINATE'):
            parsing = False
            file.close()
            count = count + 1
            # break

        if parsing:
            if line.__contains__('CURRENT STRUCTURE'):
                continue
            if line.__contains__('Cartesian Coordinates (Ang):'):
                continue
            if line.__contains__('---------------------------------------------------------------------'):
                continue
            if line.__contains__('(Angstroms)'):
                continue
            if line.__contains__('Number     Number                        X           Y           Z'):
                continue
            file.write(line.replace(line[0:7], ' ', 1).lstrip())

