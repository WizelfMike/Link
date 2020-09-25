import json

M = ["man", "Man"]
F = ["vrouw", "Vrouw"]

print("Hello You! Mijn naam is Mikey Clarke")

print("Wie ben jij?")

Fullname = input()

print("Hello" + " " + Fullname)

print(" ")

print("Mag ik jou leeftijd weten?")

Age = input()

print(Age + " Huh? Mooie leeftijd!")

print(" ")


def dialoge(text,choice_type):
    print(text)
    if choice_type == "gender":
        choice = input()
        if choice in F :
            return "F"
        elif choice in M :
            return "M"
        else:
            print("kies man of vrouw graag")

gender = dialoge ("bent u een man of vrouw?", "gender")
if gender == "F":
    print("M'lady")
if gender == "M":
    print("sup man")


