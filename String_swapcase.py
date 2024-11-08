def swap_case(s):
    n = ""
    for let in s:
        if let.isupper() == True:
            n+=(let.lower())
        else:
            n+=(let.upper())
    return n