from PIL import Image
from grid import Grid

def dst(color0, color1):
    return sum((color0[i] - color1[i]) ** 2 for i in range(3)) ** 0.5

# colors picked from ./gnome_mines_template
colors = {
    0: [222,222,220],
    1: [221,250,195],
    2: [236,237,191],
    3: [237,218,180],
    4: [237,195,138],
    5: [247,161,162],
    6: [254,167,133],
    7: [255,125,96],
    8: [255,50,60],
    '?': [186,189,182]
}

min_dst = min(dst(v, v1)
              for (k, v) in colors.items()
              for (k1, v1) in colors.items()
              if k != k1)

max_col_error = min_dst / 3

def get_game_cell(image, min_row, min_col, max_row, max_col):

    freqs = { k : 0 for k in colors.keys() }

    for y in range(min_row, max_row, 4):
        for x in range(min_col, max_col, 4):
            color = image.getpixel((x, y))

            for k, v in colors.items():
                if dst(color, v) < min_dst:
                    freqs[k] += 1
                    break

    return max(freqs, key=freqs.get)

def image_to_grid(image_path, contour, rows, cols):
    image = Image.open(image_path, "r").convert('RGB')
    width = contour[2] - contour[0]
    cell_size = width // cols

    grid = Grid(rows, cols)

    for r in range(rows):
        for c in range(cols):
            grid[(r, c)] = get_game_cell(image, cell_size * r + contour[1], cell_size * c + contour[0], cell_size * (r + 1) + contour[1], cell_size * (c + 1) + contour[0])

    return grid
