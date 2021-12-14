#quiz game of three question

print("Welcome to the Game!")

print("that's your name")

name = input("Type your name: ")

print("hello " + name)

start = input("For starting type s ")


if start == "s":
        print("the game beggin")

print("what is the capital of india?")

answer1 = input("type the the answer in small letters: ")

if answer1 == "delhi":
        print("correct answer")
        print("next question")
else:
        print("wrong answer")
        print("next question")


print("what is the capital of kerala")

answer2 = input("type t if answer is tiruvantapuram type k if answer kannur")

def answer22():
        if answer2 == "t":
                print("correct answer")
                print("next question")

        elif answer2 == "k":
                print("wrong answer")
                print("next question")

answer22()

print("which state Chief Minister is pinarayi vijayan?")

answer3 = input("type g if goa | type o if orisa | type k if kerala: ")

def answer33():

        if answer3 == "g":
                print("wrong answer")
                print("next question")

        elif answer3 == "o":
                print("wrong answer")
                print("wrong answer")

        elif answer3 == "k":
                print("correct answer")
                print("next question")

answer33()

