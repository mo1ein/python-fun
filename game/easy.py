def guess_num_easy():
        print("Guess the Num between 1 to 50")
        a = int(input("Enter the Num: "))
        list_num = [1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
        if a in list_num:
            print("congo!! you guessed the number")
            print("press any key to exit...")
            input()
        else:
            print("press E to  try again")
            b = input(": ")
            if b == 'e':
                guess_num_easy()
guess_num_easy()
