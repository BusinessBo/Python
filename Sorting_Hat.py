x = int(input('''Q1) Do you like Dawn or Dusk?
    1) Dawn
    2) Dusk
Answer: '''))

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

if x == 1:
 Gryffindor += 1
 Ravenclaw += 1
elif x == 2:
  Hufflepuff += 1
  Slytherin += 1
else:
  print('Wrong input!')

y = int(input('''Q2) When Im dead, I want people to remember me as:
    1) The Good
    2) The Great
    3) The Wise
    4) The Bold
Answer: '''))

if y == 1:
 Gryffindor += 2
elif y == 2:
  Ravenclaw += 2
elif y == 3:
  Hufflepuff += 2
elif y == 4:
  Slytherin += 2
else:
  print('Wrong input!')

z = int(input('''Q3) Which kind of instrument most pleases your ear?
    1) The violin
    2) The trumpet
    3) The piano
    4) The drum
Answer: '''))

if z == 1:
  Gryffindor += 4
elif z == 2:
  Ravenclaw += 4
elif z == 3:
  Hufflepuff += 4
elif z == 4:
  Slytherin += 4
else:
  print('Wrong input!')

if Gryffindor > Ravenclaw and Gryffindor > Hufflepuff and Gryffindor > Slytherin:
  print('Welcome to Gryffindor')
elif Ravenclaw  > Gryffindor and Ravenclaw > Hufflepuff and Ravenclaw > Slytherin:
  print('Welcome to Ravenclaw')
elif Hufflepuff > Gryffindor and Hufflepuff > Ravenclaw and Hufflepuff > Slytherin:
  print('Welcome to Hufflepuff')
elif Slytherin > Gryffindor and Slytherin > Ravenclaw and Slytherin > Hufflepuff:
  print('Welcome to Slytherin')

