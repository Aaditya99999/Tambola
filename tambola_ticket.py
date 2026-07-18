import random
import string
import datetime

HOST_NAME = "Beautiful Women's Group"

# Column number ranges: col 0 -> 1-9, col 1 -> 10-19, ..., col 8 -> 80-90
COLUMN_RANGES = [(1, 9)] + [(10 * i, 10 * i + 9) for i in range(1, 8)] + [(80, 90)]


def generate_column_counts():
    """Pick how many numbers (1-3) each of the 9 columns gets, summing to 15."""
    while True:
        counts = [random.randint(1, 3) for _ in range(9)]
        if sum(counts) == 15:
            return counts


def assign_rows(counts):
    """Decide which rows (0-2) hold a number for each column, so every row ends up with 5 numbers."""
    while True:
        row_has_col = [[] for _ in range(3)]  # row -> list of column indices
        col_rows = []  # column -> list of row indices
        for col_count in counts:
            rows = random.sample(range(3), col_count)
            col_rows.append(rows)
            for r in rows:
                row_has_col[r].append(len(col_rows) - 1)
        if all(len(cols) == 5 for cols in row_has_col):
            return col_rows


def generate_ticket():
    counts = generate_column_counts()
    col_rows = assign_rows(counts)

    grid = [["" for _ in range(9)] for _ in range(3)]

    for col_index, rows in enumerate(col_rows):
        low, high = COLUMN_RANGES[col_index]
        numbers = sorted(random.sample(range(low, high + 1), len(rows)))
        for row_index, number in zip(sorted(rows), numbers):
            grid[row_index][col_index] = str(number)

    return grid


def generate_verification_code():
    date_part = datetime.datetime.now().strftime("%Y%m%d")
    random_part = "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"{date_part}-{random_part}"


def print_ticket(grid, host_name, verification_code):
    col_width = 4
    border = "+" + ("-" * col_width + "+") * 9

    print(f"Host: {host_name}")
    print(f"Verification Code: {verification_code}")
    print(border)
    for row in grid:
        line = "|"
        for cell in row:
            line += cell.center(col_width) + "|"
        print(line)
        print(border)


if __name__ == "__main__":
    ticket = generate_ticket()
    verification_code = generate_verification_code()
    print_ticket(ticket, HOST_NAME, verification_code)
