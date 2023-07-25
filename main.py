#Rock, Paper, Scissors

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
import time

print(''' 

                  ,--.    ,--. 
                 ((O ))--((O )) 
               ,'_`--'____`--'_`. 
              _:  ____________  :_ 
             | | ||::::::::::|| | |
             | | ||::::::::::|| | | 
             | | ||::::::::::|| | | 
             |_| |/__________\| |_| 
               |________________| 
            __..-'            `-..__ 
         .-| : .----------------. : |-. 
       ,\ || | |\______________/| | || /. 
      /`.\:| | ||  __  __  __  || | |;/,'\ 
     :`-._\;.| || '--''--''--' || |,:/_.-': 
     |    :  | || .----------. || |  :    | 
     |    |  | || '----GH----' || |  |    | 
     |    |  | ||   _   _   _  || |  |    | 
     :,--.;  | ||  (_) (_) (_) || |  :,--.; 
     (`-'|)  | ||______________|| |  (|`-') 
      `--'   | |/______________\| |   `--' 
             |____________________| 
              `.________________,' 
               (_______)(_______) 
               (_______)(_______) 
               (_______)(_______) 
               (_______)(_______) 
              |        ||        | 
              '--------''--------' 
 
''')
game_images = [rock, paper, scissors]


print("Hello. This program will allow you to play Rock, Paper, Scissors against this bot.")
time.sleep(1)
player_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. \n"))
if player_input >= 3 or player_input < 0:
  print('''

     ,;,'.`,''.`.':.
    .'.` ; ;. `'` .``.
     ; ;`  ` ` ;` ``:
     ':,`:`.`:~..`.;'
          :.:.|
         _:..:|_
        `-|___:-'
          : .:|
    __.=~'=___=`~=.__
        `~~~~~~~'
''')
  print("You typed an invalid number so you spontaneously combusted. You lose!")
else:
  print(f"You chose: {player_input}")
  print(game_images[player_input])
  
  computer_choice = random.randint(0, 2)
  print(f"Computer chose: {computer_choice}")
  print(game_images [computer_choice])
  
  
  if player_input == 0 and computer_choice == 2:
    print("You win!")
  elif computer_choice == 0 and player_input == 2:
    print("You lose!")
  elif computer_choice > player_input:
    print("You lose.")
  elif player_input > computer_choice:
    print("You win!")
  elif compute_choice == player_input:
    print("It's a draw.")
  else:
    print('''

     ,;,'.`,''.`.':.
    .'.` ; ;. `'` .``.
     ; ;`  ` ` ;` ``:
     ':,`:`.`:~..`.;'
          :.:.|
         _:..:|_
        `-|___:-'
          : .:|
    __.=~'=___=`~=.__
        `~~~~~~~'
''')
    print("You typed an invalid number so you spontaneously combusted. You lose!")
