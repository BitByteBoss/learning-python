# # Your code goes here. Define a function called 'sign'
# def sign(x):
#     if x > 0:
#         return 1
#     elif x < 0:
#         return -1
#     else:
#         return 0
# # Check your answer
# q1.check()

# def to_smash(total_candies):
#     """Return the number of leftover candies that must be smashed after distributing
#     the given number of candies evenly between 3 friends.
    
#     >>> to_smash(91)
#     1
#     """
#     if total_candies == 1:
#         print("splitting 1 candy")
#     else:
#         print("Splitting", total_candies, "candies")
    
#     return total_candies % 3

# to_smash(91)
# to_smash(1)


# def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
#     # Don't change this code. Our goal is just to find the bug, not fix it!
#     return have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday

# # Change the values of these inputs so they represent a case where prepared_for_weather
# # returns the wrong answer.
# have_umbrella = False
# rain_level = 6
# have_hood = True
# is_workday = False

# # Check what the function returns given the current values of the variables above
# actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
# print(actual)

# # Check your answer
# q3.check()


# def is_negative(number):
#     if number < 0:
#         return True
#     else:
#         return False

# def concise_is_negative(number):
#     return number < 0# Your code goes here (try to keep it to one line!)

# # Check your answer
# q4.check()


# def wants_all_toppings(ketchup, mustard, onion):
#     """Return whether the customer wants "the works" (all 3 toppings)
#     """
#     return ketchup and mustard and onion

# # Check your answer
# q5.a.check()


# def wants_plain_hotdog(ketchup, mustard, onion):
#     """Return whether the customer wants a plain hot dog with no toppings.
#     """
#     return not(ketchup or mustard or onion)
 

# # Check your answer
# # q5.b.check()

# def exactly_one_sauce(ketchup, mustard, onion):
#     """Return whether the customer wants either ketchup or mustard, but not both.
#     (You may be familiar with this operation under the name "exclusive or")
#     """
#     return (not ketchup and mustard) or ( ketchup and not mustard)

# # Check your answer
# q5.c.check()


# def exactly_one_topping(ketchup, mustard, onion):
#     """Return whether the customer wants exactly one of the three available toppings
#     on their hot dog.
#     """
#     return ((not ketchup) and (not mustard) and onion) or ( ketchup and (not mustard) and (not onion)) or (mustard and (not ketchup) and (not onion))


# # Check your answer
# q6.check()