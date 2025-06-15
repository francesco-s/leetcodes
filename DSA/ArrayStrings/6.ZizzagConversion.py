def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s

    rows = [''] * numRows

    # Initialize the variables to traverse the string
    current_row = 0
    going_down = False

    # Traverse the input string
    for char in s:
        rows[current_row] += char
        if current_row == 0 or current_row == numRows - 1:
            going_down = not going_down
        current_row += 1 if going_down else -1

    # Concatenate all rows to form the final string
    return ''.join(rows)


print(convert("PAYPALISHIRING", 3))  # Output: "PAHNAPLSIIGYIR"
print(convert("PAYPALISHIRING", 4))  # Output: "PAHNAPLSIIGYIR"
print(convert("A", 1))  # Output: "A"
