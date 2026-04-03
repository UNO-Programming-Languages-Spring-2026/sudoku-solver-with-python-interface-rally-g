from typing import Tuple
import clingo

class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku
        
    def __str__(self) -> str:
        s = ""
        for row in range(9):
            for column in range(9):
                s += self.sudoku[(row+1, column+1)]
                s += " "
                
                if column == 8:
                    s += "\n"
                    if (row + 1) % 3 == 0:
                        s += "\n"
                        
                if (column + 1) % 3 == 0:
                    s += " "
        
        return s

    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        return cls(sudoku)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        sudoku = {}
        positions = model.symbols(shown=True)
        for position in positions:
            positionString = str(position)
            sudoku[(int(positionString[7]), int(positionString[9]))] = int(positionString[11])
        # YOUR CODE HERE
        return cls(sudoku)
