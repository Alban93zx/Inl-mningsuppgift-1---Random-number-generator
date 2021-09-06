
import random

def main():
    

    guessesTaken = 0

    print('Hello, what is your name?')
    myName = input()

    number = random.randint(1, 10)
    print( myName + ', Guess a number between 1 - 10')

    while guessesTaken < 100:
        print('Take a guess or exit the game by typing: Exit')
        guess = input()

        try:
            guess = int(guess)
        except:
            if guess == 'Exit':
                break
            else:
                print('Please enter a number!')
                continue

        guessesTaken = guessesTaken + 1


        if guess < number:
            print('Your guess is too low.')

        if guess > number:
            print('Your guess is too high.')

        if guess == number:
            break
        
    if guess == number:
        guessesTaken = str(guessesTaken)
        print(myName + '! You guessed the number in ' + guessesTaken + ' guesses!')
        
    if guess != number:
        number = str(number)
        print('Nope. The number I was thinking of was ' + number)
    
    with open("Highscore.txt", 'a') as file:
        file.write('\n' + guessesTaken  + '-' + myName)



def print_highscore():
    with open("Highscore.txt", "r") as file:
        for line in file:
            print (line)
        


if __name__ == "__main__":
    while True:
        main()
        while True:
            answer = str(input('Run again? (y/n) or p to print Highscore: '))
            if answer in ('y','n','p'):
                break
            print('invalid input')
        if answer == 'y':
            continue
        if answer == 'p':
            print_highscore()
            break
        else:
            print('Goodbye!')
            exit()



