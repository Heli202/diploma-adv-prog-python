# Generator to preprocess and stream lines
def get_lines(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()

line_generator = get_lines("large_data.txt")

# get lines using next() - pagination
for _ in range(1000):
    print(next(line_generator))