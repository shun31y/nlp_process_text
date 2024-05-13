from ..utils.regex import (
    concat_regex,
    follow_regex,
    precede_regex,
)
import re
import demoji
import unicodedata


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


def full_to_half_width(text: str) -> str:
    return unicodedata.normarize("NFKC", text)


def remove_full_width_symbol(text: str) -> str:
    """全角記号を削除する関数。削除できる全角文字は以下の通り
    全角の ！"＃＄％＆'（）＊＋，－．／
    全角の ：；＜＝＞？＠
    全角の ［＼］＾＿｀
    全角の ｛｜｝～
    CJKの記号と句読点 、。〃〄々〆〇〈〉《》「」『』【】〒〓〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿
    全角スペース

    Args:
        text (str): 処理前のテキスト

    Returns:
        str: 削除されたテキスト。
    """
    return re.sub(
        "[\uFF01-\uFF0F\uFF1A-\uFF20\uFF3B-\uFF40\uFF5B-\uFF65\u3000-\u303F]", "", text
    )


def convert_fullwidth_space_to_halfwidth(text: str) -> str:
    return re.sub(r"\u3000", " ", text)
