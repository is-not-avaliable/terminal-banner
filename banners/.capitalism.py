from colorama import Fore, init
init()
 
banner = f"""{Fore.MAGENTA}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣄⣀⣤⣼⣿⣿⣶⣤⣀⣤⣴⣾⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣩⣿⣟⣿⣿⣿⣿⣶⣤⣴⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣄⠛⣽⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠛⠿⠿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢶⣜⢻⣿⡆⠈⢽⣿⠛⣿⣽⣿⠿⣀⣐⣶⣽⡿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⢷⣿⣇⠀⣽⣿⣧⠼⣿⣿⣿⡟⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣟⣯⡿⠷⣿⣿⣧⣽⣿⡿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣞⣽⣿⣿⣿⣿⣿⣿⢿⣿⣻⣷⣮⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣴⣟⣹⣿⣤⣿⣿⣿⣿⣿⣿⢿⣷⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⡟⣿⠛⡏⠹⠻⡏⢿⡌⠀⠁⢿⡽⢛⡶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠞⠛⠙⢁⡿⠉⠀⠀⠀⠀⠀⠀⠙⠀⠙⢦⡀⠀⠉⢿⣿⢃⡝⢙⡶⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣛⣑⣤⠀⠘⠉⠀⠀⠀⠀⣠⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⣤⡟⣤⠞⢉⡷⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠞⣇⡾⡿⠟⠁⠀⠀⠀⣀⣀⣀⣠⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠣⣴⣟⡴⢃⡿⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⡾⢻⢿⣧⡿⠯⠁⠀⠀⠀⣴⣿⢟⣿⣿⣿⣿⡿⣻⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣴⢋⣤⢏⡿⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⡼⢋⢸⠀⡇⠿⠃⠀⠀⠀⢠⣾⣿⣿⣿⣿⠿⣿⣻⣿⣿⣿⣻⣟⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠿⢋⣠⠏⣴⢃⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡴⢯⡇⢸⣸⣇⠉⠀⠀⠀⠀⠀⢸⣿⣿⣿⡏⠀⢀⣿⢟⣿⣿⠙⠻⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣋⡤⢚⣱⠏⣸⢻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣴⠟⣡⣸⢹⡾⠃⠀⠀⠀⠀⠀⠀⠀⠘⣿⣾⣿⣷⣄⣸⣿⣿⣿⡏⠀⠀⠈⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡴⠚⣡⠞⣱⠋⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⡼⠋⢰⣿⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣻⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⠞⣡⠞⢁⡞⡽⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣼⠃⠀⠀⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣯⣾⣷⣿⣿⢶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⢁⡴⢋⠞⣠⢿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣷⡿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⢋⡴⢋⣴⣡⣮⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⡀⠀⠀⣼⡿⣿⣿⠀⠹⣿⣷⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢉⣵⠞⣡⣾⡿⣽⢫⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣻⣿⢷⡀⠀⣿⣿⣿⣿⠀⠀⠘⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⣡⢾⡿⣫⣾⡵⣻⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣵⡻⣿⣶⣿⣿⣿⣿⣤⣤⣾⣿⣿⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣿⡿⢋⡴⣯⢟⡞⣡⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⢿⣿⡿⣿⣿⢿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡼⣫⣴⣿⠟⣥⢟⡜⢁⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣇⢰⢻⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⣿⣵⣿⡿⠛⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠟⣻⠟⣩⣿⡷⢋⣴⢿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠸⣆⠸⣾⣿⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠿⠿⠷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠀⣠⡶⠋⡤⠞⣡⢞⡽⢋⡴⢋⣵⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠙⣦⠙⣿⢸⢰⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⡀⠀⡀⠀⠀⠀⠀⠀⣀⠀⡀⢠⡾⢣⡾⠋⣠⠚⣠⠞⣡⢋⡴⢋⡴⣿⣿⣷⣿⣽⣿⣶⣦⣤⣄⡀⠀⠀⠀
⠀⠀⠀⠘⢷⡉⢸⣼⣻⣧⡶⣄⢀⡀⣀⠀⠀⢀⣀⡴⣤⡞⣡⠞⣡⠞⣡⠞⣁⡴⢋⣰⢿⡴⢋⡼⣭⠟⡽⢋⣾⡟⢁⡞⢁⡞⣡⠊⣠⢏⣼⣟⣟⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦
⠀⠀⠀⠀⠀⠻⣦⡈⠙⣿⡇⡇⢸⣿⣿⣽⣷⣿⣿⣴⠫⡿⣧⡞⣡⠞⣡⠞⣉⡴⢋⡴⢋⣵⣫⡼⣫⠞⣠⣿⠟⣰⠏⡴⢋⡞⣠⣾⡿⠿⢤⣤⣶⣼⣾⣷⣿⣿⣿⣿⣿⣶⣶⠶⠿
⠀⠀⠀⠀⠀⠀⢸⣿⣶⣤⣙⣙⡘⠃⠋⠘⠙⢁⠁⡉⠈⠁⣉⢀⣉⣀⣠⣶⠿⠤⠬⣶⣾⣀⣉⠺⣿⣾⣿⣏⡼⢡⠞⣡⣿⠶⠿⠭⠽⣿⣿⣿⣿⠿⣿⣭⣭⣭⣍⣍⣉⠉⠉⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠶⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣽⣿⣿⣿⡿⠿⠶⣶⣤⢤⣤⣤⣤⣼⣯⣾⣧⣿⣴⣿⣿⠛⠛⠛⠛⣳⣶⣟⣛⣛⣛⣛⡒⠚⠚⠛⠛⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠛⠿⣷⣿⣷⣶⣶⣾⣾⣾⣭⠭⠭⠭⠭⠭⠿⠽⠿⠿⠯⠭⠭⣿⢿⣿⣿⣿⣶⣿⣿⣯⣭⠭⠤⠤⠤⠄⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⢩⠽⠿⠿⠽⣿⢯⣿⣶⣭⣭⣉⣈⣁⣀⣀⣒⠛⠛⠛⠒⠀⠀⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

{Fore.RED}
 ▄████▄   ▄▄▄       ██▓███  ▄▄▄█████▓ ▄▄▄       ██▓     ██▓  ██████  ███▄ ▄███▓
▒██▀ ▀█  ▒████▄    ▓██░  ██▒▓  ██▒ ▓▒▒████▄    ▓██▒    ▓██▒▒██    ▒ ▓██▒▀█▀ ██▒
▒▓█    ▄ ▒██  ▀█▄  ▓██░ ██▓▒▒ ▓██░ ▒░▒██  ▀█▄  ▒██░    ▒██▒░ ▓██▄   ▓██    ▓██░
▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██▄█▓▒ ▒░ ▓██▓ ░ ░██▄▄▄▄██ ▒██░    ░██░  ▒   ██▒▒██    ▒██ 
▒ ▓███▀ ░ ▓█   ▓██▒▒██▒ ░  ░  ▒██▒ ░  ▓█   ▓██▒░██████▒░██░▒██████▒▒▒██▒   ░██▒
░ ░▒ ▒  ░ ▒▒   ▓▒█░▒▓▒░ ░  ░  ▒ ░░    ▒▒   ▓▒█░░ ▒░▓  ░░▓  ▒ ▒▓▒ ▒ ░░ ▒░   ░  ░
  ░  ▒     ▒   ▒▒ ░░▒ ░         ░      ▒   ▒▒ ░░ ░ ▒  ░ ▒ ░░ ░▒  ░ ░░  ░      ░
░          ░   ▒   ░░         ░        ░   ▒     ░ ░    ▒ ░░  ░  ░  ░      ░   
░ ░            ░  ░                        ░  ░    ░  ░ ░        ░         ░   
░                                                                                 
         {Fore.GREEN}                               
                [by: Iván]@is-not-avaliable
"""

print(banner)
