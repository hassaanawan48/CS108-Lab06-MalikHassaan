# Lab06 Calculator

## Purpose

A simple command-line calculator written in Python, created as part of **CS-108 Lab 06** to practice the Git and GitHub workflow — including commits, branching, pull requests, code review, and merge conflict resolution.

## Features

- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`) — with division-by-zero handling
- Power (`^`)
- Modulus (`%`) — with modulus-by-zero handling
- Input validation for non-numeric entries

## How to Run

Make sure **Python 3** is installed, then run:

```bash
python calculator.py
```

## Example Input/Output

```
=== Simple Calculator ===
Operations: +, -, *, /, ^ (power), % (modulus)
Enter first number: 2
Enter operator (+, -, *, /, ^, %): ^
Enter second number: 3
Result: 8.0
```

Another example:

```
=== Simple Calculator ===
Operations: +, -, *, /, ^ (power), % (modulus)
Enter first number: 10
Enter operator (+, -, *, /, ^, %): /
Enter second number: 0
Result: Error: Division by zero
```

## Project Structure

```
Lab06_Git/
├── calculator.py     # Main Python program
├── README.md         # Project documentation (this file)
└── .gitignore        # Files Git should ignore
```

## Author

- **Name:** Malik Hassaan
- **Registration No:** 460233
- **Program:** BS Computer Science
- **Institute:** SEECS
- **Email:** mhassaan.bscs23seecs@seecs.edu.pk

## Version Control

This project uses **Git** for local version control and **GitHub** for remote hosting and collaboration. The development workflow followed:

1. Initialize local repository
2. Commit changes with meaningful messages
3. Push to GitHub
4. Create a feature branch for new work
5. Open a Pull Request and request review
6. Merge after approval
7. Resolve merge conflicts intentionally

## Course Information

- **Course:** CS-108 — Introduction to ICT
- **Lab:** Lab 06 — Git & GitHub: Version Control and Collaborative Development