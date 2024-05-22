from converter import convert


def main(input_file, output_file):
    with open(input_file, 'r') as file:
        input_text = file.read()

    result = convert(input_text)

    with open(output_file, 'w') as file:
        file.write(result)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python main.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)
