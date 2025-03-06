import clingo
from grid import Grid

def has_numeric_neighbor(grid, r, c):
    for i in range(r - 1, r + 2):
        for j in range(c - 1, c + 2):
            if i < 0 or j < 0 or i >= grid.rows or j >= grid.cols:
                continue

            if isinstance(grid[(i, j)], int):
                return True

    return False

def solve(grid):

    predicates = []
    for r in range(grid.rows):
        for c in range(grid.cols):
            if grid[(r, c)] == '?':
                if has_numeric_neighbor(grid, r, c):
                    predicates.append(f'unknown({r}, {c}).')
            else:
                predicates.append(f'at({r}, {c}, {grid[(r, c)]}).')

    asp_facts = '\n'.join(predicates)

    ctl = clingo.Control()
    ctl.configuration.solve.models = 0
    ctl.add('base', [], asp_facts)
    ctl.load('./src/solving/solver.lp')
    ctl.ground([('base', [])])

    solutions = { 'mine' : None, 'safe' : None }

    def get_solution(model):
        for atomName in ('mine', 'safe'):
            sol = set()
        
            for atom in model.symbols(shown=True):
                if atom.name == atomName:
                    sol.add((atom.arguments[0].number, atom.arguments[1].number))
        
            if solutions[atomName] == None:
                solutions[atomName] = sol
            else:
                solutions[atomName] = solutions[atomName].intersection(sol)

    ctl.solve(on_model=get_solution)

    return solutions
