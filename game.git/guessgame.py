
print('Welcome to game')
print('please Select the level')
print('''
         1. EASY
         2. NORMAL
         3. HARD''')
d = int(input("Enter the Numm: "))

if d == 1:
    import easy
    easy.guess_num_easy()
    input()
    
elif d == 2:
    import normal

    normal.guess_num_normal()
    input()
elif d == 3:
    import hard

    hard.guess_num_hard()
    input()
