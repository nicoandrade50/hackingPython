import random

def guess_number():


    secret_number = random.randint(1, 20)
    


    while True:


        guess = int(input("Guess the number (between 1 and 20): "))
        

        if guess == secret_number:
            print("Congratulations! You guessed the correct number.")
            break


        elif guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

if __name__ == "__main__":
    guess_number()
