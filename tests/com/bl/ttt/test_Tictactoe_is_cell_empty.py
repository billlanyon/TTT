from com.bl.ttt.tictactoegame import TictactoeGame, TictactoeMove


def test_01_is_cell_empty_identifies_empty_cell():
    g = TictactoeGame()
    g._cells = ['X', 'X', ' ',
               ' ', ' ', ' ',
               ' ', ' ', ' ']
    m = TictactoeMove('O', 2)
    assert (g._is_cell_empty(m))


def test_02_is_cell_empty_identifies_empty_cell():
    g = TictactoeGame()
    g._cells = ['X', 'X', ' ',
               ' ', ' ', ' ',
               ' ', ' ', ' ']
    m = TictactoeMove('O', 7)
    assert g._is_cell_empty(m)


def test_03_is_cell_empty_identifies_occupied_cell():
    g = TictactoeGame()
    g._cells = ['X', 'X', ' ',
               ' ', ' ', ' ',
               ' ', ' ', ' ']
    m = TictactoeMove('O', 1)
    assert not g._is_cell_empty(m)


def test_04_is_cell_empty_identifies_empty_string_cell():
    g = TictactoeGame()
    g._cells = ['X', 'X', ' ',
               ' ', '', ' ',
               ' ', ' ', ' ']
    m = TictactoeMove('O', 4)
    assert not g._is_cell_empty(m)
