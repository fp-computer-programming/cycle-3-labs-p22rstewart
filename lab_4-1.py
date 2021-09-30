# Author: Ryan (AMDG) 9/30/21

magic_strength = int(input("input your magic strength: "))
shield_charge = int(input("input your shield charge: "))

if not ((magic_strength >= 90) and (shield_charge >= 75)):
    print("The dragon burns you to a crisp.")

else:
    print("You defeated the dragon! But the princess is in another castle.")
