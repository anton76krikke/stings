# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
player1_scored = 'marco van basten'
player2_scored = 'ruud gullit'
goal_1 = ' in 32'
goal_2 = ' in 54'

scorers = player1_scored + goal_1, player2_scored + goal_2
print(scorers)

report = f' the player  {player1_scored} scored in the  {goal_1} nd minute \n the player  {player2_scored} scored in the  {goal_2} th minute  '
print(report)

player = 'frank rijkaard'
print(player.find(' '))
print(player[:5])

last_name_length = len(player[5:])
print(last_name_length)

name_short = f'{player[0]}.{player[5:]}'
print(name_short)

chant_space = f'{player[:5]}!' * len(player[:5])

chant = chant_space[:-1]
print(chant, '!')
good_chant = chant[:-1] != ""
print(good_chant)
