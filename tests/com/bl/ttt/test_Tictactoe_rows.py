# Tests is_any_row_complete()
from com.bl.ttt.tictactoe import Tictactoe


def test_01_is_any_row_complete_identifies_complete_row():
	g = Tictactoe()
	g.cells = ['X', 'X', 'X',
			   ' ', ' ', ' ',
			   ' ', ' ', ' ']
	assert g.is_any_row_complete('X')


def test_02_is_any_row_complete_identifies_complete_one_of_two_rows():
	g = Tictactoe()
	g.cells = ['O', 'O', 'O',
			   'X', 'X', 'X',
			   ' ', ' ', ' ']
	assert g.is_any_row_complete('X')


def test_03_is_any_row_complete_identifies_row():
	g = Tictactoe()
	g.cells = ['X', 'X', ' ',
			   ' ', ' ', ' ',
			   ' ', ' ', ' ']
	assert not g.is_any_row_complete('X')


def test_04_is_any_row_complete_identifies_complete_column():
	g = Tictactoe()
	g.cells = ['X', ' ', ' ',
			   'X', ' ', ' ',
			   'X', ' ', ' ']
	assert not g.is_any_row_complete('X')


def test_05_is_any_row_complete_identifies_complete_back_diagonal():
	g = Tictactoe()
	g.cells = ['X', ' ', ' ',
			   ' ', 'X', ' ',
			   ' ', ' ', 'X']
	assert not g.is_any_row_complete('X')


def test_06_is_any_row_complete_identifies_complete_fwd_diagonal():
	g = Tictactoe()
	g.cells = [' ', ' ', 'X',
			   ' ', 'X', ' ',
			   'X', ' ', ' ']
	assert not g.is_any_row_complete('X')


def test_07_is_any_row_complete_identifies_empty_grid():
	g = Tictactoe()
	g.cells = [' ', ' ', ' ',
			   ' ', ' ', ' ',
			   ' ', ' ', ' ']
	assert not g.is_any_row_complete('X')


def test_08_is_any_row_complete_identifies_complete_row_for_wrong_player():
	g = Tictactoe()
	g.cells = ['X', 'X', 'X',
			   ' ', ' ', ' ',
			   ' ', ' ', ' ']
	assert not g.is_any_row_complete('O')


def test_09_is_any_row_complete_identifies_complete_row_for_symbol_other_than_x_or_o():
	g = Tictactoe()
	g.cells = ['A', 'A', 'A',
			   ' ', ' ', ' ',
			   ' ', ' ', ' ']
	assert not g.is_any_row_complete('O')