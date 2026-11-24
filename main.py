"""Funniest Autocorrect Fail — make.fun entry.

Writes one line (under 200 characters) to /output/entry.txt: a single
autocorrect fail, nothing else.

The line, chosen from a dozen candidates for the judge's brief:
- the wrong word ("quilt") is clear, surprising, specific and original;
- the slip reads as a real autocorrect ("quit" -> "quilt" is one letter);
- the joke lands on first read, no explanation needed;
- HR's reply is the second beat, so the line escalates instead of
  stopping at one neat twist.
"""

import os

# The line is built from its three beats so the escalation is visible in
# the code: the setup, the slip, then HR's reply that lands the joke.
_SETUP = "I texted my boss 'I quit' and autocorrect sent 'I quilt'"
_REPLY = "HR replied 'we look forward to your blanket.'"
LINE = _SETUP + " \u2014 " + _REPLY


def main() -> None:
    text = LINE
    assert 1 <= len(text) <= 199, f"entry must be 1-199 chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
