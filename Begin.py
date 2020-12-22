print('Witaj, świecie!')
print('Jak masz na imie?')
myName = input()
if myName =='Łukasz':
    print("No siema byku, jak tam?")
else:
    print('Miło Cię poznać ' + myName + '.')
    print('Liczba znaków w Twoim imieniu wynosi:')
    print(len(myName))
print('Ile masz lat?')
myAge = input()
print('Za rok będziesz mieć ' + str(int(myAge) +1) + ' lat.')