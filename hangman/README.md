# Hangman

A simple implementation of a hangman style game in python

```shell
 ╬═══╬═
 ║   │
 ║   O
 ║  /|\
 ║  / \
═╩══════
```

## Pre-requisites

- Python 3+
- Pipenv

## Get started

```shell
cd hangman
pipenv install
pipenv run python app/hangman_cli.py
```

By default, it will try to use the default unix word list located on *nix based
systems at `/usr/share/dict/words`. If you want to supply your own word list, this
will be a plain ascii text file with one word per line. Put the path to your
word list in `WORDLIST`

For example:

```shell
echo "cat\ndog\nsheep\nfox" > mywords
WORDLIST=mywords pipenv run python app/hangman_cli.py
```

### Environment Vars

The game supports the following enviroment vars:

| Env var         | Default                 | Description                                                   |
| --------------- | ----------------------- | ------------------------------------------------------------- |
| LOG             | `INFO`                  | Set the logging level - supports `INFO` and `DEBUG`           |
| MIN_WORD_LENGTH | `3`                     | Words under this length will be filtered out of the word list |
| MAX_WORD_LENGTH | `7`                     | Words over this length will be filtered out of the word list  |
| WORDLIST        | `/usr/share/dict/words` | Word list to use (newline delimited)                          |
| CHEAT           | `False`                 | Switch on to be told what the word you're guessing is!        |

## Run tests

```shell
cd hangman
pipenv install --dev
make test
```
