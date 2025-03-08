import sys
import os
import time
from PIL import ImageGrab
from image_processing.contour_detection import find_contour
from image_processing.image_processor import image_to_grid
from solving import solver
from display.display import display_solution

def show_usage():
    print('Usage: python3 <path_to_main> [-debug]')
    sys.exit(1)

def main():
    debug = False

    if len(sys.argv) > 2:
        show_usage()
    elif len(sys.argv) == 2:
        if sys.argv[1] == '-debug':
            debug = True
        else:
            show_usage()

    image_path = './temp_screenshot.png'

    for i in range(2):
        print(f'taking a screenshot in {3 - i}...')
        time.sleep(1)

    screenshot = ImageGrab.grab()
    screenshot.save(image_path)

    contour, rows, cols = find_contour(image_path)
    grid = image_to_grid(image_path, contour, rows, cols)
    solution = solver.solve(grid)

    if debug:
        print(f'\ndetected contour: {contour}')
        print(f'\ngrid:\n{grid}')
        print(f'\n{solution}')

    display_solution(image_path, contour, grid, solution)
    os.remove(image_path)

if __name__ == '__main__':
    main()
