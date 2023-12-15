def main():
    # Prompt the user for input
    filename = input("Enter a filename: ")
    
    old_string = input("Enter the old string to be replaced: ")
    new_string = input("Enter the new string to replace the old string: ")

    # Check if both strings are the same
    if old_string == new_string:
        print("The old and new strings are the same. No change will be made.")
        return

    # Initialize an empty string for the new content
    new_content = ""

    try:
        # Attempt to open the file
        with open(filename, "r") as file:
            # Read and replace string in the file
            for line in file:
                new_line = line.replace(old_string, new_string)
                new_content += new_line

        # Write the new content back to the file
        with open(filename, "w") as file:
            file.write(new_content)

        print("Done")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error occurred while reading/writing file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()