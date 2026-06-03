print(r'''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |          
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|

           {}           {}
         \  _---_  /
          \/     \/
           |() ()|
            \ + /
ejm 96     / HHH  \
          /  \_/   \
        {}          {}
''')
print("Welcome to the treasure island!")
print("IT`S EITHER DO OR DIE! HAHAHAHA\n\n")
# Telling the requirements for the game
print("Your goal is to find the TREASURE full of gold coins and valuable things.")
map_choice = ""  # initialize here
treasure = input("Do you wanna see the treasure chest first (y or n) ?").lower()
if treasure == "y":
    print(r'''
                      .--------------------------------...
               ,'-------------------------------,'   |
              /                                /     |
             /________________________________/    ,'|
             |               ..               |  ,'  |
             |___________-==/88\==-___________|,' /) |.
             |  \    \     ((  ))     /    /  |  (/  |-. .
             |   \    \     \{}/     /    /   |    .' .  .
          . '|    \    \     )(     / _  /    |    ,   .  .
         . . |\    \    \    \/    _.( ~-.   /|\ ,' .   . .
       ` .  -`_-.--.______..._____( ,/  ` \~-.|,' .   .
        .  `    .     .       .  ,'\. ~-  . , .  .  .   .
           .  `   .     ,   .      , ~~-.' .  .    .

 ''')
else:
    print("It`s totally okay if you didn`t wanna see the wholesome treasure chest ")

ready = input("Are you ready (Yes or No) ?\n").capitalize()
if ready == "Yes":
    map_choice = input("Do you wanna see the map too (YES or NO) ?").upper()
if map_choice == "YES":
    print(" This is the TREASURE map !!!")
    print(r'''
      ____________________________________________________________________
     / \-----     ---------  -----------     -------------- ------    ----\
     \_/__________________________________________________________________/
     |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
     |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
     | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
     |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
     |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
     |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
     |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
     |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
     | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
     |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
     |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
     | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
     |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
     | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
     |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
     | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
     |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
     | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
     |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
     |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
     / \----- ----- ------------  ------- ----- -------  --------  -------\
     \_/__________________________________________________________________/
    ''')

else:
    print("\nYou are out from the game ")
    raise SystemExit

# real game begins here
direction = input("In which direction you would like to go (Left or Right ) ?").lower()
if direction == "left":
    print("WOHOOO You cleared that path.\n")
    second_step = input(
        " Now next now tell me are you going to SWIM or WAIT in order to reach that treasure chest ?\n(SWIM or WAIT)=>").upper()
else:
    print("You got eaten by wild animals\n")
    print("GAME OVER\n")
    raise SystemExit
# now to the next path
if second_step == "WAIT":
    print(r'''
                   ________
              / ______ \
              || _  _ ||
              ||| || |||
              |||_||_|||
              || _  _o|| (o)
              ||| || |||
              |||_||_|||      ^~^  ,
              ||______||     ('Y') )
             /__________\    /   \/
     ________|__________|__ (\|||/) _________
    hjw     /____________\
    `97     |____________|
     ''')

    door = input("Choose one DOOR to reach to the end (red,yellow,blue)?").lower()
else:
    print("You SWAM into the ocean and got lost !!")
    print("GAME OVER ")
    raise SystemExit

if door == "yellow":
    print("YAYAYAYAYA YOU WON !!!!!!!!!")
    print(r'''
                                                   888            
                                               888            
                                               888            
 .d8888b .d88b. 88888b.  .d88b. 888d888 8888b. 888888.d8888b  
d88P"   d88""88b888 "88bd88P"88b888P"      "88b888   88K      
888     888  888888  888888  888888    .d888888888   "Y8888b. 
Y88b.   Y88..88P888  888Y88b 888888    888  888Y88b.      X88 
 "Y8888P "Y88P" 888  888 "Y88888888    "Y888888 "Y888 88888P' 
                             888                              
                        Y8b d88P                              
                         "Y88P"                               

    ''')
chest = input("Excited to open the chest (Yes or No)?").capitalize()

if chest == "Yes":
    print(r'''
     _____.______.______._____
 \`\                   /'/
  \ |                 | /
   >|___,____,____,___|<
  /d$$$P ,ssssssssssss. \
 /d$$$P ,d$$$$$$$$$$$$$b \
<=====w======w======w=====>
 \ \____> \_____/ <____/ /
  \_____________________/ pb


    ''')
else:
    print("It`s Okay ")
    raise SystemExit
if door == "red":
    print("You died in the burning fire :(")
    print("Try again ")
    print("GAME OVER ")
    raise SystemExit

if door == "blue":
    print("You fell into the deep dark hole ")
    print("GAME OVER ")
    raise SystemExit

else:
    print("GAME OVER")
    print("Had fun! try again!")
    raise SystemExit

