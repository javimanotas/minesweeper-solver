import os
import time
from PIL import ImageGrab
from image_processing.contour_detection import find_contour
from image_processing.image_processor import image_to_grid
from solving import solver
from display.display import display_solution

image_path = './temp_screenshot.png'

for i in range(2):
    print(f'taking a screenshot in {3 - i}...')
    time.sleep(1)

screenshot = ImageGrab.grab()
screenshot.save(image_path)

contour, rows, cols = find_contour(image_path)
print(f'detected contour: {contour}')

grid = image_to_grid(image_path, contour, rows, cols)
print(grid)

solution = solver.solve(grid)
print(solution)
display_solution(image_path, contour, grid, solution)

os.remove(image_path)
