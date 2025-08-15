import os

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

    def append(self, text_to_append: str):
        """
        Appends a given string to the file.

        Args:
            text_to_append (str): The text to append to the file.
        """
        try:
            # Open the file in append mode ('a')
            with open(self.file_path, 'a', encoding='utf-8') as f:
                f.write(text_to_append)
                print(f"\nSuccessfully appended text to '{self.file_path}'.")
        except FileNotFoundError:
            print(f"Error: The file '{self.file_path}' was not found.")
        except Exception as e:
            print(f"An unexpected error occurred during append: {e}")

    def read_and_display(self):
        """Reads and prints the content of the file."""
        print(f"\n--- Content of {self.file_path} ---")
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines:
                    # rstrip() is a safer way to remove trailing newline characters
                    print(line.rstrip('\n'))
        except FileNotFoundError:
            print(f"Error: The file '{self.file_path}' was not found.")
        except Exception as e:
            print(f"An unexpected error occurred while reading: {e}")
        print("--- End of Content ---")


def main():
    file_path = '/Users/zw/Documents/GitHub/python-learning/week3/demo.txt'
    file_op = FileOperator(file_path)

    # 1. Read and display the content of demo.txt
    file_op.read_and_display()

    # 2. Append new text to demo.txt
    new_content = "\n\n--- This is appended text. ---\n"
    file_op.append(new_content)

    # 3. Read and display the final content of the file to show the change
    file_op.read_and_display()


if __name__ == "__main__":
    main()
