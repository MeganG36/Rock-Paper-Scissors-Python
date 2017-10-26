import random;
player = input("Enter your choice (rock/paper/scissors): ");
while (player != "rock" and player != "paper" and player != "scissors"):
	print(player);
	player = player.lower();
computerInt = random.randint(0,2);
if (computerInt == 0):
    computer = "rock";
elif (computerInt == 1):
	computer = "paper";
elif (computerInt == 2):
	computer = "scissors";
else:
	computer = "Huh? Try again...";
if (player == computer):
	print("It's a tie!");
elif (player == "rock"):
	if (computer == "paper"):
		print("Sorry, You Lose.");
	else:
		print("You win!");
elif (player == "paper"):
	if (computer == "rock"):
		print("You win!");
	else:
		print("Sorry, You Lose.")
elif (player == "scissors"):
	if (computer == "rock"):
		print("Sorry, You Lose.");
	else:
		print("You win!");


