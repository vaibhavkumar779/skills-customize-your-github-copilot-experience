def read_file_lines(filepath):
    """Read a text file and return a list of cleaned lines."""
    lines = []
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            lines.append(line.strip())
    return lines


def count_text_stats(lines):
    """Return line, word, and character counts for a list of lines."""
    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)
    char_count = sum(len(line) for line in lines)
    return {
        "lines": line_count,
        "words": word_count,
        "characters": char_count,
    }


def replace_text(lines, target, replacement):
    """Return a new list of lines with the target word replaced."""
    return [line.replace(target, replacement) for line in lines]


if __name__ == "__main__":
    filepath = "sample-text.txt"
    lines = read_file_lines(filepath)
    stats = count_text_stats(lines)
    print(f"Lines: {stats['lines']}")
    print(f"Words: {stats['words']}")
    print(f"Characters: {stats['characters']}")
    updated_lines = replace_text(lines, "Python", "FastAPI")
    print("\nUpdated text sample:")
    for line in updated_lines[:5]:
        print(line)
