"""
Description:

Mastermind is a code-breaking game for two players.
the code to guess consists of 4 digits from 1-6 (digits may repeat).
A hint for the player is the feedback on how many digits have been
guessed from the 4-digit code so far
"""

import random


# Function used to generating a list of 4 random numbers in range 1 to 6
def generate_secret_code():
    secret_code = []
    for i in range(4):
        secret_code.append(random.randint(1, 6))
    return secret_code


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    secret_list = generate_secret_code()
    # print(secret_list)

    print("\nLet's play a Mastermind game!")
    print("Try to guess the secret code with 4 numbers between 1 and 6.")

    correct = 0
    counter = 0

    # The while function that runs until all four digits are guessed
    while correct != 4:
        correct = 0

        number1 = int(input("\nPlease try to guess the first number: "))
        number2 = int(input("Please try to guess the second number: "))
        number3 = int(input("Please try to guess the third number: "))
        number4 = int(input("Please try to guess the fourth number: "))
        counter += 1

        if number1 == secret_list[0]:
            correct += 1
        if number2 == secret_list[1]:
            correct += 1
        if number3 == secret_list[2]:
            correct += 1
        if number4 == secret_list[3]:
            correct += 1

        if correct != 4:
            print("\nNot this time! You guessed {} number(s) from the secret code. You have to try once again.".format(correct))
        else:
            print("\nCongratulations! You win in {} step(s)!".format(counter))

"""
Result:

Let's play a Mastermind game!
Try to guess the secret code with 4 numbers between 1 and 6.

Please try to guess the first number: 6
Please try to guess the second number: 6
Please try to guess the third number: 6
Please try to guess the fourth number: 6

Not this time! You guessed 2 number(s) from the secret code. You have to try once again.

Please try to guess the first number: 6
Please try to guess the second number: 1
Please try to guess the third number: 6
Please try to guess the fourth number: 6

Not this time! You guessed 3 number(s) from the secret code. You have to try once again.

Please try to guess the first number: 6
Please try to guess the second number: 1
Please try to guess the third number: 6
Please try to guess the fourth number: 2

Congratulations! You win in 3 step(s)!
"""