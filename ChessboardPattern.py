"""Problem Statement
A chessboard pattern is a pattern that satisfies the following conditions:

The pattern has a rectangular shape.
The pattern contains only the characters '.' (a dot) and 'X' (an uppercase letter X).
No two symbols that are horizontally or vertically adjacent are the same.
The symbol in the lower left corner of the pattern is '.' (a dot).
You are given two s rows and columns. Write a method that computes the chessboard pattern with these dimensions, and returns it in a . The elements of the return value correspond to rows of the pattern. Specifically, the first character of the last element of the return value represents the lower left corner (see example 0).

Definition
Class: ChessboardPattern
Method: makeChessboard
Parameters: integer, integer
Returns: tuple (string)
Method signature: def makeChessboard(self, rows, columns):
Limits
Time limit (s): 840.000
Memory limit (MB): 64
Constraints
- rows will be between 1 and 50, inclusive.
- columns will be between 1 and 50, inclusive.
Examples
0)
8
8
Returns: {"X.X.X.X.", ".X.X.X.X", "X.X.X.X.", ".X.X.X.X", "X.X.X.X.", ".X.X.X.X", "X.X.X.X.", ".X.X.X.X" }
A standard chessboard. Note that the last element starts with a dot.
1)
1
20
Returns: {".X.X.X.X.X.X.X.X.X.X" }
A single row is a special case of a rectangle.
2)
5
1
Returns: {".", "X", ".", "X", "." }
And so is a single column.
3)
5
13
Returns: {".X.X.X.X.X.X.", "X.X.X.X.X.X.X", ".X.X.X.X.X.X.", "X.X.X.X.X.X.X", ".X.X.X.X.X.X." }"""

class ChessboardPattern:
    def makeChessboard(self, rows, columns):

        rownum = 0
        chars = [".X", "X."]
        board = []
        while rownum < rows:
            col = ""
            colnum = 0
            while colnum < columns:
                col += chars[rownum % 2][colnum % 2]
                colnum += 1

            board.insert(0, col)
            rownum += 1

        return tuple(board)


M = ChessboardPattern()
print(M.makeChessboard(8, 8))