
while True:
    print('Type 1 to import a file \nType 2 to enter your passage \nType 3 to exit')
    askinput=input("Enter your input here: ")
    if askinput not in ["1","2","3"]:
        print("invalid input please try again!")
        continue
    if askinput  =="1":
        while True:
            filenameenter=input("Enter your file name with Extension: ")
            try:
                filehandler=open(filenameenter)
            except:
                print("invalid input!")
                continue
            while True:
                letter_to_find=input("enter the letter that you wanna find: ")
                if len(letter_to_find)!=1:
                    print("don't add more or less than one letter")
                    continue
                break
            while True:
                letter_to_replace=input("enter the letter that you wanna replace: ")
                if len(letter_to_replace)!=1:
                    print("don't add more or less than one letter")
                    continue
                break
            while True:
                replaced=filehandler.read().replace(letter_to_find,letter_to_replace)
                askoutputfilename=input("enter the output file name: ")
                extension=input("enter the extension name without '.' : ")
                try:
                    outputt=open(askoutputfilename+"."+extension,"w")
                    outputt.write(str(replaced))
                    outputt.close()
                    break
                except:
                    print("Invalid enteries!")
                    continue

                print("exported!")

            askinput=input("Press yes if you want to print the exported output: ").lower()
            if askinput=="yes":
                print(replaced)
            askexit1=input("type yes to go back to the previous menu or press enter if you wanna continue").lower()
            try:
                if askexit1=="yes":
                    break
            except:
                continue



    if askinput=="2":
        while True:
            passageenter=input("Enter your passage here: ")
            while True:
                letter_to_find=input("enter the letter that you wanna find: ")
                if len(letter_to_find)!=1:
                    print("don't add more or less than one letter")
                    continue
                break

            while True:
                letter_to_replace=input("enter the letter that you wanna replace")
                if len(letter_to_replace)!=1:
                    print("don't add more or less than one letter")
                    continue
                break
        
            replaced=passageenter.replace(letter_to_find,letter_to_replace)
            
            askoutputfilename=input("Enter the file name: ")
            extension=input("enter the extension name without '.' : ")
            outputfile=open(askoutputfilename+"."+extension,"w")
            outputfile.write(replaced)
            outputfile.close()
            
            askinput=input("Press yes if you want to print the exported output: ").lower()
            if askinput=="yes":
                print(replaced)
            askexit1=input("type yes to go back to the previous menu or press enter if you wanna continue").lower()
            try:
                if askexit1=="yes":
                    break
            except:
                continue
    if askinput=="3":
        break
      

    
            
            
            
            


    
        
    

