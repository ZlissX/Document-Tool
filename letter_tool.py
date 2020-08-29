while True:
    print('1.Press 1 to import a file: \n2.Press 2 to enter your passage: \n3.Press 3 to exit out of the application: ')
    choose_method=int(input("enter your input here: "))
    #Choice 1
    if choose_method==1:

        filename_input=input("Please enter your File name with extension: ")
        try:
            dochandler=open(filename_input)
        except:
            print("invalid file name detected please make sure to add the file extesion in the end: ")
            filename_input=("Please enter your File name with extension: ")
            filename_input=input("Please enter your File name with extension: ")
            dochandler=open(filename_input)
        doc=dochandler.read()

        stripped_doc=doc.rstrip()

        char_count=0

        find_letter=0

        total_letter_counter=0
    
        number_of_int=0

        total_punctuation=0

        input_conformation_specific_letter_counter=input("Type yes if you want to know the count of specific word: ").lower()

        if input_conformation_specific_letter_counter==("yes"):

            letter_to_find=input('Enter the letter you want to find: ')
    #print(len(doc))
        for character in stripped_doc:
            if input_conformation_specific_letter_counter==("yes"):
                if character==letter_to_find:
                    find_letter+=1
            
        if input_conformation_specific_letter_counter=="yes":
            print("Total number of",letter_to_find+":" ,find_letter)        
        
        for charr in stripped_doc:

            if not charr in ['!', "," ,";" , ".", "-" ,"?", "/", "<", ">","(",")","`","~","$",'#',"@","#","%","^","*","-","_","+","=","|","&","=","[","]","{","}"," ","\n","'"]:
                total_letter_counter+=1
            if charr in ['!', "," ,"\'" ,";" ,"\"", ".", "-" ,"?"]:
                total_punctuation+=1
        
            try:
                integer=int(charr)
                if integer==int(charr):
                    total_letter_counter-=1
                    number_of_int+=1
            except:
                total_letter_counter=total_letter_counter
        ask_forint_tot_punc=input('type yes if you want to print the amount of letters,integers and punctuaion marks? :').lower()
        if ask_forint_tot_punc=="yes":
            print("The total amountof letters: \n",total_letter_counter)
            print("the total amount of integers: \n",number_of_int)
            print("The total amount of punctuation mark: \n",total_punctuation)
            if input_conformation_specific_letter_counter=="yes":
                print("Total number of",letter_to_find+":" ,find_letter) 


        ask_exit1=input("type yes and press enter if you want to exit out of the application or press enter to countinue").lower()
        
        if ask_exit1=="yes":
                exit()
        if ask_exit1=="":
                continue
        if ask_exit1!="yes"or "":
            print("invalid input!")
            ask_exit1=input("type yes and press enter if you want to yes out of the application or press enter to countinue").lower()
            if ask_exit1=='yes':
                exit()
            else:
                print("Invalid Input!")
    #Choice 2
    if choose_method==2:
        while True:
            passs=str(input('Please enter your passage here:'))
            letinpass=0
            let=0
            amountofint=0
            Total_Numbers=0
            Total_letters=0
            punctuationmarks=0
            notanumber=0


            for letterss in passs:
                if letterss in ('!', "," ,"\'" ,";" ,"\"", ".", "-" ,"?", "/", "<", ">","(",")","`","~","$",'#',"@","#","%","^","*","-","_","+","=","|","&","=","[","]","{","}"): #if the letters in the loop matches this it will deduct one from the totoal count
                    letinpass=letinpass-1
                try:
                    if let==int(letterss):
                        letinpass=letinpass-1
                        amountofint=amountofint+1
                except:
                    if letterss != ' ':
                        letinpass = letinpass+1
            print('The Total amount of Letters:\n',letinpass)



            Letter=(input('what letter do you want to find ?'))
            print("you want to  find :" ,Letter)
            count=0


            for letters in passs:
                if letters==Letter:
                    count += 1

            print(count)
            askint=((input('Type yes if you want to know the amount of integers,punctuation marks and letters in the passage:')).lower())
            if askint == 'yes':
                for lett in passs:
                    if lett in ('!', "," ,"\'" ,";" ,"\"", ".", "-" ,"?"):
                        punctuationmarks+=1
                    if lett in ('!', "," ,"\'" ,";" ,"\"", ".", "-" ,"?", "/", "<", ">","(",")","`","~","$",'#',"@","#","%","^","*","-","_","+","=","|","&","=","[","]","{","}"):
                        Total_letters-=1
                    try:
                        spare=int(lett)
                        if spare==int(lett):
                            Total_Numbers+=1
                    except:
                        if lett != ' ':
                            Total_letters=Total_letters+1  

                print('The amount of letters:\n',Total_letters)
                print('The amount of integers:\n',Total_Numbers)
                print('The amount of punctuation marks:\n',punctuationmarks)

            programexit=((input('do you want to exit the program ? if yes type yes or press enter:')).lower())#.lower() will convert all of them to lower case letters
            if programexit!='yes':
                print('restarting')
                break
            if programexit=='yes':
                exit()#this  will exit out of the program
    #Choice 3
    
    if choose_method==3:
        break
            
            


    
    




        
    