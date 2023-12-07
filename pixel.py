from PIL import Image

def get_white_pixels(image_path):
    img = Image.open(image_path)
    width, height = img.size

    white_pixels = []

    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            if pixel == (255, 255, 255):  # Vérifie si le pixel est blanc (R=255, G=255, B=255)
                white_pixels.append((x, y))

    return white_pixels

# Chemin vers votre fichier PNG
image_file = 'ascii2.png'

white_positions = get_white_pixels(image_file)

for position in white_positions:
    print(f"{position[0]},{position[1]}")

