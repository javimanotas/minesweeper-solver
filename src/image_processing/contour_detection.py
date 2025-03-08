import cv2
import numpy as np

def same_cell(cellA, cellB):
    return np.abs(cellA[2] - cellB[2]) < 4

def filter_similars(cells):
    cells.sort(key = lambda c : c[2])

    groups = {}
    i = 0
    while i < len(cells):
        j = i + 1
        while j < len(cells) and same_cell(cells[i], cells[j]):
            j += 1
        
        groups[i] = j - i
        i += 1

    k = max(groups, key = groups.get)

    for i in range(k, k+groups[k]):
        print(f'detected cell: cells[i]')

    return cells[k:k+groups[k]]

def cnt_rowscols(cells, n):
    cnt = 1
    for i in range(1, len(cells)):
        if np.abs(cells[i][n] - cells[0][n]) < 3:
            cnt += 1
    return cnt

def find_contour(image_path, debug = False):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cells = []

    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)
            aspect_ratio = w / h
            
            if np.abs(aspect_ratio - 1) < 0.1 and w > 8 and h > 8:
                if debug:
                    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                
                cells.append((x, y, w, h))

    if debug:
        cv2.imshow('Detected Minesweeper Board', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    valid_cells = filter_similars(cells)

    rows = cnt_rowscols(valid_cells, 0)
    cols = cnt_rowscols(valid_cells, 1)
    print((rows, cols))

    key = lambda n : lambda x : x[n]
    a = max(valid_cells, key=key(0))
    b = max(valid_cells, key=key(1))
    return (min(valid_cells, key=key(0))[0], min(valid_cells, key=key(1))[1], a[0] + a[2], a[1] + a[3]), rows, cols
