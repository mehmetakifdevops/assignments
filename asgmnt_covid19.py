age = input("Are you a cigarette addict older than 75 years old?(yes or no): ").title() == "Yes"



chronic = input("Do you have a severe chronic disease?(yes or no): ").title() == "Yes"



immune = input("Is your immune system too weak?(yes or no): ").title() == "Yes"



risk = age or chronic or immune

if risk:

    print("You are in risky group")

else:

    print("You are not in risky group")