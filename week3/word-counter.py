import os

def words_of_line(line: str):
    words_count = line.strip().split()
    return words_count.__len__()

class FileOperator:
    def __init__(self, file_path: str):
        self.file_path = file_path


    def read_and_display(self):
        print(f"\n--- Content of {self.file_path} ---")
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                count = 0
                for line in lines:
                    count += words_of_line(line)
                print('words of the file:', count)
                f.close()
        except FileNotFoundError:
            print(f"Error: The file '{self.file_path}' was not found.")
        except Exception as e:
            print(f"An unexpected error occurred while reading: {e}")


def main():
    file_path = 'week3/demo.txt'
    file_op = FileOperator(file_path)

    # 1. Read and display the content of demo.txt
    file_op.read_and_display()


if __name__ == "__main__":
    main()
