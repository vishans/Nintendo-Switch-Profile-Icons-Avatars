import os

for avatar in os.listdir('avatars'):
    print(f'<img src="avatars/{avatar}">')