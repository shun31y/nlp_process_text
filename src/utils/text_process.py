from .regex import (
    captured_group,
    uncaptured_group,
    concat_regex,
    follow_regex,
    not_follow_regex,
    precede_regex,
    not_precede_regex,
)
import re
import demoji


def remove_inline(text: str) -> str:
    return text.replace("\n", "").replace("\r", "")


def remove_url(text: str) -> str:
    cleansed = re.sub(
        r"(https?|ftp)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+\$,%#]+)", "", text
    )
    cleansed = re.sub(
        r"(http?|ftp)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+\$,%#]+)", "", cleansed
    )
    return cleansed


def remove_emoji(text: str) -> str:
    return demoji.replace(string=text, repl="")


def remove_empty_lines(text: str) -> str:
    cleansed = re.sub(r"\n+", "\n", text)
    cleansed = cleansed.strip()
    return cleansed


def insert_newline_after_regex(text: str, regexes: list[str]) -> str:
    regexes = concat_regex(regexes)
    cleansed = re.sub(follow_regex(regex="", regex_obj=regexes), "\n", text)
    return cleansed


def insert_newline_before_regex(text: str, regexes: list[str]) -> str:
    regexes = concat_regex(regexes)
    cleansed = re.sub(precede_regex(regex="", regex_obj=regexes), "\n", text)
    return cleansed
