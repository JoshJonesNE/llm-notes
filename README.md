# LLM Notes

LLM Notes is a small web-based note taking application implemented with Flask. Notes are stored as plain files in the `notes` directory similar to how Obsidian manages files.

## Requirements

- Python 3.11 or later
- Dependencies listed in `requirements.txt`

## Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running

Start the server and open [http://localhost:5000](http://localhost:5000) in your browser:

```bash
python3 note_app.py
```

## Features

- Create new notes
- Edit existing notes
- Notes saved as Markdown or text files on disk
