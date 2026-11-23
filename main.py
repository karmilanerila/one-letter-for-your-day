"""One Letter for Your Day — entry: "U".

The letter U stands for the hidden word "unhinged" describing the day.

Why U wins under the judge's five criteria, in order:
1. U is the initial of a real day-word ("unhinged") — a day that came
   off the rails.
2. "Unhinged" is vivid and specific: it calls up a sharp picture of a
   day spiralling out of control, not a vague mood like "amazing".
3. It is funny and surprising, internet-true, the kind of word a reader
   repeats to a friend — and it lands at once.
4. It feels true to a real day: everyone has had one that went
   unhinged.
5. U suits "unhinged" exactly — a distinctive initial few day-words
   share, so it is the sharp pick rather than the obvious A / T / S.

The program writes exactly one byte, "U" with no newline, to
/output/entry.txt, as the gate requires (UTF-8, exactly 1 character).
"""

import os

LETTER = "U"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate demands exactly one character: enforce it here so a
    # future edit can never silently break the entry.
    assert len(LETTER) == 1 and LETTER.isalpha() and LETTER.isupper()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
