import random2
secretNumber=random2.randint(1,20)
print('Mam na myśli pewną liczbę z zakresu od 1 do 20.')

for guessTaken in range(1,7):
    print('Spróbuj odgadnąć liczbę.')
    guess=int(input())

    if guess < secretNumber:
        print('Liczba jest za mała!')
    elif guess > secretNumber:
        print('Podana liczba jest za duża')
    else:
        break

if guess == secretNumber:
    print("Brawo, odgadłeś liczbę w ciągu " + str(guessTaken) + " prób!")
else:
    print("No cóż, nie udało się, miałem na myśli liczbę " + str(secretNumber))