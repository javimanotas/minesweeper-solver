import clingo
from grid import Grid

def solve(grid):

    predicates = []
    for r in range(grid.rows):
        for c in range(grid.cols):
            if grid[(r, c)] == '?':
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
