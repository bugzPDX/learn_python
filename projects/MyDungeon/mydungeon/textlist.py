def text_list(listtext, sep1=", ", sep2=", and "):
    n = len(listtext)
    if n > 1:
        return sep1.join(listtext[:-1]) + sep2 + listtext[-1]
    elif n == 1:
        return listtext[0]
    else:
        return "nothing!"
