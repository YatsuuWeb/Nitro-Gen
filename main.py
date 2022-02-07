import random
from colored import fg

caracteres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

banner =F"""{fg(93)}
$$\     $$\          $$\                                         $$\      $$\           $$\       
\$$\   $$  |         $$ |                                        $$ | $\  $$ |          $$ |      
 \$$\ $$  /$$$$$$\ $$$$$$\    $$$$$$$\ $$\   $$\ $$\   $$\       $$ |$$$\ $$ | $$$$$$\  $$$$$$$\  
  \$$$$  / \____$$\\_$$  _|  $$  _____|$$ |  $$ |$$ |  $$ |      $$ $$ $$\$$ |$$  __$$\ $$  __$$\ 
   \$$  /  $$$$$$$ | $$ |    \$$$$$$\  $$ |  $$ |$$ |  $$ |      $$$$  _$$$$ |$$$$$$$$ |$$ |  $$ |
    $$ |  $$  __$$ | $$ |$$\  \____$$\ $$ |  $$ |$$ |  $$ |      $$$  / \$$$ |$$   ____|$$ |  $$ |
    $$ |  \$$$$$$$ | \$$$$  |$$$$$$$  |\$$$$$$  |\$$$$$$  |      $$  /   \$$ |\$$$$$$$\ $$$$$$$  |
    \__|   \_______|  \____/ \_______/  \______/  \______/       \__/     \__| \_______|\_______/ 
                                                                                                  
                                                                                                  
                                                                                                  
"""
print(banner)
f=input("entré pour gen")
while True:
    nitrocode = ''

    for i in range(16):
        nitrocode = f"{nitrocode}{random.choice(caracteres)}"

    print(f"https://discord.gift/{nitrocode}")

    with open("nitros.txt", "a+") as nitroFile:

        nitroFile.write(f"https://discord.gift/{nitrocode}\n")

        nitroFile.close()