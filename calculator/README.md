# Calculator App

This is a simple command-line calculator application built with Python. It allows users to evaluate mathematical expressions directly from the terminal.

## Usage

To run the calculator, execute the `main.py` file with your desired mathematical expression enclosed in quotes.

```bash
python main.py "3 + 5"
```

### Examples

- Addition:
  ```bash
  python main.py "10 + 2"
  ```

- Subtraction:
  ```bash
  python main.py "15 - 7"
  ```

- Multiplication:
  ```bash
  python main.py "4 * 6"
  ```

- Division:
  ```bash
  python main.py "20 / 4"
  ```

- Complex Expressions:
  ```bash
  python main.py "(3 + 5) * 2 - 1"
  ```

## Error Handling

The calculator will display an error message if the expression is invalid or empty.

```bash
python main.py ""
# Output: Error: Expression is empty or contains only whitespace.
```

```bash
python main.py "3 + "
# Output: Error: Invalid expression
```
