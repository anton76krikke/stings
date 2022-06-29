# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

maker1 = "van basten "
maker2 = " gullit "
doelpunt1 = 32
doelpunt2 = 54

scorers = maker1 + str(doelpunt1),  maker2 + str(doelpunt2)
print(scorers)

report = f"{maker1} scoorde in  de {doelpunt1} nd minute  \n  {maker2} scoorde in  de {doelpunt2} th minute"
print(report)

player = "hans van breukelen"

first_name = player.split(" ")[0]
print(first_name)
last_Name = player.split(" ")[1:3]
print(last_Name)
tot_spatie = player.find(" ", 5, 10)
print(tot_spatie)
voornaam = player[0:4]
print(voornaam)
achternaam = player[5:20]
print(len(achternaam))
print(achternaam)
name_short = ((voornaam[0], ("."), achternaam))
print(name_short)
chant = voornaam + '!'
print(chant * len(voornaam))
good_chant = print(chant[-1] != " ")
