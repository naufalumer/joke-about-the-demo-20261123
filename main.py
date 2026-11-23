"""The joke about the demo (make.fun, the-joke-about-the-demo-20261123-0112).

Writes one one-line joke about working beside an AI coding agent to
$MAKEFUN_OUTPUT_DIR/entry.txt. Standard library only, deterministic, no
network, no model call: the joke is a fixed text, so two runs produce
byte-identical output.
"""

import os
from pathlib import Path

JOKE = (
    "My agent demoed the fix live, showed the bug instead, flawlessly, "
    "twice, and asked if I wanted to see it again in slow motion."
)


def main() -> None:
    if not 1 <= len(JOKE) <= 280:
        raise SystemExit("joke must be 1 to 280 characters")
    text = JOKE.strip()
    if not text:
        raise SystemExit("joke must not be only whitespace")
    if len(text) != len(JOKE):
        raise SystemExit("joke must not need trimming")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
