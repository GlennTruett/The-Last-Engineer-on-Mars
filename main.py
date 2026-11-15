# Imports the rooms from the rooms.py file so that I don't have to change my code if I used just "import rooms"
from rooms import rooms 
# create inital variables for health, oxygen, and score
health = 0
oxygen = 0
score = 0
# Create variables for Easy difficulty the user's Health, oxygen of the colony, and the score.
ehealth = 100
eoxygen = 100
escore = 10
# create variables for Medium difficulty the user's health, oxygen of the colony, and the score.
mhealth = 100
moxygen = 75
mscore = 0
#create varibles for Hard difficulty the user's health, oxygen of the colony, and the score.
hhealth = 80
hoxygen = 50
hscore = 0
# creating a current location variable
currentLocation = "Main Control Room"
userName = "Joe"
controlRoomChoice = "A"
difficulty = "Easy"
batteryPower = 18
#Create a function to display the current statistics of the user
# This function will take the user's choice of difficulty and assign the appropriate starting stats
def difficulty_stats(health, oxygen, score, difficulty, batteryPower):

        if difficulty == "A":
         health = ehealth
         oxygen = eoxygen
         score = escore 
        elif difficulty == "B": 
                health = mhealth   
                oxygen = moxygen
                score = mscore
        elif difficulty == "C":
                health = hhealth
                oxygen = hoxygen 
                score = hscore
        return health, oxygen, score, difficulty, batteryPower
# This function takes the first level decision and updates the stats        
def update_stats(health, oxygen, score, difficulty, batteryPower):

    if      difficulty == "A":
                           health += 0
                           oxygen -= 5
                           score +=  10
    elif    difficulty == "B":
                           health += 5
                           oxygen -= 10
                           score += 5
    elif    difficulty == "C":
                              health -= 15
                              oxygen -= 20
                              score -= 5   
    return health, oxygen, score, difficulty, batteryPower
# this function when called will display the stats
def display_statistics(health, oxygen, score, batteryPower):
    
    print(f"Health: {health}%")
    print(f"Oxygen: {oxygen}%")
    print(f"Score {score}")
    print(f"Battery Power: {batteryPower}%")
# Create an adventure sim
#  First Let's display the title of the sim
def display_title():
    print("  \n\n    ")
    print("============================================================")
    print("          Let The Adventure Begin                          ")
    print("============================================================\n\n")
 #prints the title of the Game
    print("THE LAST ENGINEER ON MARS\n")
# Display the title of the adventure sim
display_title()
# Lets print out the introduction to the sim
# I will be using \n to create new lines
def display_introduction(userName):
    print("Introduction: The Red Silence \n\n")
    print("Mars — Sol 247, 03:17 Colony Time \n")
    # The user will now be asked for their name and it will be stored as the variable userName
    userName = input("What is your name?").strip()
    print (f"\n Welcome to Mars, {userName}.")
    # the user will have to press enter to continue this makes for a better user experience
    input("\nPress Enter To continue...")
    print("_" * 80)
    print("""You awaken to the sound of an emergency alarm.
    Red lights flash across your sleeping quarters. The ventilation fans have stopped, and the familiar hum of the
    colony's life-support equipment is gone.\n\n """)
    input("\n Press Enter to continue...")
    print("_" * 80)
    print(f"{userName}, you are the chief engineer of Ares Colony, humanity's first permanent settlement on Mars. The other six")
    print("colonists departed three days ago on a geological expedition to a nearby canyon. You stayed behind to")
    print("maintain the colony's equipment.\n\n")
    input("\n Press Enter to continue...")
    print("_" * 80)
    print("Now something has gone terribly wrong.")
    print("The colony's central computer displays a terrifying message:\n\n")
    input("\n Press Enter to continue...")
    print("_" * 80)
    print("\n\n")
    print("ARES COLONY--CRITICAL SYSTEM FAILURE\n")
    print("MAIN POWER: OFFLINE\n")
    print("BACKUP POWER: 18%\n")
    print("OXYGEN GENERATION: OFFLINE\n")
    print("COMMUNICATIONS: OFFLINE\n")
    print("COLONY AI: UNRESPONSIVE\n")
    print("CREW STATUS: UNKNOWN\n")
    input("\n Press Enter to continue...")
    print("_" * 80)
    print("\n\n")
    # A final message appears on the screen:
    print("WARNING: Multiple system failures detected. Cause unknown. Estimated survival time: 6 hours.\n")
    input("\n Press Enter to continue")
    print("_" * 80)
    #now let's print out many lines of text with only one print statement.
    print("""You grab your engineering toolkit and look toward the darkened corridor. 
    You are alone. 
    There is no rescue coming unless you can restore communications. 
    You are the last engineer on Mars. 
    And the colony's survival depends on what you do next. 
    """)
    return userName
#Now run the introduction
userName = display_introduction(userName)

# Now print out the game instructions for our user
def gameInstructions():
    print("""
    Game Directions\n 
    The game consists of 10 scenarios. Each scenario presents a problem and three possible actions: A, B, or C.
    You must make decisions to repair equipment, conserve resources, investigate failures, and restore the colony.\n
    Scoring System\n
    Your decisions will affect your mission score:\n
    +10 points: Excellent decision\n
    +5 points: Acceptable decision\n
    -5 points: Poor decision\n                                      
    Your health and the colony's oxygen reserves may also be affected by your decisions.
    Your final score will help determine the outcome of your mission.
    Choose carefully, Engineer. The survival of Ares Colony is in your hands.\n
    """) 
gameInstructions()

# the user choses the dificulty which only affects the initial stats of health, oxygen, and score
def choseDifficulty(health, oxygen, score, difficulty, batteryPower):
    difficulty = input("What level of difficulty do you choose A. Easy B. Medium. C. Hard ").strip().upper() 
    print("\n")
    while difficulty not in ("A", "B", "C"):
          print("Invalid difficulty. Please choose A, B, or C ")
          difficulty = input("What level of difficulty do you choose A. Easy B. Medium. C. Hard ").strip().upper()  
    #Now show the user the initial stats of Health, Colony Oxygen levels, and the score.
    print(f"\n{userName} your stats are as follows\n")
    health, oxygen, score, difficulty, batteryPower = difficulty_stats(health, oxygen, score, difficulty, batteryPower)
    display_statistics(health, oxygen, score, batteryPower)
    input("Press Enter to continue...")
    print("_" * 80)
    return health, oxygen, score, difficulty, batteryPower
#now run choseDifficulty
health, oxygen, score, difficulty, batteryPower = choseDifficulty(health, oxygen, score, difficulty, batteryPower)

#starts Level 1
def Level1(controlRoomChoice, health, oxygen, score, difficulty, batteryPower):
    print("""\n Level 1: Darkness in the Control Room

        Location: Ares Colony — Main Control Room

        The emergency lighting flickers as you enter the control room. The main reactor has shut down, leaving the colony dependent on\n its rapidly draining backup batteries.
        \nA diagnostic warning flashes across the central monitor.
        """)
    input("\n Press Enter to continue")
    print("_" * 80)
    print(f"""\n WARNING: MAIN POWER FAILURE

    BACKUP BATTERY: {batteryPower}%

    LIFE SUPPORT: EMERGENCY MODE """)
    print("""\n The colony's oxygen circulation system is operating at reduced capacity. Every minute without stable power brings the colony closer to disaster.

    You examine the engineering console. Three possible actions are available.
    """)

    print(""" What do you do?

    A. Inspect the main electrical distribution panel.

    Examine the electrical system, identify the source of the failure, and isolate any damaged components before attempting repairs.

    B. Activate the portable emergency generators.

    Restore temporary power to essential equipment while postponing the investigation of the main reactor failure.

    C. Immediately restart the main reactor.

    Attempt to restore full power without first investigating what caused the shutdown.""")
    # the user makes a choice input is saved and new stats are calculated and results are shown
    controlRoomChoice = input("\n Choose A. B. or C. ").strip().upper()
    while controlRoomChoice not in ("A", "B", "C"):
            print("Invalid choice. Please choose A, B, or C ")
            controlRoomChoice = input("\n Choose A. B. or C. ").strip().upper()
    input("\n Press Enter to continue")
    print("_" * 80)
    if controlRoomChoice == "A":
            batteryPower += 70
            print("""Excellent Decision

        You inspect the electrical distribution panel and discover a damaged power relay. After isolating the faulty circuit,

        you prevent additional electrical damage.

        Your careful investigation takes time, consuming some of the colony's remaining oxygen reserves.\n""")
            health, oxygen, score, difficulty, batteryPower = update_stats(health, oxygen, score, difficulty, batteryPower)
            display_statistics(health, oxygen, score, batteryPower)
    elif controlRoomChoice == "B":
            batteryPower += 40
            print("""Acceptable Decision

    You activate the portable emergency generators. Essential systems begin operating again, but fuel reserves are limited.

    Temporary power reduces the immediate danger, although the original electrical failure remains unresolved. """)
            health, oxygen, score, difficulty, batteryPower = update_stats(health, oxygen, score, difficulty, batteryPower)
            display_statistics(health, oxygen, score, batteryPower)
    elif controlRoomChoice == "C":
        batteryPower -= 10
        print(""" Poor Decision

    You initiate an emergency reactor restart without checking the electrical system.

    A damaged relay causes another electrical fault. Sparks erupt from a nearby control panel, and an electrical arc throws you backward.

    You suffer minor injuries, and the additional power failure accelerates the depletion of the colony's oxygen reserves.""") 
            
        health, oxygen, score, difficulty, batteryPower = update_stats(health, oxygen, score, difficulty, batteryPower)
        display_statistics(health, oxygen, score, batteryPower)
    return health, oxygen, score, difficulty, batteryPower
health, oxygen, score, difficulty, batteryPower = Level1(controlRoomChoice, health, oxygen, score, difficulty, batteryPower)
#First level is complete
print("""\nEnd of Darkness in the Control room\n
        The control room falls quiet as you assess the consequences of your decision.\n
        Your engineering console updates your current health, the colony's oxygen reserves, and your mission score.\n
        Mission Status: Scenario 1 of 10 Complete\n
        The next emergency awaits.\n
        Next Level: The Oxygen Crisis \n""")

input("Press Enter to continue...")
print("_" * 80)
print(rooms[currentLocation]["exit"])
destination = input("Where would you like to go: ").strip()
while destination not in rooms[currentLocation]["exit"]:

        print("Invalid destination. Please choose a valid room.")
        destination = input("Where would you like to go: ").strip()
       
currentLocation = destination
print(f"You have moved to the {currentLocation}.")
# End of simulation should always be at the end
print("\n")
print("This is the end of the current simulation. More content will be added in the future\n\n")
input("Press Enter to End Simulation")

