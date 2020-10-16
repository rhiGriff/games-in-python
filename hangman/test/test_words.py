from app.words import Words
import app.settings
import pytest
import os
import re


@pytest.fixture()
def game():
    return Words()


def test_display(game):
    game.new_game()
    # Basic check the structure of the output
    assert re.match(r"([ ╬═║╩│\n]*)[\w░](\.[\w░])+\s*\[.*\]", game.display())

