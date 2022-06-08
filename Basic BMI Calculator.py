# Basic BMI Calculator by Afrodisiac

print("Basic BMI Calculator by Afrodisiac\n")
# Variables
user_name = (input("What is your name?\n"))
user_height = float(input("How tall are you (in inches)?\n"))
user_weight = float(input("How much do you weigh?\n"))
user_BMI = (user_weight * 703) / (user_height ** 2)  # Weight is multiplied by 703 to convert lbs to kgs

# Program
def main():
    if user_BMI < 18.5:
        print(f"Yikes, {user_name}! According to the math, your BMI is {user_BMI}, which classifies you as Underweight!")

    elif 18.5 < user_BMI < 24.9:
        print(f"{user_name}, your BMI is {user_BMI}, which classifies you as Normal. Nothing more, normie.")

    elif 24.9 < user_BMI < 29.9:
        print(f"Careful, {user_name}. Your BMI was calculated at {user_BMI}, which is considered overweight.")

    elif user_BMI > 29.9:
        print(f"{user_name}, your BMI is {user_BMI}, which is considered Obese. Please see a physician.")

    else:
        next_BMI = (input("Would you like to run another BMI calculation? Y/n"))
        if next_BMI == "Y":
            main()
