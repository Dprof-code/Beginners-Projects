# This program is a quiz program
print("This is a quiz session")
print("You are to choose the odd word")
words1 = ["Buy", "Sell", "Scam", "Eat"]
words2 = ["Java", "Python", "Javascript", "Css"]
# noinspection SpellCheckingInspection
words3 = ["Samsung", "Itel", "Lexus", "Tecno"]
print(words1)
answer_words1 = input("Which word is the odd one among the above list of words?\n")
if answer_words1 == "Eat":
    print("You are correct")
else:
    print("You are wrong")
print(words2)
answer_words2 = input("Which word is the odd one among the above list of words?\n")
if answer_words2 == "Css":
    print("You are correct")
else:
    print("You are wrong")
print(words3)
answer_words3 = input("Which word is the odd one among the above list of words?\n")
if answer_words3 == "Lexus":
    print("You are correct")
else:
    print("You are wrong")
if answer_words1 == "Eat" and answer_words2 == "Css" and answer_words3 == "Lexus":
    print("You answered everything correctly")
    print("You had an excellent score, You are brilliant")
elif answer_words1 == "Eat" and answer_words2 == "Css" and not answer_words3 == "Lexus":
    print("You answered only two correctly")
    print("You have a good score")
elif not answer_words1 == "Eat" and answer_words2 == "Css" and answer_words3 == "Lexus":
    print("You answered only two correctly")
    print("You have a good score")
elif answer_words1 == "Eat" and not answer_words2 == "Css" and answer_words3 == "Lexus":
    print("You answered only two correctly")
    print("You have a good score")
elif not answer_words1 == "Eat" and not answer_words2 == "Css" and not answer_words3 == "Lexus":
    print("You answered all wrongly")
    print("You have a poor score")
