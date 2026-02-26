# Keylogger-Project

## IMPORTANT DISCLAIMER

#### This project is for educational purposes only. Any use outside of research and testing is not intended, and the owner is not liable for any harm caused by this project.

---

## What is this?

This is a keylogger written for educational and research purposes. It captures keystrokes on the host machine and logs them to a file. The goal of this project is to demonstrate how keyloggers work at a low level so that developers and security researchers can better understand the threat they pose and how to defend against them.

---

## Features

- Logs all keystrokes to a local file
- Runs silently in the background
- Lightweight with minimal dependencies
- Easy to set up and run in a controlled test environment
- Logs are stored in plain text for easy reading and analysis

---

## Requirements

Before setting up the project, make sure you have the following installed on your machine:

- Python 3.8 or higher
- pip (Python package manager)
- A virtual environment tool such as `venv` (recommended)
- The `pynput` library (installed via pip in the setup steps below)

---

## Setup

Follow these steps to get the project running on your local machine.

**1. Clone the repository**

```bash
git clone https://github.com/yourusername/Keylogger-Project.git
cd Keylogger-Project
```

**2. Create and activate a virtual environment**

On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

If there is no `requirements.txt`, install manually:

```bash
pip install pynput
```

**4. Run the keylogger**

```bash
python keylogger.py
```

**5. View the log file**

Once the script is running, keystrokes will be written to a file called `log.txt` in the same directory. Open it with any text editor to view the captured input.

---

## Project Structure

```
Keylogger-Project/
│
├── keylogger.py        # Main script
├── log.txt             # Output log file (generated on run)
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

---

## Legal Notice

- This tool must only be run on machines you own or have explicit written permission to test on
- Running this software on any machine without consent is illegal in most countries
- The author takes no responsibility for misuse of this project
- This project is strictly for learning about input capture mechanisms and cybersecurity awareness

---

## Contributing

Pull requests are welcome. If you find a bug or want to suggest an improvement, open an issue first to discuss what you would like to change. Please keep all contributions within the educational scope of this project.
