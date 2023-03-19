# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

scorer_2 = "Marco van Basten"
scorer_1 = "Ruud Gullit"
goal_0 = 32
goal_1 = 54

scorers = scorer_1 + " " + str(goal_0) + ", " + scorer_2 + " " + str(goal_1)
print(scorers)

report = scorer_1 + " scored in the " +  str(goal_0) + "nd minute\n" + scorer_2 + " scored in the " + str(goal_1) + "th minute"
print(report)

player = 'frank rijkaard'
print(player.find(' '))
first_name = (player[:5])
print(first_name)

last_name_len = len(player[6:])
print(last_name_len)

name_short = f'{player[0]}.{player[5:]}'
print(name_short)

chant_space = f'{player[:5]}! ' * len(player[:5])

chant = chant_space[:-1]
print(chant)
good_chant = chant[:-1] != ""
print(good_chant)
