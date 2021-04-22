# ╭━━╮╱╱╱╱╱╱╱╱╱╱╱╱╭━━━╮╱╭╮╭╮
# ╰┫┣╯╱╱╱╱╱╱╱╱╱╱╱╱┃╭━━╯╱┃┣╯╰╮
# ╱┃┃╭╮╭┳━━┳━━┳━━╮┃╰━━┳━╯┣╮╭╋━━┳━╮
# ╱┃┃┃╰╯┃╭╮┃╭╮┃┃━┫┃╭━━┫╭╮┣┫┃┃╭╮┃╭╯
# ╭┫┣┫┃┃┃╭╮┃╰╯┃┃━┫┃╰━━┫╰╯┃┃╰┫╰╯┃┃
# ╰━━┻┻┻┻╯╰┻━╮┣━━╯╰━━━┻━━┻┻━┻━━┻╯
# ╱╱╱╱╱╱╱╱╱╭━╯┃
# ╱╱╱╱╱╱╱╱╱╰━━╯

#Notice, you will need the python pillow package.
from PIL import Image, ImageFilter, ImageEnhance, ImageOps, ImageDraw


from PIL.ImageFilter import (
   BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
)

import os

#Notice, you can change any of these based on how you want to.

Brightnener = 1.2
Size = (1100, 1100)
Contrastener = 0.9
CenterImage = (0.7, 0.5)

#Getting the actual original image.
cwd = os.chdir('YourDictory')
image = Image.open('ImageName.png')

#Sharpening the image a little bit.
image = image.filter(SHARPEN)
enhancer = ImageEnhance.Brightness(image)
image = enhancer.enhance(Brightnener)

#Cutting a circle around the image.
mask = Image.new('L', Size, 0)
draw = ImageDraw.Draw(mask) 
draw.ellipse((0, 0) + Size, fill=255)

#Adding detail.
image = image.filter(SMOOTH_MORE)
enhancer = ImageEnhance.Contrast(image)
image = enhancer.enhance(Contrastener)
image = image.filter(DETAIL)

#Masking the image.
image = ImageOps.fit(image, mask.size, centering = CenterImage)
image.putalpha(mask)

#Saving the new image.
image.save('YourName.png', quality = 100)
image.show()

#Coded by Nicholas Smirnov