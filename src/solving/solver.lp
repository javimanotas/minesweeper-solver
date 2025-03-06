% predicate unknown(X, Y)
% predicate at(X, Y, N) -> N: number of adjacent mines

cell(X, Y) :- unknown(X, Y).
cell(X, Y) :- at(X, Y, _).

adjacent(X, Y, X', Y') :- cell(X, Y)
                        , cell(X', Y')
                        , | X - X' | <= 1
                        , | Y - Y' | <= 1
                        , (X, Y) != (X', Y')
                        .


{ mine(X, Y) } :- unknown(X, Y).


:- at(X, Y, N), N != #sum { 1, X', Y' : adjacent(X, Y, X', Y'), mine(X', Y') }.

safe(X, Y) :- unknown(X, Y), not mine(X, Y).


#show safe/2.
#show mine/2.
