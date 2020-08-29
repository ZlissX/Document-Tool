while True:
    print('1.Type 1 to import the file  \n2.Type 2 to write the passage\n3.Type 3 to go back to the main menu')
    askinput=input("Enter your input  here: ")
    
    #choice 1
    if askinput=="1":
        confirmprompt=input("Type back to go back to the previous menu or press enter: ")
        
        if confirmprompt=="":
            print("")
        if confirmprompt=="back":
            break
        
        while True:
            importnamefile=input("Enter the file name with Extension: ")
            try:
                filehandler=open(importnamefile).read()
            except:
                print("invalid file name or extension!")
                continue
            break
        fileprocess=filehandler
        wordtofind=input("enter the word you want to find: ")
        wordtoreplace=input("enter the word to replace: ")
        

        replacedfile=fileprocess.replace(wordtofind,wordtoreplace)
        while True:
            askprint_or_export=input("1.Enter 1 to print the file. \n2.Enter 2 to export the file.")
            if askprint_or_export=="1":
                print(replacedfile)
                break
            if askprint_or_export=="2":
                while True:
                
                    askoutputfilename=input("enter the output file name: ")
                    extension=input("enter the extension name without '.' : ")
                    try:
                        outputt=open(askoutputfilename+"."+extension,"w")
                        outputt.write(str(replacedfile))
                        outputt.close()
                        break
                    except:
                        print("Invalid enteries!")
                        continue

                    print("exported!")
                break

            if askprint_or_export not in["1","2"]:
                print("invalid input!")
                continue
        while True:
            subexitpromot=input("press exit if you wanna exit to previous menu or press enter to continue: ")
            if subexitpromot not in ["exit",""]:
                print("Invalid input!")
                continue
            else:
                break
        
        
        
        
        if subexitpromot=="exit":
            break
        if subexitpromot=="":
             print("restarting!")
             continue

    #choice 2
    if askinput=="2" :

        confirmprompt=input("Type back to go back to the previous menu or press enter: ")
        
        if confirmprompt==(""):
            print("")
        if confirmprompt=="back":
            break
            
        passagee=input('Enter your passage here')
        
        
        passgeprocess=passagee
        wordtofind=input("enter the word you want to find: ")
        wordtoreplace=input("enter the word to replace: ")
        replacedfile=passgeprocess(wordtofind,wordtoreplace)
        
        while True:
            askprint_or_export=input("1.Enter 1 to print the file. \n2.Enter 2 to export the file.")
            if askprint_or_export=="1":
                print(replacedfile)
                break
            if askprint_or_export=="2":
                while True:
                
                    askoutputfilename=input("enter the output file name: ")
                    extension=input("enter the extension name without '.' : ")
                    try:
                        outputt=open(askoutputfilename+"."+extension,"w")
                        outputt.write(str(replacedfile))
                        outputt.close()
                        break
                    except:
                        print("Invalid enteries!")
                        continue

                    print("exported!")
                break

            if askprint_or_export not in["1","2"]:
                print("invalid input!")
                continue
        while True:
            subexitpromot=input("press exit if you wanna exit to previous menu or press enter to continue: ")
            if subexitpromot not in ["exit",""]:
                print("Invalid input!")
                continue
            else:
                break
        
        
        
        
        if subexitpromot=="exit":
            break
        if subexitpromot=="":
            print("restarting!")
            continue

    if askinput=="3":
        break
    if askinput not in ["1","2","3"]:
        print("invalid input")   
        continue