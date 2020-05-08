print('ON THE SUBJECT OF PASSWORDS\n\n')
print('Input all values from each dial, continuing until the password is cracked.')
print('Type 0 to exit\n')

possible_passwords = [
  'about', 'after', 'again', 'below', 'could', 'every', 'first', 'found', 'great', 'house',
  'large', 'learn', 'never', 'other', 'place', 'plant', 'point', 'right', 'small', 'sound',
  'spell', 'still', 'study', 'their', 'there', 'these', 'thing', 'think', 'three', 'water',
  'where', 'which', 'world', 'would', 'write'
]

user_input = -1
column_number = 0
remaining_possibilities = possible_passwords
while (user_input != 0):
  next_possibilities = []
  user_input = input('Enter the letters for column ' + str(column_number + 1) + ': ')
  if user_input == '0':
    break
  for ltr in user_input:
    for i in range(len(remaining_possibilities)):
      if remaining_possibilities[i][column_number] == ltr:
        next_possibilities.append(remaining_possibilities[i])
  print('Remaining possibilities: ')
  print(*next_possibilities)
  print('\n')
  if len(next_possibilities) == 1:
    print('\nThe word is "' + next_possibilities[0] + '"!')
    break
  else:
    remaining_possibilities = next_possibilities
    column_number += 1

print('Done with passwords!')