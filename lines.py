import sys


def main():
    filename = get_filename()
    lines = read_lines(filename)
    print(count_lines_of_code(lines))


def get_filename():
    # Exactly one command-line argument, and it must be a .py file
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    filename = sys.argv[1]
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")
    return filename


def read_lines(filename):
    # Read all lines of the file; exit if the file does not exist
    try:
        with open(filename) as file:
            return file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")


def is_code(line):
    # A line is code if it is not blank and does not start with # (ignoring spaces)
    stripped = line.strip()
    return stripped != "" and not stripped.startswith("#")


def count_lines_of_code(lines):
    # List comprehension: keep only the lines that are code, then count them
    return len([line for line in lines if is_code(line)])


if __name__ == "__main__":
    main()
