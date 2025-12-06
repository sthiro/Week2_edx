#Special requirments they mentioned => Casing, Strip spaces

usr_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().replace("-"," ").casefold() 

#First it strips accidental spaces both side (or returns same string)
#If there is "-" this symbol it replaces with " " blank space
#Converts all the string letter to small letters

#Length of string remain unchange when adding blank space both side so it's working

match usr_input:
    case "42" | "forty two" : # | => It's or only in case checking
        print("Yes")
    case _:
        print("No")