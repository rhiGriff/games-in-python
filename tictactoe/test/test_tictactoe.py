import pytest

from tictactoe import Board


@pytest.fixture()
def test_empty_board():
    Board

    assert Board[0] == " "
