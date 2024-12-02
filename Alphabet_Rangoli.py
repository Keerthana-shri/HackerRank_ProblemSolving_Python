def print_rangoli(size):
    alphbets = "abcdefghijklmnopqrstuvwxyz"
    total_size = ((4*size)-3)
    
    for i in range(1, size+1):
        alpha_string = ""
        for j in range(i):
            letter = alphbets[size-i+j]
            alpha_string = alpha_string.center((2*j+1), letter)
        alpha_string_hiphen = "-".join(alpha_string)
        print(alpha_string_hiphen.center(total_size, "-"))
    for i in range(size-1, 0, -1):
        alpha_string = ""
        for j in range(i):
            letter = alphbets[size-i+j]
            alpha_string = alpha_string.center((2*j+1), letter)
        alpha_string_hiphen = "-".join(alpha_string)
        print(alpha_string_hiphen.center(total_size, "-"))