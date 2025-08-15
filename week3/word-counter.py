import os

def words_of_line(line: str):
    words_count = line.strip().split(' ')
    return words_count.__len__()

class FileOperator:
    """
    A class to handle file operations like reading and appending
    to a single file.
    """
    def __init__(self, file_path: str):
        """
        Initializes the FileOperator with the file path.

        Args:
            file_path (str): The path to the file to be operated on.
        """
        self.file_path = file_path


    def read_and_display(self):
        """Reads and prints the content of the file."""
        print(f"\n--- Content of {self.file_path} ---")
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                count = 0
                for line in lines:
                    count += words_of_line(line)
                print('words of the file:', count)
        except FileNotFoundError:
            print(f"Error: The file '{self.file_path}' was not found.")
        except Exception as e:
            print(f"An unexpected error occurred while reading: {e}")


def main():
    file_path = '/Users/zw/Documents/GitHub/python-learning/week3/demo.txt'
    file_op = FileOperator(file_path)

    # 1. Read and display the content of demo.txt
    file_op.read_and_display()


if __name__ == "__main__":
    main()
