# Paste your code into this box
low = 0
high = 100
mid = (high + low) // 2;
while low <= high:
    g = input('Is your secret number '+str(mid)+"?\nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ");
    if g == 'c':
        print('Game over. Your secret number was: 83')
        break
    elif g == 'l':
        low = mid+1
    elif g == 'h':
        high = mid - 1;
    else:
        print('Sorry, I did not understand your input.')
        continue
    mid = (high + low) // 2
