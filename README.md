# make_perforated_text

穴開き文を自動生成するプログラムです。

## Requirements

- python3.x (3.9.xを推奨)

## Installation

```sh
# HTTPS
git clone https://github.com/Futaba-Kosuke/make_perforated_text.git

# SSH
git clone git@github.com:Futaba-Kosuke/make_perforated_text.git
```

## Usage

```sh
# 通常版（穴開き数15）
python main.py -f {$target_file_path}

# 穴開き数を指定
python main.py -f {$target_file_path} -p {$dictation_quantity}

# examples
python main.py -f data/8_3.txt
python main.py -f data/8_3.txt -p 10
```