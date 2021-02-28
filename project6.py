# This program would help detect spam in a group
name = input("Enter your name: ")
msg = input("Make a post: ")
bot_reply = "You have spammed the group, You should be removed!"
if "money" in msg:
    print(bot_reply)
elif "business" in msg:
    print(bot_reply)
elif "buy" in msg:
    print(bot_reply)
elif "sex" in msg:
    print(bot_reply)
elif "fool" in msg:
    print(bot_reply)
else:
    print("Your post is approved")
    print(name + " made a post")
    print(msg)
