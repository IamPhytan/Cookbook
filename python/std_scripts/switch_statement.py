# In other languages, there is a way to implement
# a switch-case statement. In C++ :

# switch (x) {
#     case "value 1":
#         action1;
#         break;
#     case "value 2":
#         action2;
#         break;
#     case "value 3":
#         action3;
#         break;
#     default:
#         defaultAction;
# }

# %%
# In Python, it's possible to implement something similar with dictionaries :

prompt = "Give an integer between 1 and 12 (inclusively) : "
while not (month_number := input(prompt)).isdigit() or not (1 <= int(month_number) <= 12):
    print("Not a valid integer")
month_number = int(month_number)

calendar = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}
month_name = calendar.get(month_number, None)

# %%
# We can also call functions with this structure


def mountain_climbing():
    """Spring activity"""
    print("Up we go !")


def soccer():
    """Summer activity"""
    print("GOOOOAALL!")


def apples_u_pick():
    """Autumn activity"""
    print("An apple a day keeps the doctor away")


def ski():
    """Winter activity"""
    print("Down we go !")


def default_activity():
    """Default"""
    print("Is 42 an activity ?")


activities = {
    "January": ski,
    "February": ski,
    "March": mountain_climbing,
    "April": mountain_climbing,
    "May": mountain_climbing,
    "June": soccer,
    "July": soccer,
    "August": soccer,
    "September": apples_u_pick,
    "October": apples_u_pick,
    "November": apples_u_pick,
    "December": ski,
    None: default_activity,
}
activities[month_name]()
