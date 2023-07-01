# mapframes
Mapframes is a very simple script developed to assist in the making of mapping videos on Youtube, by automating the creation of frames/images that represent changes in occupation during a depicted conflict.
It takes in a start image, and an end image, and progressively paints the map until it reaches the end image result, saving each step as an output png. These output pngs can then be used in a video editing software for animation purposes.

# How to run
On windows, the command is py mapframes.py (RGB value of the attacker occupation)
for example: py mapframes.py (255,0,0)
Make sure there are no spaces when writing the RGB value. 
