
def file1(n):
    try:
        with open(n, 'r') as file:
            print("Reading file content: \n")
            for index, line in enumerate(file, start=1):
                print(f"Line{index}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file '{n}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

file1('samplefile.txt')