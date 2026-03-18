# ASCII Printer

A Python library to print text in ASCII Art format with multiple fonts and ANSI colors.
Perfect for creating banners, decorative titles, and ASCII art text in command-line applications.

## Features

- **Multiple ASCII fonts** - Choose from 10 different fonts (doom, epic, starwars, standard, big, small, and more)
- **ANSI color support** - Customize the color of your ASCII text (red, green, blue, yellow, magenta, cyan, white)
- **Terminal size adaptive** - Automatically detects your terminal width
- **Easy to use** - Simple and intuitive API
- **Lightweight** - No external dependencies

## Installation

### Requirements

- Python 3.6 or higher
- Operating System: Linux, macOS, or Windows

### From the repository

```bash
# Clone the repository
git clone <REPOSITORY_URL>
cd ASCII_printer

# (Optional) Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install the library
pip install -e .
```

# Usage

```bash
#!/usr/bin/env python3

from ascii import ascii_printer

# Print simple text
ascii_printer(text="HELLO")

# Print with specific font
ascii_printer(text="HELLO", font_name="doom")

# Print with color
ascii_printer(text="HELLO", font_name="doom", color_name="green")
```


# Available Fonts 
| Font        | Description                          |
|-------------|--------------------------------------|
| big         | Large and clear font                 |
| doh         | Rounded font                         |
| doom        | Classic video game style font        |
| epic        | Epic font with details               |
| small       | Compact font                         |
| smkeyboard  | Keyboard-style font                  |
| speed       | Dynamic font                         |
| standard    | Standard ASCII font                  |
| starwars    | Star Wars style font                 |


# Available Colors
| Color    | ANSI Code       |
|----------|-----------------|
| red      | Red             |
| green    | Green (Default) |
| white    | White           |
| yellow   | Yellow          |
| blue     | Blue            |
| magenta  | Magenta         |
| cyan     | Cyan            |




# System Requirements 
- ANSI compatible terminal (Linux, macOS, Windows 10+)
- Python 3.6+
- No external dependencies required

# License
This project is licensed under the GNU General Public License v3.0 (GPLv3). See the LICENSE file for details.

# Contributing
Contributions are welcome. To contribute:

1. Fork the project
2. Create a branch for your feature (git checkout -b feature/new-feature)
3. Commit your changes (git commit -am 'Add new feature')
4. Push to the branch (git push origin feature/new-feature)
5. Open a Pull Request