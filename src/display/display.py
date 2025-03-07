import pygame

def load_image(path, res = None):
    image = pygame.image.load(path)
    
    if res != None:
        width, height = image.get_size()
        ratio = width / height
        image = pygame.transform.scale(image, (ratio * res, res))
    
    return image

def center_at(screen, row, col, cell_size, res):
    width, height = res

    center_x = cell_size * (col + 0.5)
    center_y = cell_size * (row + 0.5)
    pygame.draw.circle(screen, (0, 0, 255), (cell_size * col, cell_size * row), 5)
    return center_x - width / 2, center_y - height / 2

def display_solution(image_path, grid, solution):
    mines = solution['mine']
    safes = solution['safe']

    pygame.init()
    image = load_image(image_path)
    width, height = image.get_size()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Solution')

    screen.blit(image, (0, 0))

    cell_size = width / grid.cols

    mine = load_image('./src/display/mine.png', cell_size * 0.8)
    not_mine = load_image('./src/display/not_mine.png', cell_size * 0.66)
    
    for (r, c) in mines:
        screen.blit(mine, center_at(screen, r, c, cell_size, mine.get_size()))
    for (r, c) in safes:
        screen.blit(not_mine, center_at(screen, r, c, cell_size, not_mine.get_size()))

    pygame.display.update()
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
