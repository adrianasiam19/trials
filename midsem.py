height = input("How tall are you?")
height = int(height)

if height >=48:
    print("\nYou are tall enough to ride")
else:
    print("\nYou will be able to ride if you are a little older.")

    #input
number = input("Enter any number, and i will tell you if it is even or odd")
number = int(number)
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd")

    #dinnertable
dinner = input("How many people are you on a table?")
dinner = int(dinner)
if dinner >=8:
    print(f"\nYou will have to to wait for another table")
else:
    print(f"\nYour table is ready.")

    #while lopp
prompt = "\nTell me something, and i will repeat it back to you:"
prompt +="\nEnter 'quit' to end the program"

message = ""
while message  !='quit':
   message = input(prompt)
print(message)

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
 message = input(prompt)
 if message == 'quit':
   active = False
else:
 print(message)

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
 city = input(prompt)
 if city == 'quit':
      break
else:
 print(f"I'd love to go to {city.title()}!")


def get_formatted_name(first_name, last_name):
 """Return a full name, neatly formatted."""
 full_name = f"{first_name} {last_name}"
 return full_name.title()
musician = get_formatted_name('jimi,' 'hendrix')
print(musician)