import sys
from pathlib import Path

class Lox:

    had_error: bool = False

    @staticmethod
    def run(source: str) -> None:
        print(source)

    @staticmethod
    def run_file(path: Path) -> None:
            Lox.run(path.read_text())
            if Lox.had_error:
                sys.exit(65)

    @staticmethod
    def run_prompt() -> None:
        print("Running REPL...")
        while True:
            try:
                Lox.run(input(">> "))
                Lox.had_error = False
            except EOFError:
                break

    @staticmethod
    def error(line: int, message: str) -> None:
        Lox.report(line, "", message)

    @staticmethod
    def report(line: int, where: str, message: str) -> None:
        print(f"[line {line}] Error {where}: {message}", file=sys.stderr)
        Lox.had_error = True

    @staticmethod
    def main() -> None:
        if len(sys.argv) > 2:
            print("Too many arguments usage should be: pylox [file]")
            sys.exit(64)
        elif len(sys.argv) == 2:
            Lox.run_file(Path(sys.argv[1]))
        else:
            Lox.run_prompt()

if __name__ == "__main__":
    Lox().main()
