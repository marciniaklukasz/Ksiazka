while True:
    print("Kim jesteś?")
    name=input()
    if name != 'Łukasz':
        continue
    print('Witaj Łukasz, Jakie jest hasło?')
    password = input()
    if password == 'mlecznik':
        break
print('Masz dostęp!')
