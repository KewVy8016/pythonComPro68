def format_string(*args):
    list_up = []

    for i in(args):
        uppers = i.upper().replace(" ","-")
        list_up.append(uppers)
    
    result = "".join(list_up)
    return (result)

print(format_string("Hello","Kewvy"))