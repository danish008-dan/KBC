# KBC
This is a Python console-based Kaun Banega Crorepati (KBC) game inspired by the famous Indian TV show.

🎮 KBC Game in Python
📌 Overview

This is a Python console-based Kaun Banega Crorepati (KBC) game inspired by the popular Indian TV show.
The player answers multiple-choice questions, uses lifelines, and tries to win the game.
It is built using Object-Oriented Programming (OOP) concepts in Python.

🚀 Features

✔ Multiple-choice questions with 4 options each
✔ Two lifelines available:

50-50 Lifeline → Eliminates 2 wrong options

Hint Lifeline → Gives a helpful hint for the answer
✔ Score system for correct answers
✔ Interactive console-based gameplay
✔ Simple, beginner-friendly Python project

📂 Project Structure
KBC-Game/
│── kbc.py        # Main Python file (game code)
│── README.md     # Project documentation

🔧 How It Works

Class Amitabh_bachchan → Stores questions, options, correct answers, hints, and lifelines.

Class Danish (inherits from Amitabh_bachchan) → Handles game logic, lifeline usage, player inputs, and scoring.

The game starts with Amitabh Bachchan's style introduction 🎤.

For each question:

Options are displayed

Player can use a lifeline (50-50 or Hint)

Player answers the question

If the answer is correct → score increases.
If wrong → game ends.

🖥️ Example Run
Welcome to kon banega crorepati ke season 7 me
Aaj hamere first contestant he Mr. Danish Khatri
Danish ji apke paas 1 Hint or 1 Fifty-Fifty Lifeline he 

To chaliye shuru krte he apne pehle sawal se
Danish ji apka pehla sawal he ye:

 Which planet is known as the Red Planet?
Options:
- Earth
- Venus
- Mars
- Jupiter

Danish ji kya aap life_line lena chahenge (yes/no): yes
1. 50-50
2. Hint
apke paas 2 life_line ka option he abhi (1/2): 1
Fifty-Fifty diya jaye Danish ji ko
Remaining Options:
- Mars
- Venus

Danish ji aap apna jawab bata sakte he ab: Mars
7 crore
Mubarak ho Danish ji aap jeet te he 7 crore

📦 Installation & Usage

Clone the repository:

git clone https://github.com/<your-username>/kbc-game.git


Navigate to the project folder:

cd kbc-game


Run the program:

python kbc.py

📚 Future Enhancements

Add more questions for longer gameplay

Include multiple contestants feature

Add prize money levels (like original KBC)

GUI version using Tkinter or PyQt
