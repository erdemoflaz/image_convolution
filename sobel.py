from PIL import Image, ImageDraw
from math import sqrt

input_image = Image.open("erdem.jpg")
input_pixels = input_image.load()

# renk yogunlugu bul
intensity = [[sum(input_pixels[x, y]) / 3 for y in range(input_image.height)] for x in range(input_image.width)]

kernelx = [[1, 0, -1],
           [2, 0, -2],
           [1, 0, -1]]
kernely = [[1, 2, 1],
           [0, 0, 0],
           [-1, -2, -1]]

# yeni image
output_image = Image.new("RGB", input_image.size)
draw = ImageDraw.Draw(output_image)

# renk yogunlugu ile cekirdek arasindaki konvulusyonu hesapla
for x in range(1, input_image.width - 1):
    for y in range(1, input_image.height - 1):
        magx, magy = 0, 0
        for a in range(3):
            for b in range(3):
                xn = x + a - 1
                yn = y + b - 1
                magx += intensity[xn][yn] * kernelx[a][b]
                magy += intensity[xn][yn] * kernely[a][b]

        # siyah beyaz olarak ciz
        color = int(sqrt(magx**2 + magy**2))
        draw.point((x, y), (color, color, color))

output_image.save("output.png")
