def get_file_stats(filename):
    """
    Get statistics about a text file.

    Parameters:
        filename (str): Name of the file to analyze

    Returns:
        dict: Dictionary with 'lines', 'words', and 'characters' counts.
        Returns None if file doesn't exist.
    """

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

            line_count = len(lines)
            word_count = sum(len(line.split()) for line in lines)
            char_count = sum(len(line) for line in lines)

            return {
                'lines': line_count,
                'words': word_count,
                'characters': char_count
            }

    except FileNotFoundError:
        return None

stats = get_file_stats("test.txt")

if stats:
    print(f"Lines: {stats['lines']}")
    print(f"Words: {stats['words']}")
    print(f"Characters: {stats['characters']}")
else:
    print("File not found.")
