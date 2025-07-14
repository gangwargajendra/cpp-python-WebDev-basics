# function with output

def formatName(f_name, l_name) :
    # DocString (It will be first line of code after function defination)
    """Take a first and last name and format it 
    to return the title case version of the name."""
    # name = f_name + " " + l_name
    # name = name.title()  # ye har word ka first letter capital aur sabko small kar deta h
    # return name
    #**********OR***********
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"
    # return  ## Empty return statement will return only "None".

f_name = input("What's your first name?: ")
l_name = input("What's your last name?: ")

name = formatName(f_name=f_name, l_name=l_name)
print(f"Your full name is {name}.")