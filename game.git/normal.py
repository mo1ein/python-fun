def guess_num_normal():
    print("Guess the Num between 1 to 50")
    a = int(input("Enter the Num: "))
    list_num = [1,11,31,37,41,43,47]
    if a in list_num:
        print("congo!! you guessed the number")
        print("press any key to exit...")
        input()
    else:
        print("press E to  try again")

        b = input(": ")
        if b == 'e':
            guess_num_normal()
guess_num_normal()