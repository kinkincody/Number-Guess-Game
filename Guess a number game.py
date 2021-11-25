import random as rd

ans = rd.randint(1,101)

xl = 1
xh = 100

guess = int(input(f'Please guess a number between {xl} and {xh}: '))
count = 0
while not guess == ans:
    print(ans)
    if guess > ans:
        xh = guess
        guess = int(input(f'Please guess a number between {xl} and {xh}: '))
        count += 1
        
    elif guess < ans:
        xl = guess
        guess = int(input(f'Please guess a number between {xl} and {xh}: '))
        count += 1
        
    if guess == ans:
        count += 1
        print('Bingo')
        print(f'Number of attempt = {count}')