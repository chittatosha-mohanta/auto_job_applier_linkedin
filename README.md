# LinkedIn AI Auto Job Applier 🤖

Automation can revolutionize the job application process — letting you focus on what truly matters: preparing for interviews and growing your skills.

This is a web scraping bot that automates the process of job applications on LinkedIn. It searches for jobs relevant to you, answers all questions in the application form, customizes your resume based on job details like required skills, description, and company information — and applies to the job. Can apply to **100+ jobs in less than 1 hour**.

---

## 📽️ See it in Action

[![Auto Job Applier Demo Video](https://drive.google.com/thumbnail?id=1wEHgE4ffUsrlMjnmWeXforNzB97SxQPw)](https://drive.google.com/file/d/1wEHgE4ffUsrlMjnmWeXforNzB97SxQPw/view?usp=drive_link)

Click the image above to watch the demo, or use this link:
👉 [Watch Demo Video](https://drive.google.com/file/d/1wEHgE4ffUsrlMjnmWeXforNzB97SxQPw/view?usp=drive_link)

---

## ✨ How It Works

- Upload your Resume/CV
- The system reads and understands it
- It finds relevant jobs on LinkedIn based on your preferences
- Automatically fills and submits Easy Apply applications
- Saves all applied jobs to a history file for tracking
- A web UI (`app.py`) lets you view your applied jobs with user login support

No manual searching, no repetitive clicking, and no missed opportunities.

---

## ✨ Contents

- [How It Works](#-how-it-works)
- [Install](#️-how-to-install)
- [Configure](#-how-to-configure)
- [Run](#-how-to-run)
- [Project Structure](#-project-structure)
- [Disclaimer](#-disclaimer)
- [License](#️-license)
- [Socials](#-socials)
- [Credits](#-credits)

---

## ⚙️ How to Install

1. **Python 3.10 or above** — Download from [python.org](https://www.python.org/downloads/) or search "Python" on Microsoft Store (Windows). Make sure Python is added to your system PATH.

2. **Install required packages** — Open a terminal and run:

```bash
pip install -r requirements.txt
```

3. **Install Google Chrome** — Download from [google.com/chrome](https://www.google.com/chrome) and install in its default location.

4. **Clone this repository:**

```bash
git clone https://github.com/chittatosha-mohanta/auto_job_applier_linkedin.git
cd auto_job_applier_linkedin
```

5. **ChromeDriver Setup:**
   - If using `stealth_mode = True` (recommended), no manual ChromeDriver installation is needed.
   - Otherwise, download the matching [ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/) for your Chrome version.
   - On Windows, you can also run `windows-setup.bat` from the `/setup` folder to auto-install ChromeDriver.

---

## 🔧 How to Configure

All configuration files are in the `/config` folder:

| File | What to configure |
|------|-------------------|
| `personals.py` | Your name, phone, address, and other personal details |
| `questions.py` | Answers to common application questions, resume path, pause settings |
| `search.py` | Job search terms, location, filters, blacklisted companies |
| `secrets.py` | LinkedIn email, password, and OpenAI API key (optional) |
| `settings.py` | Stealth mode, click intervals, background mode, screen awake settings |

> **Optional:** Place your default resume PDF at the path defined in `config/questions.py` under `default_resume_path`. If not provided, the bot uses the last resume submitted on LinkedIn.

---

## ▶️ How to Run

### Run the Bot

```bash
python runAiBot.py
```

### Run the Applied Jobs Web UI

```bash
python app.py
```

Then open your browser at: [http://localhost:5000](http://localhost:5000)

The web UI supports user registration and login (powered by SQLite + Flask-SQLAlchemy).

To create a test user for the web UI:

```bash
python create_test_user.py
```

---

## 📁 Project Structure

```
auto_job_applier_linkedin/
│
├── config/             # All user configuration files
│   ├── personals.py
│   ├── questions.py
│   ├── search.py
│   ├── secrets.py
│   └── settings.py
│
├── modules/            # Core bot logic (scraping, answering, validation)
├── setup/              # Windows ChromeDriver auto-install scripts
├── templates/          # HTML templates for the Flask web UI
├── static/             # CSS and JS for the web UI
├── instance/           # SQLite database (auto-generated, not committed)
├── tests/              # Test and helper scripts
│   ├── create_test_user.py
│   └── test_login.py
├── app.py              # Flask web application (job history UI + user auth)
├── models.py           # SQLAlchemy database models
├── requirements.txt    # All required Python packages
├── runAiBot.py         # Main entry point to start the bot
```

---

## 📜 Disclaimer

This program is for **educational purposes only**. By using this project, you acknowledge and agree to all terms mentioned. The responsibility to review and comply with LinkedIn's terms of service and policies regarding web scraping lies with the user. Usage is at your own risk. The creator bears no responsibility for any misuse, damages, or legal consequences resulting from its usage.

---

## ⚖️ License

Copyright (C) 2024 Chittatosha Mohanta — [chittatoshamohanta@gmail.com](mailto:chittatoshamohanta@gmail.com)

This program is free software: you can redistribute it and/or modify it under the terms of the **GNU Affero General Public License** as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

See [AGPLv3 LICENSE](./LICENSE) for full details.

---

## 🐧 Socials

- **LinkedIn:** [chittatosha-mohanta](https://www.linkedin.com/in/chittatosha-mohanta-32a182288/)
- **GitHub:** [chittatosha-mohanta](https://github.com/chittatosha-mohanta)
- **Email:** [chittatoshamohanta@gmail.com](mailto:chittatoshamohanta@gmail.com)
