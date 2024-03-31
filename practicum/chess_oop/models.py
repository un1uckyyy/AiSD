from validation import validation

WHITE = 0
BLACK = 1
LETTERS = "abcdefgh"


class Board:
    def __init__(self):
        self.board = [
            [Rook(BLACK), Knight(BLACK), Bishop(BLACK), Queen(BLACK),
             King(BLACK), Bishop(BLACK), Knight(BLACK), Rook(BLACK)],
            [Pawn(BLACK) for _ in range(8)],
            ["." for _ in range(8)],
            ["." for _ in range(8)],
            ["." for _ in range(8)],
            ["." for _ in range(8)],
            [Pawn(WHITE) for _ in range(8)],
            [Rook(WHITE), Knight(WHITE), Bishop(WHITE), Queen(WHITE),
             King(WHITE), Bishop(WHITE), Knight(WHITE), Rook(WHITE)],
        ]
        self.moves_counter = 0

    def __str__(self):
        s = "   A B C D E F G H   \n\n"
        for ind in range(8, 0, -1):
            s += f"{ind}  {' '.join([str(el) for el in self.board[8 - ind]])}  {ind}\n"
        s += "\n   A B C D E F G H   "
        return s

    def __getitem__(self, ind):
        return self.board[ind]

    def game(self):
        print(self)
        while True:
            print(
                f"""
            Ход {"белых" if self.moves_counter % 2 == 0 else "черных"}, введите координаты вашего хода в формате
            [буква][цифра]-[буква][цифра]"""
            )
            input_string = input()
            if not validation(input_string, self):
                continue
            self.moves_counter += 1
            self.move(input_string)
            print(self)
            if "k" not in self.__str__() or "K" not in self.__str__():
                print("Игра окончена!")
                print(f"Победили {'Белые' if self.moves_counter % 2 == 1 else 'Черные'}")
                break

    def move(self, input_string):
        _from, _to = input_string.split("-")
        _from = (8 - int(_from[1]), LETTERS.index(_from[0].lower()))
        _to = (8 - int(_to[1]), LETTERS.index(_to[0].lower()))
        if self[_to[0]][_to[1]] == ".":
            self[_from[0]][_from[1]], self[_to[0]][_to[1]] = self[_to[0]][_to[1]], self[_from[0]][_from[1]]
        else:
            self[_from[0]][_from[1]], self[_to[0]][_to[1]] = ".", self[_from[0]][_from[1]]


class Rook:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return "r" if self.color else "R"

    def can_move(self, _from, board: Board):
        x1, y1 = _from
        allowed_moves = set()
        for dx in range(1, 8):
            if 0 <= x1 + dx <= 7:
                cell = board[x1 + dx][y1]
                if cell == ".":
                    allowed_moves.add((x1 + dx, y1))
                elif cell.color != self.color:
                    allowed_moves.add((x1 + dx, y1))
                    break
                else:
                    break
        for dx in range(-1, -8, -1):
            if 0 <= x1 + dx <= 7:
                cell = board[x1 + dx][y1]
                if cell == ".":
                    allowed_moves.add((x1 + dx, y1))
                elif cell.color != self.color:
                    allowed_moves.add((x1 + dx, y1))
                    break
                else:
                    break
        for dy in range(1, 8):
            if 0 <= y1 + dy <= 7:
                cell = board[x1][y1 + dy]
                if cell == ".":
                    allowed_moves.add((x1, y1 + dy))
                elif cell.color != self.color:
                    allowed_moves.add((x1, y1 + dy))
                    break
                else:
                    break
        for dy in range(-1, -8, -1):
            if 0 <= y1 + dy <= 7:
                cell = board[x1][y1 + dy]
                if cell == ".":
                    allowed_moves.add((x1, y1 + dy))
                elif cell.color != self.color:
                    allowed_moves.add((x1, y1 + dy))
                    break
                else:
                    break
        return allowed_moves


class Knight:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return "n" if self.color else "N"

    def can_move(self, _from, board: Board):
        x1, y1 = _from
        allowed_moves = set()
        for dx in (-2, -1, 1, 2):
            if dx in (-2, 2):
                for dy in (-1, 1):
                    if 0 <= (x1 + dx) <= 7 and 0 <= (y1 + dy) <= 7:
                        cell = board[x1 + dx][y1 + dy]
                        if cell == ".":
                            allowed_moves.add((x1 + dx, y1 + dy))
                        elif cell.color != self.color:
                            allowed_moves.add((x1 + dx, y1 + dy))
            else:
                for dy in (-2, 2):
                    if 0 <= (x1 + dx) <= 7 and 0 <= (y1 + dy) <= 7:
                        cell = board[x1 + dx][y1 + dy]
                        if cell == ".":
                            allowed_moves.add((x1 + dx, y1 + dy))
                        elif cell.color != self.color:
                            allowed_moves.add((x1 + dx, y1 + dy))
        return allowed_moves


class Bishop:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return "b" if self.color else "B"

    def can_move(self, _from, board: Board):
        x1, y1 = _from
        allowed_moves = set()
        for sign_x in (-1, 1):
            for sign_y in (-1, 1):
                for delta in range(1, 8):
                    if 0 <= x1 + sign_x * delta <= 7 and 0 <= y1 + sign_y * delta <= 7:
                        cell = board[x1 + sign_x * delta][y1 + sign_y * delta]
                        if cell == ".":
                            allowed_moves.add((x1 + sign_x * delta, y1 + sign_y * delta))
                        elif cell.color != self.color:
                            allowed_moves.add((x1 + sign_x * delta, y1 + sign_y * delta))
                            break
                        else:
                            break
        return allowed_moves


class Queen:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return "q" if self.color else "Q"

    def can_move(self, _from, board: Board):
        x1, y1 = _from
        allowed_moves = set()
        for dx in range(1, 8):
            if 0 <= x1 + dx <= 7:
                cell = board[x1 + dx][y1]
                if cell == ".":
                    allowed_moves.add((x1 + dx, y1))
                elif cell.color != self.color:
                    allowed_moves.add((x1 + dx, y1))
                    break
                else:
                    break
        for dx in range(-1, -8, -1):
            if 0 <= x1 + dx <= 7:
                cell = board[x1 + dx][y1]
                if cell == ".":
                    allowed_moves.add((x1 + dx, y1))
                elif cell.color != self.color:
                    allowed_moves.add((x1 + dx, y1))
                    break
                else:
                    break
        for dy in range(1, 8):
            if 0 <= y1 + dy <= 7:
                cell = board[x1][y1 + dy]
                if cell == ".":
                    allowed_moves.add((x1, y1 + dy))
                elif cell.color != self.color:
                    allowed_moves.add((x1, y1 + dy))
                    break
                else:
                    break
        for dy in range(-1, -8, -1):
            if 0 <= y1 + dy <= 7:
                cell = board[x1][y1 + dy]
                if cell == ".":
                    allowed_moves.add((x1, y1 + dy))
                elif cell.color != self.color:
                    allowed_moves.add((x1, y1 + dy))
                    break
                else:
                    break
        for sign_x in (-1, 1):
            for sign_y in (-1, 1):
                for delta in range(1, 8):
                    if 0 <= x1 + sign_x * delta <= 7 and 0 <= y1 + sign_y * delta <= 7:
                        cell = board[x1 + sign_x * delta][y1 + sign_y * delta]
                        if cell == ".":
                            allowed_moves.add((x1 + sign_x * delta, y1 + sign_y * delta))
                        elif cell.color != self.color:
                            allowed_moves.add((x1 + sign_x * delta, y1 + sign_y * delta))
                            break
                        else:
                            break
        return allowed_moves


class King:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return "k" if self.color else "K"

    def can_move(self, _from, board: Board):
        x1, y1 = _from
        allowed_moves = set()
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == dy == 0:
                    continue
                if 0 <= x1 + dx <= 7 and 0 <= y1 + dy <= 7:
                    cell = board[x1 + dx][y1 + dy]
                    if cell == ".":
                        allowed_moves.add((x1 + dx, y1 + dy))
                    elif cell.color != self.color:
                        allowed_moves.add((x1 + dx, y1 + dy))
        return allowed_moves


class Pawn:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return "p" if self.color else "P"

    def can_move(self, _from, board: Board):
        x1, y1 = _from
        allowed_moves = set()
        if self.color == WHITE:
            if x1 == 6 and board[x1 - 2][y1] == ".":
                allowed_moves.add((x1 - 2, y1))
            if 1 <= x1 <= 6 and board[x1 - 1][y1] == ".":
                allowed_moves.add((x1 - 1, y1))
            if 1 <= y1 <= 7 and board[x1 - 1][y1 - 1] != ".":
                if board[x1 - 1][y1 - 1].color != self.color:
                    allowed_moves.add((x1 - 1, y1 - 1))
            if 0 <= y1 <= 6 and board[x1 - 1][y1 + 1] != ".":
                if board[x1 - 1][y1 + 1].color != self.color:
                    allowed_moves.add((x1 - 1, y1 + 1))
        elif self.color == BLACK:
            if x1 == 1 and board[x1 + 2][y1] == ".":
                allowed_moves.add((x1 + 2, y1))
            if 1 <= x1 <= 6 and board[x1 + 1][y1] == ".":
                allowed_moves.add((x1 + 1, y1))
            if 1 <= y1 <= 7 and board[x1 + 1][y1 - 1] != ".":
                if board[x1 + 1][y1 - 1].color != self.color:
                    allowed_moves.add((x1 + 1, y1 - 1))
            if 0 <= y1 <= 6 and board[x1 + 1][y1 + 1] != ".":
                if board[x1 + 1][y1 + 1].color != self.color:
                    allowed_moves.add((x1 + 1, y1 + 1))
        return allowed_moves
