# This is a short and simple game created to fulfill the requirements of a Codecademy portfolio project. It entails navigating a starship to different planets in the style of a rudimentary "choose your own adventure" story. Names and other material from "Star Trek" are used, but only for the non-commercial, educational purpose of demonstrating mastery of the course material.

import random

# List of valid warp factors
warp_factors = [str(factor) for factor in range(1, 10)]

# List of planets
planets = ["Vulcan", "Ceti Alpha V", "Qo'noS", "Risa"]

# Generate stardate for opening log entry
def stardate():
    sdate = str(round(random.uniform(1312.4, 5928.5), 1))
    return sdate
initial_stardate = stardate()

# Start list for computing subsequent stardates
sdate_list = [initial_stardate]

# Compute stardates for subsequent log entries
def next_stardate():
    sdate_list.append(str(round((float(sdate_list[-1]) + 0.1), 1)))
    return sdate_list[-1]

# Create class for planets
class Planet:
    
    def __init__(self, planet_name, environment, contact, objective, contact_response, log_entry):
        """Initialize basic planet attributes"""
        self.planet_name = planet_name
        self.planet_environment = environment
        self.contact = contact
        self.objective = objective
        self.contact_response = contact_response
        self.log_entry = log_entry
        self.order_scan = "Scan the planet's surface."
        self.order_hail = f"Hail {contact}."
        self.order_log_entry = "Record a log entry."
        self.order_new_course = "Lay in a new course."

    def arrival_dialogue(self):
        """Sulu announces arrival and asks for orders"""
        arrival_prompt = f"""\n(Some time later...)
SULU: Entering orbit around {self.planet_name}. Orders, sir?
    A - {self.order_scan}
    B - {self.order_hail}
"""
        arrival_order = input(arrival_prompt)

        while True:
            if arrival_order.upper() == "A":
                self.scan_planet()
                break
            elif arrival_order.upper() == "B":
                self.hail()
                break
            else:
                arrival_order = self.repeat_order()
                continue

    def repeat_order(self):
        """Science officer asks Captain to repeat order; handles error of invalid input in following functin definitions"""
        input("ACTING SCIENCE OFFICER: Sorry, Captain. Please repeat. (A or B) ")

    def scan_planet(self):
        """Science officer reports results of planetary scan"""
        next_order = input(f"""
ACTING SCIENCE OFFICER: Sensors indicate a class M environment {self.planet_environment}. Orders?
    A - {self.order_hail}
    B - {self.order_new_course}
""")
        while True:
            if next_order.upper() == "A":
                self.hail()
                break
            elif next_order.upper() == "B":
                self.new_course()
                break
            else:
                next_order = self.repeat_order()
                continue

    def hail(self):
        """Uhura hails, Kirk greets, contact replies"""
        next_order = input(f"""
UHURA: Hailing frequencies open.
KIRK: {self.contact}, this is Captain James Kirk of the Federation starship Enterprise. We have come to {self.objective}.
{self.contact.upper()}: {self.contact_response}
    A - {self.order_log_entry}
    B - {self.order_new_course}
""")
        while True:
            if next_order.upper() == "A":
                self.make_log_entry()
                break
            elif next_order.upper() == "B":
                self.new_course()
                break
            else:
                next_order = self.repeat_order()
                continue
    
    def make_log_entry(self):
        """Captain makes a log entry at end of mission"""
        new_stardate = next_stardate()
        print(f"Captain's log, stardate {new_stardate}: {self.log_entry}")
        next_order = input(f"""
Orders, Captain?
    A - {self.order_new_course}
    B - End game.
""")
        while True:
            if next_order.upper() == "A":
                self.new_course()
                break
            elif next_order.upper() == "B":
                self.end_program()
                break
            else:
                next_order = self.repeat_order()
                continue
                
    def new_course(self):
        """Captain sets course for another planet"""
        print("KIRK: Lay in a new course.")
        navigation_dialogue()

    def end_program(self):
        """Print message announcing end of game"""
        print("SCOTTY: Computer, end program. Save holodeck file as 'Scotts_Enterprise_No_Bloody_A_B_C_or_D.'")

# Instantiate planets
planet_vulcan = Planet(planets[0], "with gravity of 1.4 g and relatively thin atmosphere", "Ambassador Sarek", "return an earring that your wife lost during your last visit to Enterprise", "Captain, logic would lead one to judge that your use of a starship to transport a single piece of jewelry to be disproportionate to the task. Nevertheless, on Amanda's behalf, I give you sincere thanks.", "On an excursion to Vulcan, the crew of the Enterprise had occasion to explore the paradoxes of Vulcan philosophy. I for one contend that sometimes the needs of the one outweigh the needs of the many.")
planet_ceti = Planet(planets[1], "but with far less vegetation than on our last visit", "Kahn", "check in on your progress. How's the colony doing?", "Why, Captain, if I didn't know better, I would say it sounded as if you were gloating. As to how we're doing--well, allow me to pose a question or two to you. Your sensors didn't happen to detect anything unusual about the orbit of this planet, did they? Or perhaps an anomalous reading about the number of planets in the sys...\nUHURA: Captain, the transmission is breaking due to atmospheric disturbance...\nKirk: Erm, that'll do, Lieutenant. Nothing to see here.", "The Enterprise responded to reports of a pre-animate plot hole in the Ceti Alpha system. Nothing conclusive to report.")
planet_qonos = Planet(planets[2], "with immeasurably high quantities of blood-based cuisine", "Koloth", "return a tribble you left behind during our last encounter", "Kirk, you have got some nerve. My affection for those little buggers was supposed to be a secret. But I will overlook this dishonor you cause me, for I cannot but admire the bravado of a man who would commit a flagrant violation of the Neutral Zone treaty just to return a beloved pet to an old adversary. You have the heart of a true warrior. Now get out of Klingon space before the whole fleet is upon you. Qapla!", "It is too early to assess the character of the day's events. Either I have forged a strategically important friendship with a former foe, or I have gratuitously ignited a new war between the Federation and the Klingon Empire. Only time will tell.")
planet_risa = Planet(planets[3], "with a San Diego climate from pole to pole", "La'an", "retrieve my first officer. Shore leave time is up. Can I persuade you to relinquish him?", "James! I thought we were done being awkward. Why didn't you just call Spock directly? Know what, nevermind. He's on his way to the transporter now.", "Commander Spock has returned from shore leave. And not a moment too soon. I make much better command decisions when he's around.")

# Dictionary associating planet names with instances of Planet class
planet_dict = {planets[0]: planet_vulcan, planets[1]: planet_ceti, planets[2]: planet_qonos, planets[3]: planet_risa}

# Display title
title_card = """
 SSSSS  TTTTTTT   A     RRRRRR      TTTTTTT RRRRRR  EEEEEEE K     K
S     S    T     A A    R     R        T    R     R E       K    K 
SS         T    A   A   R    R         T    R    R  E       K   K  
  SSS      T    AAAAA   RRRRR          T    RRRRR   EEEEEEE KKKK   
     SS    T   A     A  R    R         T    R    R  E       K   K  
S     S    T   A     A  R     R        T    R     R E       K    K 
 SSSSS     T   A     A  R     R        T    R     R EEEEEEE K     K
                    --- THE OUTTAKE MISSIONS ---
 """
print(title_card)

# Game dialogue begins with opening log entry featuring random stardate
intro = f"KIRK: Captain's log, stardate {initial_stardate}: The Enterprise has completed her most recent assignment and is embarking upon a series of brief but urgent errands. First Officer Spock is still on shore leave."
print(intro)

# User inputs destination and speed in dialogue with Chekov and Sulu
def navigation_dialogue():
    # Chekov prompts for destination
    destination_prompt = f"""
CHEKOV: Awaiting your orders, Captain. What is our destination?
    A - {planets[0]}
    B - {planets[1]}
    C - {planets[2]}
    D - {planets[3]}
(Enter a selection)
"""
    destination_order = input(destination_prompt)
    
    # Chekov confirms course
    while True:
        if destination_order.upper() == "A" or planets[0] in destination_order:
            loc = planet_dict[planets[0]]
        elif destination_order.upper() == "B" or planets[1] in destination_order:
            loc = planet_dict[planets[1]]
        elif destination_order.upper() == "C" or planets[2] in destination_order:
            loc = planet_dict[planets[2]]
        elif destination_order.upper() == "D" or planets[3] in destination_order:
            loc = planet_dict[planets[3]]
        else:
            loc = ""
        if loc != "":
            print(f"CHEKOV: Course laid in for {loc.planet_name}, sir.")
            break
        else:
            destination_order = input("CHEKOV: I'm afraid that's not awaiable in navigational database at present. Orders, sir? (A-D) ")
            continue
    
    # Sulu prompts for speed
    speed_prompt = input(f"\nSULU: Warp factor, sir? (1-9) ")
    while True:
        if speed_prompt in warp_factors:
            print(f"      Engaging at warp {speed_prompt}.")
            loc.arrival_dialogue()
            break
        else:
            speed_prompt = input("Respectfully, Captain, physics won't permit that. More importantly, neither will Commander Scott. 1-9, sir? ")
            continue

# Run navigation dialogue function to begin play
navigation_dialogue()