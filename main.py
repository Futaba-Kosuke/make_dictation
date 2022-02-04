import argparse
import random
from typing import List

if __name__ == "__main__":
    # 入力用パーサーを生成
    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", "-f", type=str, required=True)
    parser.add_argument("--dictation_quantity", "-d", default=15, type=int)

    # ファイル名取得
    args = parser.parse_args()
    filename: str = args.filename
    dictation_quantity: int = args.dictation_quantity

    # ファイル読み込み
    with open(filename, "r") as f:
        # ファイル読み込み
        words: List[str] = f.read().split()

    # 穴開き箇所の生成
    indexes: List[int] = list(range(0, len(words)))
    dictations: List[int] = sorted(random.sample(indexes, dictation_quantity))

    # 穴開け実行
    for i, dictation in enumerate(dictations):
        if "." == words[dictation][-1]:
            words[dictation] = f"( {i + 1} )."
        elif "," == words[dictation][-1]:
            words[dictation] = f"( {i + 1} ),"
        elif "!" == words[dictation][-1]:
            words[dictation] = f"( {i + 1} )!"
        elif "?" == words[dictation][-1]:
            words[dictation] = f"( {i + 1} )?"
        elif ":" == words[dictation][-1]:
            words[dictation] = f"( {i + 1} ):"
        else:
            words[dictation] = f"( {i + 1} )"

    # 結合
    result: str = " ".join(words)
    print(result)
