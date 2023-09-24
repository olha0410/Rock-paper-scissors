# Rock-paper-scissors
# This game is played by two people. The rules are the same as everyone knows. The first player chooses his element (input). 
# After that, the other player takes the same action. The result depends on  the selected elements and will be printed at the end
def menu():
    print('Choose your element:')
    print(' 1) rock')
    print(' 2) scissors')
    print(' 3) paper')

def getuserinput(username):
    menu()
    inp = input(username + ' makes his choice: ')
    return inp

input1 = getuserinput('Firt user')
input2 = getuserinput('Second user') 

if input1 == input2:
    print('no sides!')
elif input1 == '1' and input2 == '2':
    print('First user won')
elif input1 == '2' and input2 == '3':
    print('First user won')
elif input1 == '3' and input2 == '1':
    print('First user won')

elif input1 == '2' and input2 == '1':
    print('Second user won')
elif input1 == '3' and input2 == '2':
    print('Second user won')
elif input1 == '1' and input2 == '3':
    print('Second user won')
