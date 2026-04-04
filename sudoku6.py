
import clingo
from sudoku_board import Sudoku

class Context:
    
    def __init__(self, board: Sudoku):
        self.board = board
    
    def initial(self) -> list[clingo.symbol.Symbol]:
        values = []

        for (r, c), v in self.board.sudoku.items():
            values.append(clingo.Tuple_((clingo.Number(r),clingo.Number(c),clingo.Number(v))))

        return values


class ClingoApp(clingo.application.Application):
    def main(self, ctl, files):

        ctl.load("sudoku.lp")
        ctl.load("sudoku_py.lp")

        with open(files[0], 'r') as fileToRead:
            sudokuBoard = Sudoku.from_str(fileToRead.read())

        context = Context(sudokuBoard)

        ctl.ground(context=context)

        ctl.solve()
        # finally done
        
    def print_model(self, model, printer):
        print(Sudoku.from_model(model))
        
clingo.application.clingo_main(ClingoApp())