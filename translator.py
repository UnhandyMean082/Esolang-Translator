import re


colcode = {
    "Christ's": "iin",
    "Churchill": "add_mem",
    "Clare": "iout",
    "Clare Hall": "cout",
    "Corpus Christi": "cin",
    "Darwin": "(Darwin)",
    "Downing": "subtr_mem",
    "Emmanuel": "bin",
    "Fitzwilliam": "(Fitzwilliam)",
    "Girton": "store_mem",
    "Gonville & Caius": "(Gonville & Caius)",
    "Homerton": "(Homerton)",
    "Hughes Hall": "(Hughes Hall)",
    "Jesus": "jump",
    "King's": "incr",
    "Lucy Cavendish": "(Lucy Cavendish)",
    "Magdalene": "read_mem",
    "Murray Edwards": "(Murray Edwards)",
    "Newnham": "prt_line",
    "Pembroke": "(Pembroke)",
    "Peterhouse": "(Peterhouse)",
    "Queens'": "decr",
    "Robinson": "(Robinson)",
    "Selwyn": "(Selwyn)",
    "Sidney Sussex": "(Sidney Sussex)",
    "St Catharine's": "(St Catharine's)",
    "St Edmund's": "(St Edmund's)",
    "St John's": "return",
    "Trinity": "1",
    "Trinity Hall": "0",
    "Wolfson": "(Wolfson)",
}


def normalize_text(text: str) -> str:
    if not isinstance(text, str):
        return text

    text = text.replace("\u2019", "'")
    text = text.replace("\u2018", "'")
    text = text.replace("\u02BC", "'")
    text = text.replace("\u201B", "'")
    text = text.replace("\u201C", '"').replace("\u201D", '"')
    text = text.replace("\u2013", "-").replace("\u2014", "-")
    text = text.replace("\u00A0", " ")
    text = re.sub(r"[ \t\f\v]+", " ", text)

    return text


def replace_mapping(text: str, mapping: dict, reverse: bool = False) -> str:
    items = list(mapping.items())
    if reverse:
        items = [(v, k) for k, v in items]

    items.sort(
        key=lambda kv: len(kv[0]) if kv and kv[0] is not None else 0, reverse=True
    )

    for key, val in items:
        if not key:
            continue

        pattern = r"(?<!\w)" + re.escape(key) + r"(?!\w)"
        text = re.sub(pattern, val, text)

    return text


if __name__ == "__main__":
    mode = int(
        input("0 for translate from Cambridge to code, 1 for code to Cambridge: ")
    )

    if mode:
        text = input("Enter code: ")
        text = normalize_text(text)
        text = replace_mapping(text, colcode, reverse=True)
        print(text)
    else:
        q = input("Enter which question: ")

        with open(f"q{q}.txt", "r") as f:
            text = f.read()
            text = normalize_text(text)
            text = replace_mapping(text, colcode, reverse=False)
            print(text)
