Heroes = {
    "AAA" : "Starlord",
    "AAB" : "Drax",
    "ABA" : "Black Panther",
    "ABB" : "Doctor Strange",
    "BAA" : "Winter Soldier",
    "BAB" : "Rocket Raccoon",
    "BBA" : "Captain America",
    "BBB" : "Iron Man",
    "CAA" : "Groot",
    "CAB" : "Hulk",
    "CBA" : "Spiderman",
    "CBB" : "Mantis",
    "DAA" : "Thanos",
    "DAB" : "Thor",
    "DBA" : "Hawkeye",
    "DBB" : "Black Widow"
}

name = input("Hello, what is your name? ")
answer = input("Hello " + name + "! Ready to play? Y or N. " )

if answer.upper() == "Y":
  question1 = input("What color do you prefer?(Choose A or B) \nA) Blue \nB) Red \n")
  question2 = input("What sport do you prefer?(Choose A or B) \nA) Tennis \nB) Baseball \n")
  question3 = input("What dessert do you prefer?(Choose A or B) \nA) Cake \nB) Cookies \n")
  choice = question1 + question2 + question3
  wait = input("Are you ready to know what Marvel Hero you are most like?Y or N")
  if wait.upper() == "Y":
    print("Your Marvel Hero is " + Heroes[choice.upper()])
  else:
    print("Okay, suit yourself")
else:
  print("Oh that's too bad. Come back again later.")

  
