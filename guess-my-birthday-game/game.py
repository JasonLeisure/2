from random import randint

name = input ("Hello, what is your name? ")

for guess_number in range(1, 6):

    month_number = randint(1, 12)
    year_number = randint(1800, 2022)

    print("Guess 1 :", name, "were you born in",
        month_number, "/" , year_number, "?")

    response = input("yes or no? ")

    if response == "yes":
        print("I am a good guesser!")
        exit()
    elif guess_number ==5:
        print("I'm gone. Bye.")
    else:
        print("Let me try again!")
