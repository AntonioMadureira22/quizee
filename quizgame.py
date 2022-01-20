print("Welcome! This is the python quiz.")

play = input("Are you ready to take on the challenge and be a python champion? yes or no? ")

if play.lower() != "yes":
    quit()

print("Perfect! Let the challenge begin")
score = 0

answer = input("What is output for − max(''please help '') ")
if answer.lower() == "s":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is PEP 8? ")
if answer.lower() == "python enhancement proposal":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What are lists and tuples? ")
if answer.lower() == "sequence data types":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What pass in Python? ")
if answer.lower() == "null operation in python":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print ("You got " + str(score) + " questions correct!")
print ("You got " + str((score/4) * 100) + "%")
