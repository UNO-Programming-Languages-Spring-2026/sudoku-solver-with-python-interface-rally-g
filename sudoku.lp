#const dim = 9.

x(1..dim).
y(1..dim).
v(1..dim).

sudoku(X,Y,V) :- initial(X,Y,V).

% assign a value V for every combo of X and Y
1 { sudoku(X,Y,V) : v(V) } 1 :- x(X), y(Y).
% this works the same as
% 1 { sudoku(1,1,1); sudoku(1,1,2); sudoku(1,1,3); sudoku(1,1,4) ...} 1.
% but for every combination of coordinates in x and y

% define the subgrids
subgrid(X,Y,1) :- x(X), y(Y), X <= 3, Y <= 3.
subgrid(X,Y,2) :- x(X), y(Y), X <= 6, X > 3, Y <= 3.
subgrid(X,Y,3) :- x(X), y(Y), X > 6, Y <= 3.
subgrid(X,Y,4) :- x(X), y(Y), X <= 3, Y <= 6, Y > 3.
subgrid(X,Y,5) :- x(X), y(Y), X <= 6, X > 3, Y <= 6, Y > 3.
subgrid(X,Y,6) :- x(X), y(Y), X > 6, Y <= 6, Y > 3.
subgrid(X,Y,7) :- x(X), y(Y), X <= 3, Y > 6.
subgrid(X,Y,8) :- x(X), y(Y), X <= 6, X > 3, Y > 6.
subgrid(X,Y,9) :- x(X), y(Y), X > 6, Y > 6.

% no row can have the same value twice
:- sudoku(X1,Y,V), sudoku(X2,Y,V), X1 != X2.

% no column can have the same value twice
:- sudoku(X,Y1,V), sudoku(X,Y2,V), Y1 != Y2.

% no subgrid can have the same value twice
:- sudoku(X1,Y1,V), sudoku(X2,Y2,V), subgrid(X1,Y1,G), subgrid(X2,Y2,G), (X1,Y1) != (X2,Y2).

#show sudoku/3.