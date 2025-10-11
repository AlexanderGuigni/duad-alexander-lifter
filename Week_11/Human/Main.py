from Human import Human
from Arm import Arm 
from Leg import Leg
from Head import Head
from Feet import Feet
from Hand import Hand
from Torso import Torso

def main():
    head = Head()
    torso = Torso()
    hand = Hand()
    feet = Feet()
    arm = Arm(hand)
    leg = Leg(feet)

    human = Human(head, torso, arm, leg)
    print("Human created with the following parts:")
    print(f"Head: {human.Head}")
    print(f"Torso: {human.Torso}")
    print(f"Arm: {human.Arm}")
    print(f"Leg: {human.Leg}")

main()