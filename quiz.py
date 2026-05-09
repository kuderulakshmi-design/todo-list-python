score = 0

print("Welcome to Quiz Game!")

answer = input("What is the capital of India? ")

if answer == "Delhi":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

answer = input("Which language are we learning? ")

if answer == "Python":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

print("Your final score is:", score)
