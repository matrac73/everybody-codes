"""Run an Everybody Codes quest: python run.py <event> <quest> [-p PART]."""
import argparse
import importlib
from pathlib import Path

ROOT = Path(__file__).parent


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("event")
    parser.add_argument("quest", type=int)
    parser.add_argument("-p", "--part", type=int, choices=(1, 2, 3))
    args = parser.parse_args()

    module = importlib.import_module(f"solutions.e{args.event}.q{args.quest:02d}")
    for part in [args.part] if args.part else (1, 2, 3):
        notes = ROOT / "inputs" / args.event / f"q{args.quest:02d}_p{part}.txt"
        if not notes.exists():
            print(f"part {part}: missing {notes.relative_to(ROOT)}")
            continue
        solve = getattr(module, f"part{part}", None)
        print(f"part {part}: {solve(notes.read_text().strip()) if solve else 'not solved'}")


if __name__ == "__main__":
    main()