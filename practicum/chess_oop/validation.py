LETTERS = "abcdefgh"


def validate_input(input_string):
    if len(positions := input_string.split("-")) != 2:
        return False
    _from, _to = [el.strip() for el in positions]
    if not (_from[0].lower() in "abcdefgh" and _to[0].lower() in "abcdefgh") or not (
            _from[1] in "12345678" and _to[1] in "12345678"
    ):
        return False
    return True


def validate_move(input_string, board):
    _from, _to = input_string.split("-")
    _from = (8 - int(_from[1]), LETTERS.index(_from[0].lower()))
    _to = (8 - int(_to[1]), LETTERS.index(_to[0].lower()))
    if _from == _to:
        print("Нельзя походить на то же место!")
        return False
    cell = board[_from[0]][_from[1]]
    if cell == '.':
        print("Вы выбрали пустую клетку! Выберете свою фигуру!")
        return False
    if board.moves_counter % 2 == 0 and cell.color == 1 \
            or board.moves_counter % 2 == 1 and cell.color == 0:
        print("Это не ваша фигура!")
        return False
    if _to not in cell.can_move(_from, board):
        # allowed_moves = cell.can_move(_from, board)
        # desk = [["X" if (j, i) in allowed_moves else "." for i in range(8)] for j in range(8)]
        # print(*desk, sep="\n")
        return False
    return True


def validation(input_string, board):
    if not validate_input(input_string):
        print("Неверный формат ввода, попробуйте еще раз!")
        return False
    if not validate_move(input_string, board):
        print("Так походить нельзя!")
        return False
    return True
