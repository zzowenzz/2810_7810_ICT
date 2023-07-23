import sys

def parse_text_histogram(text):
    word_counts = {}
    total_count = 0

    # Split the text into lines
    lines = text.strip().split('\n')

    # Process each line and count the words
    for line in lines:
        word, count = line.split()
        count = int(count)
        word_counts[word] = count
        total_count += count

    # Calculate and print histogram for each word
    for word, count in word_counts.items():
        percentage = (count / total_count) * 100
        stars_count = int((count / total_count) * 24)
        histogram = f"{word.ljust(5)} [{'*' * stars_count:<6}] {percentage:.0f}%"
        print(histogram)

# Read input from stdin and call the function
if __name__ == "__main__":
    input_text = sys.stdin.read()
    parse_text_histogram(input_text)
