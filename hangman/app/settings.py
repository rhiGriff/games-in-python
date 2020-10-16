import os
import sys
from structlog import wrap_logger
import logging

log = wrap_logger(logging.getLogger())

if (level := os.environ.get("LOG", "INFO")) not in [
    "INFO",
    "DEBUG",
]:
    print(f"Unsupported logging level, must be INFO or DEBUG. Got {level}")
    sys.exit(1)

logging.basicConfig(
    format="%(message)s", stream=sys.stdout, level=os.environ.get("LOG", level),
)

if level == "DEBUG":
    log.debug("Debug logging ON")


# Default to unix word list unless overridden
WORDLIST = os.environ.get("WORDLIST", "/usr/share/dict/words")
log.debug(f"Using wordlist from '{WORDLIST}'")

MIN_WORD_LENGTH = os.environ.get("MIN", 3)
MAX_WORD_LENGTH = os.environ.get("MAX", 7)

CHEAT = os.environ.get("CHEAT", False)

