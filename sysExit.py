import sys

while True:
    print("Wpisz exit, aby zakończyc działanie programu")
    response = input()
    if response=="exit":
        sys.exit()
    print("Wpisałeś " + response + ".")