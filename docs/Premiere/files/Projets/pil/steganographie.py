from PIL import Image

fuji = Image.open("Mont_Fuji.jpg")
code = { chr(64+i) : i for i in range(1,27)}
code[" "]=0

to_encode = "BRAVO VOUS AVEZ REUSSI A TROUVER LE MESSAGE CACHE DANS L IMAGE"
for i in range(len(to_encode)):

