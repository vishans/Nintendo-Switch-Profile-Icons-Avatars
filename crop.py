from PIL import Image
from secrets import token_hex

# Thanks to Random Talking Bush, Shiny Quagsire for ripping 
# Thanks to Nintendo

avatarCount = 0
deadSpots = [(3,20),(4,20),(5,20),(3,25),(4,25),(5,25),(1,25),(2,25)]
with Image.open("sprites.png") as spriteSheet:
    for j in range(26):
        for i in range(6):
            if (i,j) not in deadSpots:
                avatarCount+= 1
                avatar = spriteSheet.crop((1+(257*i),1+(257*j),257*(i+1),257*(j+1)))
                # avatar.show()
                fileName = f'{avatarCount}{token_hex()}'
                avatar.save(f'avatars/{fileName}.png')
    
    print(f'{avatarCount} avatars, each with size {avatar.size}px')