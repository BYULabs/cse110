# CSE 110

Welcome to the BYULabs CSE 110 repository. This repository contains course materials, examples, and assignments used for the CSE 110 (Introduction to Computer Science) curriculum.

> NOTE: If you are an instructor or student using this repository, follow the Getting Started section below for setup and assignment workflows.

## Contents

- lectures/        - Lecture notes and slides
- labs/            - Lab exercises and starter code
- assignments/     - Assignment descriptions and starter repositories
- examples/        - Example programs and solutions
- resources/       - Helpful references and supporting files

(If any of these directories are missing, they will be added as the course progresses.)

## Getting started

Prerequisites
- Python 3.10 or newer (install from https://www.python.org/)
- Git

Quick setup

1. Clone the repository

   git clone https://github.com/BYULabs/cse110.git
   cd cse110

2. (Optional) Create a virtual environment and activate it

   python -m venv .venv
   # On macOS / Linux
   source .venv/bin/activate
   # On Windows (PowerShell)
   .\.venv\Scripts\Activate.ps1

3. Install project dependencies (if a requirements.txt is provided)

   pip install -r requirements.txt

4. Run an example

   python examples/hello_world.py

## Assignment workflow (students)

- Each assignment will have its own folder under `assignments/` and include a `README.md` with requirements and submission instructions.
- Follow the instructions in the assignment folder. Submit via the course LMS or the method specified by the instructor.

## How this repository is organized (recommended)

- lectures/ — PDF slides, Jupyter notebooks or other lecture artifacts
- labs/ — short practice exercises with unit tests when available
- assignments/ — assignment statements and starter code
- examples/ — small programs demonstrating core concepts
- tests/ — optional centralized test suite for automated checking

## Contributing

Contributions are welcome from instructors and course staff. Students should not open pull requests for assignment releases unless instructed.

To contribute changes:

1. Fork the repository (or create a branch if you have push access)
2. Make your changes and run any local tests
3. Open a pull request describing your changes

Please follow the repository's code style and include clear commit messages.

## Instructors / Staff

- Add new lecture notes under `lectures/` and link them from the course site.
- Create assignment starter repos under `assignments/<assignment-name>/starter/` if you want students to clone only the starter code.
- Tag releases or create branches for each semester offering to preserve materials.

## License

If this repository should be shared publicly, add a LICENSE file describing the terms. If you are unsure which license to use, consider the MIT License for course materials.

## Contact

For questions about course content or repository structure, contact the BYULabs organization administrators or the course instructor.

---

This README is a general template. If you want a customized README with specific assignment links, semester information, or contributor guidelines, tell me what details to include and I will update the file accordingly.
