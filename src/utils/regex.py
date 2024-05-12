def captured_group(regex: str) -> str:
    """キャプチャグループを作成する関数

    Args:
        regex (str): 正規表現パターン

    Returns:
        str:キャプチャパターン。文字列がマッチした場合パターンのキャプチャを行うことができる
    """
    return r"(" + regex + r")"


def uncaptured_group(regex: str) -> str:
    """非キャプチャグループを作成する関数

    Args:
        regex (str): 正規表現パターン

    Returns:
        str:非キャプチャパターン。文字列がマッチした場合でもパターンのキャプチャを行わない。
    """
    return r"(?:" + regex + r")"


def follow_regex(regex: str, regex_obj: str) -> str:
    """特定テンプレートの後にパターンが来るようなパターンについて作成する関数

    Args:
        regex (str): 正規表現パターン
        regex_obj (str): regexの前に来る正規表現パターン

    Returns:
        str: regex_obj+regexとなるようなregexをマッチするような正規表現パターン。regex_objは固定長さでないといけない。
    """
    return r"(?<=" + regex_obj + r")" + regex


def concat_regex(regexes: list[str]) -> str:
    """正規表現パターンを「または」で繋ぎ、新しいパターンを作成する関数

    Args:
        regexes (list[str]): orで繋ぎたいパターンのリスト

    Returns:
        str: リストに記述されたパターンをまたはで繋いだパターン。非キャプチャ。
    """
    _regex = r"|".join(regexes)
    _regex = uncaptured_group(_regex)
    return _regex