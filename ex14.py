from sys import argv

#script, user_name = argv
#prompt = '>'

#print(f"Hi {user_name}, I'm the {script} script.")
#print("I'd like to ask you a few questions.")
#print(f" Do you like me {user_name}?")
#likes = input(prompt)

#print(f"Where do you live {user_name}?")
#lives = input(prompt)

#print("What kind of computer do you have?")
#computer = input(prompt)

#print(f"""
#Alright, so you said {likes} about liking me.
#You live in {lives}. Not sure where that is
#And you have a {computer} computer. Nice.
#""")

#Study Drills
# 1)Find out what the games Zork and Adventure were.
#-This is a text adventure games

#2) Change the prompt to something else entirely

script, user_name, food, drink = argv
prompt = '*'

print(f"Hi {user_name}")
print("Let's have a nice chat today.")
print(f" What brand is the best for {food}?")
brandreply = input(prompt)

print(f"Where do you buy {food}?")
foodreply = input(prompt)

print(f"Do you like to have {food} and {drink} together?")
fooddrinkreply = input(prompt)

print(f"What {drink} should I buy?")
drinkreply = input(prompt)

print(f"Anything else I should buy?")
buyreply = input(prompt)

print(f"""
Today I saw {user_name}. We talked about {food} and {drink} today.
{user_name} buys {food} from {foodreply}. {user_name} buys the {brandreply}
brand at {foodreply}. In regards to {food} and {drink} together {user_name}
said {fooddrinkreply}.
{user_name} also mentioned you should buy {drinkreply} for the {drink}
brand and for you to also buy {buyreply}."""
)
