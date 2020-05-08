print('ON THE SUBJECT OF COMPLICATED WIRES')
batteries = int(input("How many batteries are there? "))
parallel_ports = input("Are there any parallel ports (Yy/Nn)? ")
parallel_ports = True if parallel_ports.lower() == 'y' else False
serial_odd = int(input("Enter the last digit of the serial number: "))
serial_odd = False if serial_odd % 2 == 0 else True
print('\n\n')

# binary decision tree based on complicated wires diagram
# LED? -> Red? -> Blue? -> Star? -> Answer
lookup_table = [
    [
        [['C', 'C',],['S', 'D'],],
        [['S', 'C',],['S', 'P'],],
    ],
    [
        [['B', 'D',],['P', 'P'],],
        [['B', 'B',],['D', 'S'],],
    ],
]

print('Input each wire, in this order: LED (Yy/Nn), Color (Ww/Rr/Bb/Mm), Star (Yy/Nn)')
print('For example, a red and blue wire with a lit LED and no star -> YMN')
print('Type 0 to exit\n\n')
user_input = -1
wire_number = 1
while (user_input != 0):
    user_input = input('Wire ' + str(wire_number) + ': ')
    if (user_input == '0'):
        break
    led = user_input[0]
    color = user_input[1]
    star = user_input[2]

    # process LED setting
    if (led == 'y'):
        ledIndex = 1
    elif (led == 'n'):
        ledIndex = 0
    else:
        print('LED must be Yy/Nn. You gave: ' + led)
        continue
    
    # process color setting
    if (color == 'w'):
        redIndex = 0
        blueIndex = 0
    elif (color == 'r'):
        redIndex = 1
        blueIndex = 0
    elif (color == 'b'):
        redIndex = 0
        blueIndex = 1
    elif (color == 'm'):
        redIndex = 1
        blueIndex = 1
    else:
        print('Color must be Ww/Rr/Bb/Mm. You gave: ' + color)
        continue

    # process star setting
    if (star == 'y'):
        starIndex = 1
    elif (star == 'n'):
        starIndex = 0
    else:
        print('Star must be Yy/Nn. You gave: ' + star)
        continue
    
    result = lookup_table[ledIndex][redIndex][blueIndex][starIndex]
    
    if (result == 'B'):
        result = 'C' if batteries > 1 else 'D'
    elif (result == 'P'):
        result = 'C' if parallel_ports else 'D'
    elif (result == 'S'):
        result = 'D' if serial_odd else 'C'
    
    if (result == 'C'):
        print('CUT Wire ' + str(wire_number) + '\n')
    else:
        print('DO NOT CUT Wire ' + str(wire_number) + '\n')
    wire_number += 1

print('Done with complicated wires!')
