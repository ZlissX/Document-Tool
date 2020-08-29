while True:
    print("Type \n1.Letter tools. \n2.Word tools. \n3.Line Tools. \n4.Letter Replacer. \n5.Word Replacer.\n0.Exit")
    ask_main_input=None
    ask_main_input=input("Enter your input here: ")
    
    
    if ask_main_input=="1":
        exec(open("Letter_tool.py").read())
        #exec executes the file instead of  importing it.
        #make sure to open and the file and read it to make it work.
    if ask_main_input=="2":
        exec(open("WordTools.py").read())
    if ask_main_input=="3":
        exec(open("LineTools.py").read())
    if ask_main_input=="4":
        exec(open('Letter_Replacer.py').read())
    if ask_main_input=="5":
        exec(open('Word_Replacer.py').read())
    if ask_main_input=="0":
        exit()
    if ask_main_input not in["1","2","3","4","5","0"]:
        print("invalid input!")
        
    