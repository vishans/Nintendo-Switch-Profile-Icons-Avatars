import os
p = '\\'.join((__file__.split('\\')[:-1]) + ['avatars\\'])

for avatar in sorted(os.listdir('avatars'),key=lambda x: os.path.getmtime(p+x)):
    print(f'<img src="avatars/{avatar}">')