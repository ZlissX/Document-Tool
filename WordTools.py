while True:
    print( "1.Type 1 to import a file. \n2.Type 2 to enter the passage. \n3.Type 3 to exit back to main menu" )
    askinput=input("Enter your input here: ")
    if askinput == "1":
        while True:
            askconfirm=input("you  have selected import a file type back to go back or press enter").lower()
            if askconfirm=="back":
                break
            if askconfirm not in ["back",""]:
                print("Invalid Input!")
                continue
        
            filenameinput=input("please enter your file name with extension: ")
            try:
                filehandle=open(filenameinput).read()
            except:
                print("Invalid File Name or Extension!")
                continue
        
            fileprocess=filehandle.split()
            findword=input("please enter the word you want to find")
            findd=fileprocess.count(findword)
            print("number of",findword,":",findd)
            while True:
                confirmtotalcount=input("Type yes if you want to print the total amount of word or press enter: ").lower()
                if confirmtotalcount =="yes":
                    totalcount=len(fileprocess)
                    print("Total Number of words:",totalcount)
                    break
                if confirmtotalcount=="":
                    break
                if confirmtotalcount not in["yes",""]:
                    print("Invalid Input!")
                    continue
            while True:
                askexitsub=input("Type back if you wanna go back to the previos menu or press enter to continue: ").lower()
                if askexitsub=="":
                    print("restarting!")
                    continue
                if askexitsub=="back":
                    break
                if askexitsub not in["back",""]:
                    print("invalid input!")
                    continue
            break

            
        

        
               
    if askinput == "2":
        while True:
            askconfirm=input('press back to go back or enter to contnue: ').lower()
            if askconfirm=="back":
                break
            if askconfirm not in["back",""]:
                print("invalid input!")
                continue

            enterpass=input('Enter you passage here')
            passprocess=enterpass.split()
            findword=input("Enter the word you want to find: ")
            findd=passprocess.count(findword)
            print("number of",findword,":",findd)
            totalcount=len(passprocess)

            while True:
                confirmtotalcount=input("Type yes if you want to print the total amount of words or press enter: ").lower()
                if confirmtotalcount =="yes":
                    
                    print("Total Number of words:",totalcount)
                    break
                if confirmtotalcount=="":
                    break
                if confirmtotalcount not in["yes",""]:
                    print("Invalid Input!")
                    continue
            while True:
                askexitsub=input("Type back if you wanna go back to the previos menu or press enter to continue: ").lower()
                if askexitsub=="":
                    print("restarting!")
                    continue
                if askexitsub=="back":
                    break
                if askexitsub not in["back",""]:
                    print("invalid input!")
                    continue
            break


        
            
    if askinput == "3":
        break