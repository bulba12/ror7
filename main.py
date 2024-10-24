from colorama import init, Fore, Back, Style

init(autoreset=True)

print(Fore.RED + 'Це червоний текст')
print(Back.GREEN + 'Текст з зеленим фоном')
print(Style.BRIGHT + 'Яскравий текст' + Style.RESET_ALL)
