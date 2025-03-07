import pygame

def load_image(path, res = None):
    image = pygame.image.load(path)
    
    if res != None:
        ratio = image.get_rect().width / image.get_rect().height
        image = pygame.transform.scale(image, (ratio * res, res))
    
    return image

def display_solution(image_path, grid, solution):
    mines = solution['mine']
    safes = solution['safe']

    pygame.init()
    image = load_image(image_path)
    width, height = image.get_rect().width, image.get_rect().height
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Solution')

    screen.blit(image, (0, 0))

    cell_size = width / grid.cols

    mine = load_image('./src/display/mine.png', cell_size * 0.8)
    not_mine = load_image('./src/display/not_mine.png', cell_size * 0.66)
    
    for (r, c) in mines:
        screen.blit(mine, ((c + 0.26) * cell_size, (r + 0.125) * cell_size))
    for (r, c) in safes:
        screen.blit(not_mine, ((c + 0.27) * cell_size, (r + 0.2) * cell_size))

    pygame.display.update()
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
