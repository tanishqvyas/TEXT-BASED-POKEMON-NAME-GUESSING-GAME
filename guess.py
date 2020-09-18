import random as r
import sys
import os
import random
import time

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
				print("1 LIFE LOST     LIVES REMAINING : ","❤ "*life)
				play(word,length,visual_list)			
			
		else:
			print("PLEASE ENTER ONLY ONE WORD AT A TIME and DO NOT ENTER NUMBERS OR SPECIAL CHARACTERS")
			play(word,length,visual_list)
		print()
		print("LIVES REMAINING : ", "❤ "*life)
		if visual_list.count("_ ") == 0:
			time.sleep(1)
			clearscreen()
			slow_type(" YOU WIN !! CONGRATULATIONS ",s=0.2)
			time.sleep(1)
			menu()

	if life == 0:
		clearscreen()
		slow_type("NO LIVES LEFT..........")
		print()
		print()
		slow_type("     Y O U    L O S E !!     ",s=0.2)
		time.sleep(1)
		print()
		menu()

def clearscreen():
	if os.name == 'nt':
		data = os.system('cls')
	else:
		data = os.system('clear')
	return data

def slow_type(x,s=0.15):
	'''
	X = The sentence you need to display in typewriter style
	s = the speed of typing
	'''
	for l in x:
		sys.stdout.write(l)
		sys.stdout.flush()
		time.sleep(random.random()*s)
	print()
	return

#GAMEPLAY FUNCTION

def play_preparation():
	global life
	word = r.sample(l,1)[0]
	length = len(word)
	print("LENGTH OF POKEMON's NAME : ",length)
	check_list = []
	visual_list = []
	for i in range(length):
		visual_list.append("_ ")
	print("_ "*length)
	print("❤ "*life)
	play(word,length,visual_list)

def menu():
	global life
	clearscreen()
	print()
	print("      MENU       ")
	print(" 1 PLAY")
	print(" 2 HOW TO PLAY")
	print(" 3 EXIT")
	print()
	choice = int(input("ENTER THE CHOICE 1 , 2  or 3  :  "))
	
	if choice == 1:
		clearscreen()
		life=7 
		play_preparation()
	elif choice == 2:
		clearscreen()
		slow_type("YOU WILL HAVE 7 LIVES.",s=0.1) 
		slow_type("THERE WILL BE A RANDOM WORD WHICH YOU HAVE TO GUESS LETTER BY LETTER.",s=0.1)
		slow_type("IF U GUESS IT CORRECTLY YOU WIN ELSE IF U RUN OUT OF LIVES YOU LOSE.",s=0.1)
		slow_type("AVOID ENTERING NUMBERS, UPPER CASE LETTERS OR SPECIAL CHARACTERS TO AVOID LOSING LIFE.",s=0.1)
		print()
		print()
		time.sleep(1)
		menu()
	elif choice == 3:
		clearscreen()
		slow_type("EXITING THE GAME.................",s=0.2)
		sys.exit()

clearscreen()
slow_type("    WELCOME TO THE POKEMON NAME GUESSING GAME    ",s=0.22)
menu()   #CALLING THE MENU FUNCTION TO DISPLAY MENU
