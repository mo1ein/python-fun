def guess_num_hard():
    print("Guess the Num between 1 to 50")
    a = int(input("Enter the Num: "))
    list_num = [37]
    if a in list_num:
        print("congo!! you guessed the number")
        print("press any key to exit...")
        input()
    else:
        print("press E to  try again")

        b = input(": ")
        if b == 'e':
            guess_num_hard()
guess_num_hard()