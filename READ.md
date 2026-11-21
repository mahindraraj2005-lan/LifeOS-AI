# 🧬 LifeOS AI: Intelligent Student Digital Twin & Future Growth Simulator

A console-based Python application that builds a **digital profile of a student** from academic, lifestyle, skill and financial data, then generates a personal **Growth Score**, a **skill-gap analysis** and a **future growth projection** with personalized recommendations.

![Python](https://img.shields.io/badge/Python-3.x-blue) ![Dependencies](https://img.shields.io/badge/Dependencies-None-green) ![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📌 Problem Statement
Students often don't know how their daily habits (study time, sleep, screen time, spending) and skills affect their future growth. They lack data-based guidance for self-improvement and career planning.

## 💡 Solution
LifeOS AI analyzes a student's data and produces a clear, structured report covering productivity, strengths, weaknesses, skill gaps and actionable next steps.

## ✨ Features
- **Student Digital Profile** with a unique Digital Twin ID
- **Academic Analysis** with grade bands (S/A/B/C/D)
- **Productivity Score** based on study routine, sleep quality and screen time
- **Financial Behavior Analysis** using savings rate
- **Career-based Skill Gap Detection** for 13 career paths
- **Personal Growth Score** (weighted multi-factor model)
- **3 / 6 / 12-month Growth Projection**
- **Personalized Recommendations**
- Input validation and a clean, formatted console report

## 🧮 How the Growth Score Works

| Factor | Weight |
|---|---|
| Academic Performance | 30% |
| Skill Match (vs. career goal) | 30% |
| Productivity | 25% |
| Financial Behavior | 15% |

**Productivity Score (100)** = Study Routine (40) + Sleep Quality (30) + Screen-Time Control (30)

## 🛠️ Tech Stack
- **Language:** Python 3
- **Libraries:** Standard library only (`hashlib`, `time`, `textwrap`)

## 🚀 How to Run

```bash
git clone https://github.com/<your-username>/LifeOS-AI.git
cd LifeOS-AI
python lifeos_ai.py
```

Also works in any online Python compiler (Programiz, OnlineGDB, Replit, Google Colab). Just paste the code and run.

## 📥 Sample Input

```
Student Name: Aarav
Academic Marks: 82
Study Hours Per Day: 5
Sleep Hours: 6.5
Screen Time: 4
Current Skills: Python, Communication, Excel
Monthly Income: 15000
Monthly Expense: 11000
Career Goal: Data Scientist
```

## 📤 Sample Output

```
 STUDENT DIGITAL PROFILE
   Name              : Aarav
   Digital Twin ID   : LFOS-C035A4
   Career Goal       : Data Scientist

 ACADEMIC ANALYSIS
   Marks : 82.0%   Grade Band: A

 PRODUCTIVITY REPORT
   Productivity Tag : Balanced & Efficient   (74/100)

 FINANCIAL BEHAVIOR
   Savings Rate : 26.7%   (77/100)

 SKILL IMPROVEMENT SUGGESTIONS
   Skills You Have   : Python, Excel
   Skill Gaps Found  : Statistics, Machine Learning, SQL, Data Visualization

 PERSONAL GROWTH SCORE
   64.6/100   [Band: B]

 PROJECTED TRAJECTORY
   3 Months  : 68.8/100
   6 Months  : 73.4/100
   12 Months : 80.5/100
```

## 🔮 Future Enhancements
- Save and compare reports over time
- Graphical dashboard (Matplotlib / Streamlit)
- Machine-learning-based growth prediction
- Learning-resource suggestions for each skill gap
- Web or mobile version

## 👤 Author
**<Your Name>**
GitHub: [mahindraraj2005-lan](https://github.com/mahindraraj2005-lan)

---
⭐ If you found this project useful, consider giving it a star!
