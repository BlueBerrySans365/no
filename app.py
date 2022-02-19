import os
import random
from PIL import Image
count = 0
#0 255 27
def gen(cont):
    headColR = random.randint(0,255)
    headColG = random.randint(0,255)
    headColB = random.randint(0,255)
    sweatColR = random.randint(0,255)
    sweatColG = random.randint(0,255)
    sweatColB = random.randint(0,255)
    face = random.randint(1,3)

    img1 = Image.open("assets/hair.png")
    img1 = img1.convert("RGBA")
    width = img1.size[0] 
    height = img1.size[1] 
    for i in range(0,width):
        for j in range(0,height):
            data = img1.getpixel((i,j))
            if (data[0]==0 and data[1]==255 and data[2]==27):
                img1.putpixel((i,j),(headColR, headColG, headColB))
    img2 = Image.open("assets/clothes/sweater.png")
    img2 = img2.convert("RGBA")
    width = img2.size[0] 
    height = img2.size[1] 
    for i in range(0,width):
        for j in range(0,height):
            data = img2.getpixel((i,j))
            if (data[0]==0 and data[1]==255 and data[2]==27):
                img2.putpixel((i,j),(sweatColR, sweatColG, sweatColB))

    img3 = Image.open(f"assets/face/{face}.png")
    img4 = Image.open("assets/body1.png")
    bg = Image.new('RGB',(img1.size[0], img1.size[1]), (255,255,255))

    final2 = Image.new("RGBA", bg.size)
    final2 = Image.alpha_composite(final2, img4)
    final2 = Image.alpha_composite(final2, img3)
    final2 = Image.alpha_composite(final2, img2)
    final2 = Image.alpha_composite(final2, img1)
    final2.save(f"genered/{cont}.png","PNG")

if os.path.exists(f'{os.getcwd()}/genered'):
    pass
else:
    os.mkdir("genered")

while count <= 5:
    print(f"made: {count}")
    gen(count)
    count += 1
