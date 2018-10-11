#define the  html_list function
def html_list(list_of_strings):
    # Your code goes here!
    ALLstring = ""
    cstring = ""
    for index in range(len(list_of_strings)):
        HString = "<li>" + str(list_of_strings[index]) + "</li>"
        ALLstring = ALLstring + HString + "\n"
        cstring = "<ul>" + "\n" + ALLstring + "</ul>" 
    return print (cstring)
    
html_list(['first string', 'second string'])










def html_list(list_items):
    HTML_string = "<ul>\n"
    for item in list_items:
        HTML_string += "<li>{}</li>\n".format(item)
    HTML_string += "</ul>"
    return HTML_string

#html_list([1, 2, 3])

#html_list(["strings", 2.0, True, "and other types too!"])
