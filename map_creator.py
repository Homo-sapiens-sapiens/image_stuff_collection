from PIL import Image

def is_blue_hsva(hsva):
    h, s, v, a = hsva
    return 60<h

img = Image.open("map.png").convert("RGBA")
hsv_img = img.convert("HSV")
hsv_pixels = hsv_img.load()
rgba_pixels = img.load()

w, h = img.size
new_img = Image.new("RGBA", (w, h))
new_pixels = new_img.load()

for y in range(h):
    for x in range(w):
        h_val, s_val, v_val = hsv_pixels[x, y]
        a_val = rgba_pixels[x, y][3]
        hsva = (h_val, s_val, v_val, a_val)

        if is_blue_hsva(hsva):
            neighbors = []
            for nx in range(max(0, x-1), min(w, x+2)):
                for ny in range(max(0, y-1), min(h, y+2)):
                    if nx == x and ny == y:
                        continue
                    h2, s2, v2 = hsv_pixels[nx, ny]
                    a2 = rgba_pixels[nx, ny][3]
                    neighbors.append((h2, s2, v2, a2))

            if any(not is_blue_hsva(nb) for nb in neighbors):
                new_pixels[x, y] = (0, 0, 0, 255) 
            else:
                new_pixels[x, y] = (0, 0, 0, 0)
        else:
            new_pixels[x, y] = (90, 90, 90, 255)

new_img.save("map_transformed.png")
