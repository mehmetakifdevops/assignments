from random import randrange
a = randrange(500)

print("=" * 58)
print("                 █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n                 █░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n                 █░░║║║╠─║─║─║║║║║╠─░░█\n                 █░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n                 █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
print("=" * 58)
while True:
    print("=" * 58)
    b = int(input("▁ ▂ ▄ ▅ ▆ ▇ █  GUESS A NUMBER BETWEEN 0-500  █ ▇ ▆ ▅ ▄ ▂ ▁\n"))
    print("=" * 58)
    if b == a:
        print("ღ(¯`◕‿◕´¯) ♫ ♪ ♫   WELL DONE TRUE NUMBER WAS :", b, "  ♫ ♪ ♫ )¯´◕‿◕`¯(ღ")
        print()
        print("██████   █████  ███    ███ ███████      ██████  ██    ██ ███████ ██████") 
        print("██       ██   ██ ████  ████ ██          ██    ██ ██    ██ ██      ██   ██")
        print("██   ███ ███████ ██ ████ ██ █████       ██    ██ ██    ██ █████   ██████ ")
        print("██    ██ ██   ██ ██  ██  ██ ██          ██    ██  ██  ██  ██      ██   ██ ")
        print(" ██████  ██   ██ ██      ██ ███████      ██████    ████   ███████ ██   ██")
        print()
        print("=" * 58)
        break
    elif b > a:
        print("HOLD YOUR HORSES MAN, NOW YOU ARE OUT OF LİNE")
        print("                ԅ(º﹃ºԅ)")
    elif b > a * 90 / 100:
        
        print("░▒▓█ YOU ARE TOO CLOSE █▓▒░")
    elif b > a / 2:
        
        print("░▒▓█ YOU PASSED TO HALF OF NUMBER █▓▒░") 
    elif b < a / 2:
        print("ARE YOU SURE YOU CAN HANDLE THIS? YOU MUST İNCREASE YOUR NUMBER")
        print("                       ¯\_(ツ)_/¯")
    elif b == a / 2:
        
        print("░▒▓█ YOU ARE ON THE HALF █▓▒░")
