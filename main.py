"""
-> Display the puzzle in a readable format
-> Check each section, row, and column to make sure they adhere to the game's rule
-> Display the error & state the reason why it's invalid
-> Incomplete if it contains any zeroes
"""

class Validator:
    def __init__(self, puzzle):
        # Initialize variables
        self.puzzle = puzzle
        self.status = []

    def validate_rows(self):
        # Iterate through all rows
        for i in range(9):
            # Get a row for each loop
            row = self.puzzle[i]
            # --------- INCOMPLETE ----------
            if 0 in row:
                print(f"ROW {i + 1}: INCOMPLETE - has a '0'")
                self.status.append('INCOMPLETE')  # Add an 'INCOMPLETE' in the list
                # Skip invalid if it's incomplete
                continue
            # --------- DUPLICATES ----------
            if len(set(row)) != 9:  # set() -> unique values
                # Initialize a empty duplicates list
                duplicates = []
                # Iterate through the unique numbers in the row
                for num in set(row):
                    # Check if the number is not zero and appears more than once in the row
                    if num != 0 and row.count(num) > 1:
                        # Add the duplicate number to the list
                        duplicates.append(num)
                if len(duplicates) == 1:
                    print(f"ROW {i + 1}: INVALID - has duplicates of {duplicates[0]}")
                else:  # If more than one duplicate
                    # Join the duplicate numbers as a string
                    dupval = ", ".join(str(num) for num in duplicates)
                    print(f"ROW {i + 1}: INVALID - has duplicates of {dupval}")
                self.status.append('INVALID')  # Add an 'INVALID' in the list
            # --------- OUT OF RANGE ----------
            # If numbers in range 1-9 in ALL rows returns False
            elif not all(1 <= num <= 9 for num in row):
                for num in row:
                    if num < 1 or num > 9:  # Range 1-9
                        print(f"ROW {i + 1}: INVALID - out of range numbers '{num}'")
                self.status.append('INVALID')
            # --------- VALID ----------
            else:
                print(f"ROW {i + 1}: VALID")
                self.status.append('VALID')

            # ---------- DUPLICATES + OUT OF RANGE ----------
            if len(set(row)) != 9 and not all(1 <= num <= 9 for num in row):
                for num in row:
                    if num < 1 or num > 9:
                        # Print out of range only since duplicate is printed first
                        print(f"    -> INVALID - contains out of range number '{num}'")
                self.status.append('INVALID')

        # Return the status
        return self.status

    def validate_columns(self):
        # Iterate through all columns
        for i in range(9):
            # Get a column for each loop
            column = []
            for j in range(9):
                column.append(self.puzzle[j][i])

            # --------- INCOMPLETE ----------
            if 0 in column:
                print(f"COLUMN {i + 1}: INCOMPLETE - has a '0'")
                self.status.append('INCOMPLETE')
                # Skip invalid if it's incomplete
                continue
            # --------- DUPLICATES ----------
            if len(set(column)) != 9:  # set() -> unique values
                # Initialize a empty duplicates list
                duplicates = []
                # Iterate through the unique numbers in the column
                for num in set(column):
                    # Check if the number is not zero and appears more than once in the column
                    if num != 0 and column.count(num) > 1:
                        # Add the duplicate number to the list
                        duplicates.append(num)
                if len(duplicates) == 1:
                    print(f"COLUMN {i + 1}: INVALID - has duplicates of {duplicates[0]}")
                else:  # If more than one duplicate
                    # Join the duplicate numbers as a string
                    dupval = ", ".join(str(num) for num in duplicates)
                    print(f"COLUMN {i + 1}: INVALID - has duplicates of {dupval}")
                self.status.append('INVALID')
            # --------- OUT OF RANGE ----------
            # If numbers in range 1-9 in ALL columns returns False
            elif not all(1 <= num <= 9 for num in column):
                for num in column:
                    if num < 1 or num > 9:  # Range 1-9
                        print(f"COLUMN {i + 1}: INVALID - out of range numbers '{num}'")
                self.status.append('INVALID')
            # --------- VALID ----------
            else:
                print(f"COLUMN {i + 1}: VALID")
                self.status.append('VALID')

            # ---------- DUPLICATES + OUT OF RANGE ----------
            if len(set(column)) != 9 and not all(1 <= num <= 9 for num in column):
                for num in column:
                    if num < 1 or num > 9:
                        # Print out of range only since duplicate is printed first
                        print(f"       -> INVALID - contains out of range number '{num}'")
                self.status.append('INVALID')
        # Return the status
        return self.status

    def validate_sections(self):
        # Initialize a section list
        section = []
        # Iterate over the puzzle in rows of 3
        for i in range(0, 9, 3):
            # Iterate over the puzzle in columns of 3
            for j in range(0, 9, 3):
                # Initialize empty list
                temp_section = []
                # Iterate over the 3 rows in the current 3x3 section
                for k in range(3):
                    # Iterate over the 3 columns in the current 3x3 section
                    for x in range(3):
                        # Append the row and column index
                        temp_section.append(self.puzzle[i + k][j + x])
                # Append the temporary list of values for the current section to the section list
                section.append(temp_section)

        for i in range(9):
            # --------- INCOMPLETE ----------
            if 0 in section[i]:
                print(f"SECTION {i + 1}: INCOMPLETE - has a '0'")
                self.status.append('INCOMPLETE')
                continue
            # --------- DUPLICATES  ----------
            if len(set(section[i])) != 9:
                # Initialize a empty duplicates list
                duplicates = []
                # Iterate through the unique numbers in the section
                for num in set(section[i]):
                    # Check if the number is not zero and appears more than once in the section
                    if num != 0 and section[i].count(num) > 1:
                        # Add the duplicate number to the list
                        duplicates.append(num)
                if len(duplicates) == 1:
                    print(f"SECTION {i + 1}: INVALID - has duplicates of {duplicates[0]}")
                else:  # If more than one duplicate
                    # Join the duplicate numbers as a string
                    dupval = ", ".join(str(num) for num in duplicates)
                    print(f"SECTION {i + 1}: INVALID - has duplicates of {dupval}")
                self.status.append('INVALID')
            # ---------- OUT OF RANGE ---------
            # If numbers in range 1-9 in ALL sections returns False
            elif not all(1 <= num <= 9 for num in section[i]):
                for num in section[i]:
                    if num < 1 or num > 9:
                        print(f"SECTION {i + 1}: INVALID - out of range numbers '{num}'")
                self.status.append('INVALID')
            # --------- VALID ----------
            else:
                print(f"SECTION {i + 1}: VALID")
                self.status.append('VALID')

            # ---------- DUPLICATES + OUT OF RANGE ----------
            if len(set(section[i])) != 9 and not all(1 <= num <= 9 for num in section[i]):
                for num in section[i]:
                    if num < 1 or num > 9:
                        print(f"        -> INVALID - contains out of range number '{num}'")
                self.status.append('INVALID')

        return self.status


def main():
    # Puzzle
    puzzle = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
              [6, 7, 2, 1, 9, 5, 3, 4, 8],
              [1, 9, 8, 3, 4, 2, 5, 6, 7],
              [8, 5, 9, 7, 6, 1, 4, 2, 3],
              [4, 2, 6, 8, 5, 3, 7, 9, 1],
              [7, 1, 3, 9, 2, 4, 8, 5, 6],
              [9, 6, 1, 5, 3, 7, 2, 8, 4],
              [2, 8, 7, 4, 1, 9, 6, 3, 5],
              [3, 4, 5, 2, 8, 6, 1, 7, 9]]

    # Display the puzzle
    print("\n\n───────PUZZLE────────")
    for i in range(len(puzzle)):
        # Initialize an empty string to represent the current row
        row_str = ""
        # Iterate through each cell in the row
        for j in range(len(puzzle)):
            # Convert the cell value to a string and add it to the row string
            row_str += str(puzzle[i][j]) + " "
            # Add a vertical bar on multiples of 3 (excluding the last index)
            if (j + 1) % 3 == 0 and j < 8:
                row_str += "│ "
        # Print the current row
        print(row_str)
        # Add a horizontal bar after every third row (excluding the last index)
        if (i + 1) % 3 == 0 and i < 8:
            print("──────┼───────┼──────")

    # Create the class instance
    validator = Validator(puzzle)

    print("\n\n───────ROWS───────")
    # Store the returned status & call the function
    result1 = validator.validate_rows()

    print("\n───────COLUMNS───────")
    # Store the returned status & call the function
    result2 = validator.validate_columns()

    print("\n───────SECTIONS───────")
    # Store the returned status & call the function
    result3 = validator.validate_sections()

    # Print the overall status of the puzzle
    print("\n───────STATUS───────")

    # Check for each status individually in each result
    if 'INCOMPLETE' in result1 or 'INCOMPLETE' in result2 or 'INCOMPLETE' in result3:
        print('Overall Status: INCOMPLETE')
    elif 'INVALID' in result1 or 'INVALID' in result2 or 'INVALID' in result3:
        print('Overall Status: INVALID')
    else:
        print('Overall Status: VALID')


if __name__ == '__main__':
    main()
