while True:
    print("1.Count the number of lines in a file.\n2.exit")
    askinput=input("please enter your input: ")
    if askinput=="1":
        while True:
            filenameinput=input("please enter your file name with extension: ")
            try:
                filehandle=open(filenameinput).read()
            except:
                print("Invalid File Name or Extension!")
                continue
            totallinecount=filehandle.count("\n")
            print("total number of lines in your document:",totallinecount+1)

            while True:
                askexitsub=input("Type back if you wanna go back to the previos menu or press enter to continue: ").lower()
                if askexitsub=="":
                    print("restarting!")
                    break
                if askexitsub=="back":
                    break
                if askexitsub not in["back",""]:
                    print("invalid input!")
                    continue
            if askexitsub=="":
                continue
            if askexitsub=="back":
                break
    if askinput=="2":
        break
    if askinput not in ["1","2"]:
        print("invalid input")
        continue