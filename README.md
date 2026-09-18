Simple Python CLI Password Manager

A lightweight, command-line interface (CLI) password manager written in **Python**. This script automatically generates secure, random 12-character passwords and organizes your credentials into a local CSV file.

## 🚀 Features

* **Automatic Generation:** Creates strong passwords by mixing uppercase letters, lowercase letters, numbers, and special characters.
* **Local CSV Database:** Stores websites, usernames, and passwords locally in a `passwords.csv` file managed via `pandas`.
* **Duplicate Prevention:** If you enter an existing website and username combination, the script prompts you before overwriting and updating the password.
* **Persistent Loop:** Stays active in a continuous loop so you can add multiple credentials in a single session.

## 📋 Requirements

To run this script, you need **Python 3.10+** (as it uses the `match-case` syntax) and the **pandas** library.

Install the required dependency via pip:
```bash
pip install pandas
```

## 🔧 Installation and Usage


4. Follow the on-screen prompts by entering the website and your username. The password will be generated and saved automatically.

## 📝 Security Disclaimer
This project was created for educational purposes. Data is saved in plain text inside the CSV file without encryption. Do not use this tool to store real or highly sensitive account passwords.
