import time
import logging
import datetime
from venv import create
import csv
import os
import pandas as pd

logging.basicConfig(filename="gitsawLog.log", level=logging.DEBUG)

# data = {
#     'col1': [10, 20, 30],
#     'col2': ['A', 'B', 'C']
# }

# print(data)

# df = pd.DataFrame(data)

# print(df.to_json())
# df.to_json('example_json.json')

# example_dictionary = {'name': ["Rich", "Ollie", "Chris", "Zakiya", "Ben", "Steph", "Gabe"],
# 'age (guess)': [35, 29, 37, 24, 37, 24, 24],
# 'designation': ["Head of US", "Head Teach", "DataHead", "Talent", "Instructor", "A. Instructor", "A. Instructor"]}

# df = pd.DataFrame(example_dictionary)

# print(example_dictionary)

# print(" ")

# print(df)

# df.to_csv('csv_example.csv', index=False)

# df_csv = pd.read_csv('csv_example.csv')

# print(df_csv)


# headers = ['Name', 'age (guess)']
# data = [['Alex', 25], ['Brad', 30], ['Joey', 18]]

# with open('prey.csv', mode='w', newline='') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=headers)

#     writer.writeheader()
#     for student in data:
#         writer.writerow({'Name': student[0], 'age (guess)': student[1]})

# rows = []
# with open('prey.csv', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     print(["Name"], ["email"])
#     for row in reader:
#         print(row["Name"], row["email"])

# header = ['Name', 'age', 'location']
# data = [['Alex', 25, 'usa'], ['Brad', 30, 'canada'], ['Joey', 10, 'australia']]
# with open ('git_saw.csv', mode='w', newline='') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerow(header)
#     csvwriter.writerows(data)

# rows = []
# with open('prey.csv', newline='') as csvfile:
#     csvreader = csv.reader(csvfile)
#     header = next(csvreader)
#     for row in csvreader:
#         rows.append(row)

# print(f"The headers are: {header}")
# print(rows)
# print("current directory: ", os.getcwd())
# os.mkdir("mydir")

# os.chdir("mydir")
# os.remove("newfile.text")
# os.rename("myfile.text", "newfile.text")

# with open("myfile.text", mode="w", encoding="utf-8") as my_file:
#     my_file.write("Some text\nMore text\nEven more\nMOAR")

# with open("myfile.text", encoding="utf-8") as my_file:
#     print(my_file.read())

#     print(my_file.name)
#     print(my_file.mode)
# with open("newfile.text", encoding="utf-8") as my_file:
#    line_num = 1
#    while True:
#        line = my_file.readline()
#        if not line:
#            break
#        print("Line # : ", line_num, "|", line, end="")
#        line_num += 1


class Player:
    def __init__(self, name, turns):
        self.name = name
        self.turns = turns

    def checkTurns(self, turns):
        if turns <= 0:
            print("Times run out. Game Over")
            logging.info("No more lives. Your Times Up")
            time.sleep(3)
            create_csv()
            quit()


def create_csv():
    with open('gitsawLog.log') as file:
        lines = file.read().splitlines()
        lines + [lines[x:x+3]for x in range(0, len(lines), 3)]

    with open('gitsawLog.csv', 'w+') as csvfile:
        w = csv.writer(csvfile)
        w.writerows(lines)


def introduction():
    global start_game
    start_game = datetime.datetime.now()
    logging.info(f"Waking up at the bottom of a tub {start_game} ")
    print("..::....::....::....::....::....::....::....::....::....::....::....::....::..")
    print("..:                                                                        :..")
    print("..:  Rise and shine. You're probably wondering where you are. I'll tell    :..")
    print("..:  you where you might be. You might be in the room that you die in. Up  :..")
    print("..:  until now you simply sat in the shadows watching others live out      :..")
    print("..:  their lives. But what do voyeurs see when they look into the mirror?  :..")
    print("..:  Now, I see you as a strange mix of someone angry, yet apathetic. But  :..")
    print("..:  mostly just pathetic. So are you going to watch yourself die today or :..")
    print("..:  do something about it?                                                :..")
    print("..:                                                                        :..")
    print("..::....::....::....::....::....::....::....::....::....::....::....::....::..")
    choice = input("Make your choice (live or die) ")
    print("                                                                              ")
    newPlayername = input("Enter Your Name If You Dare ")
    global newPlayer
    newPlayer = Player(newPlayername, 10)
    choice = input(f"Want to play a game?  {newPlayer.name}? Yes or No ")
    print("                                                                              ")
    if choice.lower() == 'yes':
        logging.info(f"Let The Game Begin {datetime.datetime.now()}")
        the_tub()
    elif choice.lower() == 'no':
        print("Times running out! Press enter if you want live. ")
        choice = input("")
        logging.info(f"Let The Game Begin {datetime.datetime.now()}")
        the_tub()
    else:
        choice = input("Type 'yes' or 'no'. ")
        if choice.lower() == 'yes':
            logging.info(f"Let The Game Begin {datetime.datetime.now()}")
            the_tub()
        elif choice.lower() == 'no':
            print("Times running out! Press any key to proceed. ")
            choice = input("")
            logging.info(f"Let The Game Begin {datetime.datetime.now()}")


def the_tub():
    print("..::....::....::....::....::....::....::....::....::....::....::....::....::..")
    print("..:                                                                        :..")
    print("..:  Waking up at the bottom of the tub, your eyes open as you struggle    :..")
    print("..:   to breath. You are confused as to how you ended up here.             :..")
    print("..:       What will you do next? Times running out... Make your choice!    :..")
    print("..:                                                                        :..")
    print("..::....::....::....::....::....::....::....::....::....::....::....::....::..")
    print("                                                                              ")
    choice = input("Sit Up and Grasp for Air(x) or Lay There(y) [type x or y]")
    print("                                                                              ")
    if choice.lower() == 'x':
        logging.info(
            f"You Have Chosen DEATH!!! GOODBYE {datetime.datetime.now()}")
        chain_leg()
        newPlayer.turns == 10
        logging.info(f"{newPlayer.name} ends with {newPlayer.turns} turns.")
        end_game = datetime.datetime.now()
        logging.info(f"The Game took {end_game - start_game} time.")
        create_csv()
        print("..::....::....::....::....::....::....::....::....::....::....::...::..:..")
        print("..:                                                                    :..")
        print("..:     No one's here to help you value your life. Just remember, you  :..")
        print("..:         made your choice. Game Over                                :..")
        print("..:                                                                    :..")
        print("..::....::....::....::....::....::....::....::....::....::....::....::.:..")
    elif choice.lower() == 'y':
        choice = input("Want to Play Again? ")
        print("                                                                          ")
        introduction()


def chain_leg():
    print("..::....::....::....::....::....::....::....::....::....::....::...::..:..")
    print("..:                                                                    :..")
    print("..:   At this very moment, you decided to fight for life. While still  :..")
    print("..:   in a panic, you notice one of your legs are chained to a pole.   :..")
    print("..:   There's also a tape recorder lying in the middle of the floor.   :..")
    print("..:      Choose to PLAY the tape or Suffer the consequences!           :..")
    print("..::....::....::....::....::....::....::....::....::....::....::....::.:..")
    print("                                                                          ")
    choice = input("Play or Suffer? ")
    print("                                                                          ")
    if choice.lower() == 'play':
        logging.info(
            f"You choose to play the tape recorder{datetime.datetime.now()}")
        time.sleep(1)
        newPlayer.turns == 1
        newPlayer.checkTurns(newPlayer.turns)
        tape_of_clues()
    elif choice.lower() == 'suffer':
        logging.info(
            f"You choose to suffer all alone {datetime.datetime.now()}")
        time.sleep(1)
        newPlayer.turns == 1
        newPlayer.checkTurns(newPlayer.turns)
        suffer_alone()
    else:
        print("Type 'play' or 'suffer' ")
        if choice.lower() == 'play':
            logging.info(
                f"You choose to play the tape recorder at {datetime.datetime.now()}")
        elif choice.lower() == 'suffer':
            logging.info(
                f"You choose to suffer all alone {datetime.datetime.now()}")
            time.sleep(1)
            newPlayer.turns == 1
            newPlayer.checkTurns(newPlayer.turns)
            suffer_alone()
        else:
            print("Please type a or b ")
            print(
                "                                                                          ")
            choice = input("a or b ")
        if choice.lower() == 'b':
            logging.info(f"Game Over at {datetime.datetime.now()}")
            end_game = datetime.datetime.now()
            logging.info(f"{end_game}")
            choice = input("Want to Play Again? [type 'yes' or 'no'] ")
            print("                                                                    ")
            introduction()


def suffer_alone():
    print("..::....::....::....::....::....::....::....::....::....::....::....::....::..")
    print("..:                                                                        :..")
    print("..: The human body is a fascinating organism. It can withstand the         :..")
    print("..: most brutal injury... and yet repair itself miraculously. But          :..")
    print("..: you know this all too well. How many broken bones have you suffered    :..")
    print("..: at the hands of others? How many flesh wounds have you endured?        :..")
    print("..: With time, the bruises have healed, but your pain has not. Today, I    :..")
    print("..: empower you to take control of your life. Can you disconnect from the  :..")
    print("..: one thing that has brought you and others so much pain? With time,     :..")
    print("..: your wounds will heal. However, others won't. Remove the ties that     :..")
    print("..: bind... or bleed to death from your inactivity. The choice is yours.   :..")
    print("..:                                                                        :..")
    print("..::....::....::....::....::....::....::....::....::....::....::....::....::..")
    print("                                                                              ")
    choice = input("Saw Your Foot Off or Search For A Key ")
    print("                                                                              ")
    if choice.lower() == 'saw':
        logging.info(
            f"You choose to saw your foot off {datetime.datetime.now()}")
        print(
            "..::....::....::....::....::....::....::....::....::....::....::....::....::..")
        print(
            "..:   Oh no! You sawed your foot off and bleed to death!                   :..")
        print(
            "..::....::....::....::....::....::....::....::....::....::....::....::....::..")
        # time.sleep(1)
        # newPlayer.turns -= 1
        # newPlayer.checkTurns(newPlayer.turns)
        introduction()
    elif choice.lower() == 'key':
        logging.info(
            f"Listen to the tape to find the key {datetime.datetime.now()} ")
        # time.sleep(1)
        tape_of_clues()
    else:
        print("Type 'saw' or 'key' ")
        print(
            "                                                                              ")
        choice = input("saw or key? ")
        logging.info(
            f"You choose to saw off your foot {datetime.datetime.now()}")
        if choice.lower() == 'saw':
            time.sleep(1)
            newPlayer.turns -= 1
            newPlayer.checkTurns(newPlayer.turns)
            chain_leg
        elif choice.lower() == 'key':
            logging.info(
                f"You choose to play the tape {datetime.datetime.now()}")
            time.sleep(1)
            tape_of_clues()


def tape_of_clues():
    print("..::....::....::....::....::....::....::....::....::....::....::....::....::..")
    print("..:                                                                        :..")
    print("..:   If you're listening to this tape, I assumed you believed you would   :..")
    print("..:   find a key to break away from those chains.  You had the key wrapped :..")
    print("..:   around your toe until it washed down the drain. You of all people    :..")
    print("..:   should know there are no short cuts to life. Try to reach and        :..")
    print("..:   pull the handle on the wall and you will be set free!                :..")
    print("..:                                                                        :..")
    print("..::....::....::....::....::....::....::....::....::....::....::....::....::..")
    choice = input(
        "Pull the handle or search for options? [type 'handle' or 'options' ")
    print("                                                                              ")
    if choice.lower() == 'handle':
        logging.info(
            f"You chose to pull the handle to escape {datetime.datetime.now()}")
    print("..:  Pull the handle and free yourself! Beware of the blades :..")
    time.sleep(1)
    newPlayer.turns -= 1
    newPlayer.checkTurns(newPlayer.turns)
    the_handle()

    if choice.lower() == "options":
        logging.info(
            f"You chose to look for other options to escape {datetime.datetime.now()}")

        print("..::....::....::....::....::....::....::....::....::....::....::....::....::....")
        print("..:                                                                          :..")
        print("..:Time's Up! You Played a Good Game but Not Good Enough to Value Your Life! :..")
        print("                                                                                ")
        time.sleep(1)
        suffer_alone()
    else:
        print("Type 'options' or 'handle' ")
        print("                                                                                ")
        choice = input("options or handle? ")
    if choice.lower() == 'handle':
        logging.info(
            f"You choose to reach for the handle {datetime.datetime.now()}")
        time.sleep(1)
        newPlayer.turns -= 1
        newPlayer.checkTurns(newPlayer.turns)
        suffer_alone()
    elif choice.lower() == 'options':
        logging.info(
            f"You choose to look for other options to escape {datetime.datetime.now()}")
        print("..::....::....::....::....::....::....::....::....::....::....::....::....::....")
        print("..:                                                                          :..")
        print("..:Time's Up! You Played a Good Game but Not Good Enough to Value Your Life! :..")
        print("..:                                                                          :..")
        print("..::....::....::....::....::....::....::....::....::....::....::....::....::....")
        print("                                                                                ")
        time.sleep(1)
        suffer_alone()
    else:
        print("Type 'option' or 'handle' ")
        if choice.lower() == 'handle':
            logging.info(
                f"You choose to reach for the handle {datetime.datetime.now()}")
            time.sleep(1)
            newPlayer.turns -= 1
            newPlayer.checkTurns(newPlayer.turns)
            suffer_alone()
        elif choice.lower() == 'options':
            logging.info(
                f"You choose to look for other options to escape {datetime.datetime.now()}")
            print(
                "..::....::....::....::....::....::....::....::....::....::....::....::....::....")
            print(
                "..:                                                                          :..")
            print(
                "..:Time's Up! You Played a Good Game but Not Good Enough to Value Your Life! :..")
            print(
                "..:                                                                          :..")
            print(
                "..::....::....::....::....::....::....::....::....::....::....::....::....::....")
            print(
                "                                                                                ")
            # time.sleep(1)
            introduction()


def the_handle():
    print("..::....::....::....::....::....::....::....::....::....::....::....::....::....")
    print("..:                                                                          :..")
    print("..:  Reach out and pull the switch, but beware of the spinning blades!       :..")
    print("..:         Will you pull the switch or saw your foot off to escape?         :..")
    print("..:                                                                          :..")
    print("..::....::....::....::....::....::....::....::....::....::....::....::....::....")
    choice = input(
        "Saw Off Your Foot or Try to Reach for the Switch  [type 'foot' or 'switch'] ? ")
    print("                                                                                ")
    if choice.lower() == 'switch':
        logging.info(
            f"You chose to reach for the switch while blades are spinning")
        print("..::....::....::....::....::....::....::....::....::....::....::....::....::....")
        print("..:                                                                          :..")
        print("..:  Obssession has stopped those around you from making the wrong choices   :..")
        print("..:  No one will stop you from making the wrong choice. Time's run out!      :..")
        print("..:  You value Obssession more than life! Game Over!                         :..")
        print("..:                                                                          :..")
        print("..::....::....::....::....::....::....::....::....::....::....::....::....::....")
        choice = input("Want to Play Again? [type 'yes' or 'no'] ")
        print("                                                                                ")
        # time.sleep()
        # newPlayer.turns -= 1
        # newPlayer.checkTurns(newPlayer.turns)
        introduction()
    elif choice.lower() == "foot":
        logging.info(
            f"You chose to saw your foot off to escape {datetime.datetime.now()}")
        print("..::....::....::....::....::....::....::....::....::....::....::....::....::....")
        print("..:                                                                          :..")
        print("..:                          Clever! Clever!                                 :..")
        print("..:             You've figured out what it takes to value life.              :..")
        print("..:                 Lesson Learned... Won't You Agree!                       :..")
        print("..:                                                                          :..")
        print("..::....::....::....::....::....::....::....::....::....::....::....::....::....")
        choice = input("Want to Play Again? [type 'yes' or 'no'] ")
        print("                                                                                ")
        # time.sleep(1)
        introduction()
    else:
        print("Game Over Hit 'enter' to Start A New Game")
        choice = input("")
        introduction()


introduction()
the_tub()
chain_leg()
suffer_alone()
tape_of_clues()
the_handle()
quit()
