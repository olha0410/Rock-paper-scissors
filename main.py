def menu():

    print('Choose your element:')
    print(' 1) rock')
    print(' 2) scissors')
    print(' 3) paper')
    
    input1 = input('Firt user:  ')
    input2 = input('Second user:  ') 

    if input1 == input2:
       print('It is a tie!')
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
       
menu()
