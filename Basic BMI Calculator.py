# Basic BMI Calculator by Afrodisiac
import os, sys

from asyncore import loop
from cProfile import run
from termcolor import colored, cprint

# Welcome message
cprint("Basic BMI Calculator by Afrodisiac\n", "white", "on_green")


# Variables
user_name = input(("What is your name?\n"))
user_height = float(input("How tall are you (in inches)?\n"))
user_weight = float(input("How much do you weigh?\n"))
user_BMI = (user_weight * 703) / (user_height ** 2)  # Weight is multiplied by 703 to convert lbs to kgs

# Program
while True:
    if user_BMI < 18.5:
        cprint(f"Yikes, {user_name}! According to the math, your BMI is {user_BMI}, which classifies you as Underweight!", "red")

    elif 18.5 < user_BMI < 24.9:
        cprint(f"{user_name}, your BMI is {user_BMI}, which classifies you as Normal. Nothing more, normie.", "green")

    elif 24.9 < user_BMI < 29.9:
        cprint(f"Careful, {user_name}. Your BMI was calculated at {user_BMI}, which is considered Overweight.", "yellow")

    elif user_BMI > 29.9:
        cprint(f"{user_name}, your BMI is {user_BMI}, which is considered Obese. Please see a physician.", "red")
        
    next_BMI = (input("Would you like to check another BMI? Y/n\n"))
    if next_BMI == "n":
        break
    else:
        os.execl(sys.executable, sys.executable, *sys.argv)
