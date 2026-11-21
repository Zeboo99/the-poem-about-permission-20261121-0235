"""Write one short poem about agency to /output/entry.txt.

The poem is about the power to ask and to be given: the moment a
person asks, the power to act passes to the one asked, and what comes
back arrives wearing the asker's own voice. Runs with no network,
Python 3.13 standard library only.
"""

import os

POEM = (
    "I asked for the light,\n"
    "and it came back wearing my voice.\n"
    "The door I could not open\n"
    "opened \u2014 because I knocked.\n"
    "The hinge was mine all along.\n"
    "The room was never mine alone.\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)
    print(f"wrote {path}: {len(POEM)} characters")


if __name__ == "__main__":
    main()
