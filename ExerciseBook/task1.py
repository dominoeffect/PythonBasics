# def which_prize(point):
#     if point <= 50 and point >=0:
#     	print("Congratulations! You have won a wooden rabbit!")
#     elif point >=51 and point <= 150:
#     	print("Oh dear, no prize this time.")
#     elif point >=151 and point <=180:
#     	print("Congratulations! You have won a wafer-thin mint!")
#     elif point >=181 and point <=200:
#     	print("Congratulations! You have won a penguin!")
#     else:
#         print("Oh dear, no prize this time.")





def which_prize(points):
    """
    Returns the prize-winning message, given a number of points
    """
    if points <= 50:
        return "Congratulations! You have won a wooden rabbit!"
    elif points <= 150:
        return "Oh dear, no prize this time."
    elif points <= 180:
        return "Congratulations! You have won a wafer-thin mint!"
    else:
        return "Congratulations! You have won a penguin!"


print(which_prize(34))



def which_prize(points):
    """
    Returns the prize-winning message, given a number of points
    """
    if points <= 50:
        prize = "wooden rabbit"
    elif points <= 150:
        prize = None
    elif points <= 180:
        prize = "wafer-thin mint"
    else:
        prize = "penguin"

    if prize:
        if prize == "wooden rabbit":
            return "Congratulations! You have won a wooden rabbit!"
        elif prize == "wafer-thin mint":
            return "Congratulations! You have won a wafer-thin mint!"
        else:
            return "Congratulations! You have won a penguin!"
    else:
        return "Oh dear, no prize this time."
    
# print(which_prize(140))




def which_prize2(points):
    """
    Returns the number of prize-winning message, given a number of points
    """
    prize = None
    if points <0:
        prize = None
    if points <= 50:
        prize = "a wooden rabbit"
    elif 151 <= points <= 180:
        prize = "a wafer-thin mint"
    elif points >= 181:
        prize = "a penguin"
    if prize:
        return "Congratulations! You have won " + prize + "!"
    else:
        return "Oh dear, no prize this time."