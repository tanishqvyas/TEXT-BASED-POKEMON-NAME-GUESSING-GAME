import random as r
import sys


l = ["gyarados","victreebell","rayquaza","venusaur","blastoise","vaporeon","charizard","garchomp"]
life = 7

def play(word,length,visual_list):
	global life
	
	while life > 0:
		chance = input("ENTER A LETTER : ")
		if len(chance) == 1:
			if chance in word:
				for i in range(len(word)):
					if word[i] == chance:
						visual_list[i] = word[i]
				for i in range(len(word)):
					print(visual_list[i],end="")
						
			else:
				print("THE ENTERED LETTER IS NOT IN WORD")
				life -= 1
				print()
				print("1 LIFE LOST     LIVES REMAINING : ","❤"*life)
				play(word,length,visual_list)			
			
		else:
			print("PLEASE ENTER ONLY ONE WORD AT A TIME and DO NOT ENTER NUMBERS OR SPECIAL CHARACTERS")
			play(word,length,visual_list)
		print()
		print("LIVES REMAINING :", "❤"*life)
		if visual_list.count("_ ") == 0:
			print()
			print(" YOU WIN !! CONGRATULATIONS ")
			menu()

	if life == 0:
		print("NO LIVES LEFT..........Y O U    L O S E !! ")
		print()
		menu()


#GAMEPLAY FUNCTION

def play_preparation():
	global life
	word = r.sample(l,1)[0]
	length = len(word)
	print("LENGTH OF POKEMON's NAME :",length)
	check_list = []
	visual_list = []
	for i in range(length):
		visual_list.append("_ ")
	print("_ "*length)
	print("❤"*life)
	play(word,length,visual_list)




def menu():
	print()
	print("      MENU       ")
	print(" 1 PLAY")
	print(" 2 HOW TO PLAY")
	print(" 3 EXIT")
	print()
	choice = int(input("ENTER THE CHOICE 1 , 2  or 3  :  "))
	
	if choice == 1:
		play_preparation()
	elif choice == 2:
		print(" YOU WILL HAVE 7 LIVES. THERE WILL BE A RANDOM WORD WHICH YOU HAVE TO GUESS LETTER BY LETTER. IF U GUESS IT CORRECTLY YOU WIN ELSE IF U RUN OUT OF LIVES YOU LOSE. AVOID ENTERING NUMBERS,UPPER CASE LETTERS OR SPECIAL CHARACTERS TO AVOID LOOSING LIFE.")
		print()
		print()
		menu()
	elif choice == 3:
		print("EXITING THE GAME.................exit")
		sys.exit()


print("    WELCOME TO POKEMON NAME GUESSING GAME ")

menu()   #CALLING THE MENU FUNCTION TO DISPLAY MENU
