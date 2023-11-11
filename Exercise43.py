banknotes = {
    1: "George Washington",
    2: "Thomas Jefferson",
    5: "Abraham Lincoln",
    10: "Alexander Hamilton",
    20: "Andrew Jackson",
    50: "Ulysses S. Grant",
    100: "Benjamin Franklin"
}

def display_leader(denomination):
    if denomination in banknotes:
        leader_name = banknotes[denomination]
        print(f"The person on the ${denomination} banknote is: {leader_name}")
    else:
        print("Sorry, there is no information about this banknote.")

try:
    denomination = int(input("Enter the denomination of the banknote (1, 2, 5, 10, 20, 50, 100): "))
    display_leader(denomination)
except ValueError:
    print("Please enter an integer.")