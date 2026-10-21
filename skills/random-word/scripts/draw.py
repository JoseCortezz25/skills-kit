#!/usr/bin/env python3
"""Draw a random stimulus for the random-word technique (Edward de Bono).

Why this exists: a language model does not pick at random. It drifts toward
"creative" words or words that already fit the focus, which defeats the
technique. This script uses the operating system's cryptographic generator
(`secrets`), so nobody with a prior idea of the focus chooses the word.

Usage:
    python3 draw.py                          # one word
    python3 draw.py --focus "shoe design"
    python3 draw.py --n 3                    # several, for separate sessions
    python3 draw.py --physical-object        # formal rule for picking a real object
    python3 draw.py --json                   # machine-readable output
    python3 draw.py --file my_words.txt

Design choices:
- With --focus, only words that appear literally in the focus are excluded
  (if the focus is "shoes", "shoe" cannot come up). Nothing is filtered by
  relevance, because that would be choosing the stimulus, and choosing it
  beforehand cancels the effect.
- There is deliberately no "draw again" option inside a session: the
  technique says to work with the first word, not to hunt for the best fit.
"""

import argparse
import json
import secrets
import sys
import unicodedata
from pathlib import Path

DEFAULT_LIST = Path(__file__).resolve().parent.parent / "references" / "words.txt"

# Formal rules for picking a physical object without choosing it by hand.
COLORS = ["red", "blue", "green", "yellow", "white", "black", "brown", "gray", "orange"]
COLOR_RULES = [
    "the {c} object closest to you",
    "the third {c} object you see when you look to your right",
    "the smallest {c} object you can reach without standing up",
    "the {c} object that is highest up in the room",
]
POSITION_RULES = [
    "the third book on the top shelf, counting from right to left",
    "the first thing you touch in the second drawer of your desk",
    "the fifth item you see when you open the fridge door",
    "whatever is at the far left of your pocket or bag",
]


def normalize(text: str) -> str:
    """Lowercase and strip accents, to compare against the focus."""
    decomposed = unicodedata.normalize("NFD", text.lower())
    return "".join(ch for ch in decomposed if unicodedata.category(ch) != "Mn")


def load_words(path: Path) -> list[str]:
    if not path.exists():
        sys.exit(f"Word list not found: {path}")
    words = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            words.append(line)
    if not words:
        sys.exit("The word list is empty.")
    return words


def exclude_by_focus(words: list[str], focus: str) -> list[str]:
    """Drop only the words that already appear literally in the focus."""
    if not focus:
        return words
    cleaned = normalize(focus)
    for ch in ",.;:!?()\"'":
        cleaned = cleaned.replace(ch, " ")
    tokens = set(cleaned.split())
    kept = []
    for w in words:
        wn = normalize(w)
        # Exact match, or a shared stem (shoe / shoes).
        if wn in tokens or any(
            len(t) > 3 and len(wn) > 3 and (t.startswith(wn) or wn.startswith(t))
            for t in tokens
        ):
            continue
        kept.append(w)
    return kept or words


def physical_object_rule() -> str:
    if secrets.randbelow(2) == 0:
        return secrets.choice(COLOR_RULES).format(c=secrets.choice(COLORS))
    return secrets.choice(POSITION_RULES)


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument(
        "--n", type=int, default=1, help="how many words to draw (default 1)"
    )
    ap.add_argument(
        "--focus", default="", help="focus text, used only to exclude literal matches"
    )
    ap.add_argument(
        "--file",
        type=Path,
        default=DEFAULT_LIST,
        help="custom word list (one word per line)",
    )
    ap.add_argument(
        "--physical-object",
        action="store_true",
        help="return a formal rule for picking a real object",
    )
    ap.add_argument("--json", action="store_true", help="JSON output")
    args = ap.parse_args()

    if args.physical_object:
        rules = [physical_object_rule() for _ in range(max(1, args.n))]
        if args.json:
            print(
                json.dumps(
                    {"mode": "physical_object", "rules": rules}, ensure_ascii=False
                )
            )
        else:
            for r in rules:
                print(f"Pick: {r}")
        return

    everything = load_words(args.file)
    candidates = exclude_by_focus(everything, args.focus)
    n = max(1, min(args.n, len(candidates)))

    # SystemRandom.sample = sampling without replacement using system entropy.
    drawn = secrets.SystemRandom().sample(candidates, n)

    if args.json:
        print(
            json.dumps(
                {"mode": "word", "words": drawn, "pool_size": len(candidates)},
                ensure_ascii=False,
            )
        )
    else:
        for w in drawn:
            print(w)
        print(f"(drawn from {len(candidates)} words)", file=sys.stderr)


if __name__ == "__main__":
    main()
