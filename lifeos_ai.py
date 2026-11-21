
import hashlib
import time
import textwrap

LINE_WIDTH = 70
BAR_LENGTH = 30

CAREER_SKILL_MAP = {
    "software engineer": ["Python", "Data Structures", "Algorithms", "Git", "Problem Solving", "SQL"],
    "software developer": ["Python", "Data Structures", "Algorithms", "Git", "Problem Solving", "SQL"],
    "data scientist": ["Python", "Statistics", "Machine Learning", "SQL", "Data Visualization", "Excel"],
    "data analyst": ["Excel", "SQL", "Statistics", "Data Visualization", "Communication"],
    "web developer": ["HTML", "CSS", "JavaScript", "React", "Git", "Problem Solving"],
    "designer": ["UI/UX Design", "Figma", "Creativity", "Color Theory", "Communication"],
    "ui/ux designer": ["UI/UX Design", "Figma", "Creativity", "Color Theory", "Communication"],
    "business analyst": ["Excel", "Communication", "Data Analysis", "SQL", "Presentation Skills"],
    "entrepreneur": ["Leadership", "Communication", "Financial Management", "Marketing", "Networking"],
    "doctor": ["Biology", "Critical Thinking", "Communication", "Patience", "Time Management"],
    "civil services": ["General Knowledge", "Communication", "Writing Skills", "Time Management", "Current Affairs"],
    "teacher": ["Communication", "Patience", "Subject Knowledge", "Public Speaking", "Time Management"],
    "engineer": ["Mathematics", "Problem Solving", "Technical Drawing", "Critical Thinking", "Teamwork"],
}

DEFAULT_REQUIRED_SKILLS = ["Communication", "Time Management", "Critical Thinking",
                           "Problem Solving", "Digital Literacy"]

MOTIVATION_QUOTES = {
    "S": "You are operating near peak potential - sustain it, refine it.",
    "A": "Excellent trajectory. Small consistent upgrades will get you to elite level.",
    "B": "Solid foundation. A few focused habit changes will accelerate your growth.",
    "C": "You have real potential waiting to be unlocked - structure is the key.",
    "D": "Every expert was once a beginner. Start small, stay consistent, grow daily.",
}


# ----------------------------- HELPERS -----------------------------

def line(char="-"):
    print(char * LINE_WIDTH)


def header(title):
    print()
    line("=")
    print(title.center(LINE_WIDTH))
    line("=")


def section(title):
    print()
    print(f" {title}")
    line("-")


def progress_bar(score, length=BAR_LENGTH):
    score = max(0, min(100, score))
    filled = int(round((score / 100) * length))
    return "█" * filled + "░" * (length - filled)


def wrap(text, indent="   "):
    return textwrap.fill(text, width=LINE_WIDTH - len(indent),
                         initial_indent=indent, subsequent_indent=indent)


def safe_float(prompt, low=None, high=None):
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
            if low is not None and value < low:
                print(f"   Please enter a value of at least {low}.")
                continue
            if high is not None and value > high:
                print(f"   Please enter a value of at most {high}.")
                continue
            return value
        except ValueError:
            print("   Invalid number, please try again.")


def clamp(value, low=0, high=100):
    return max(low, min(high, value))


def grade_band(score):
    if score >= 90:
        return "S"
    elif score >= 75:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 45:
        return "C"
    return "D"


def generate_digital_id(name):
    seed = f"{name}{time.time()}".encode()
    return "LFOS-" + hashlib.md5(seed).hexdigest()[:6].upper()


# ------------------------- DATA COLLECTION -------------------------

def collect_student_data():
    header("LIFEOS AI - STUDENT DIGITAL TWIN INTAKE")
    print(" Please answer the following questions honestly.\n")

    name = input(" 1. Student Name: ").strip() or "Student"
    marks = safe_float(" 2. Academic Marks (overall %, 0-100): ", 0, 100)
    study_hours = safe_float(" 3. Study Hours Per Day (0-16): ", 0, 16)
    sleep_hours = safe_float(" 4. Sleep Hours Per Day (0-14): ", 0, 14)
    screen_time = safe_float(" 5. Screen Time Per Day (hrs, 0-18): ", 0, 18)

    skills_raw = input(" 6. Current Skills (comma-separated): ").strip()
    current_skills = [s.strip() for s in skills_raw.split(",") if s.strip()]

    income = safe_float(" 7a. Monthly Income / Allowance: ", 0)
    expense = safe_float(" 7b. Monthly Expense: ", 0)

    career_goal = input(" 8. Career Goal (e.g., Software Engineer): ").strip() or "General Career"

    return {
        "name": name, "marks": marks, "study_hours": study_hours,
        "sleep_hours": sleep_hours, "screen_time": screen_time,
        "current_skills": current_skills, "income": income,
        "expense": expense, "career_goal": career_goal,
    }


# --------------------------- ANALYSIS ENGINE ---------------------------

def analyze_academics(marks):
    score = clamp(marks)
    grade = grade_band(score)
    if score >= 90:
        remark = "Outstanding academic command."
    elif score >= 75:
        remark = "Strong academic performance with room to push for excellence."
    elif score >= 60:
        remark = "Decent performance; targeted revision could raise scores significantly."
    elif score >= 45:
        remark = "Below comfortable range - a structured study plan is recommended."
    else:
        remark = "Academic performance needs urgent attention and support."
    return {"score": score, "grade": grade, "remark": remark}


def analyze_productivity(study_hours, sleep_hours, screen_time):
    if study_hours <= 6:
        study_component = (study_hours / 6) * 40
    else:
        study_component = max(40 - (study_hours - 6) * 3, 20)

    sleep_component = clamp(30 - abs(sleep_hours - 8) * 5, 0, 30)
    screen_component = clamp(30 - screen_time * 3, 0, 30)
    total = clamp(study_component + sleep_component + screen_component)

    if total >= 80:
        tag = "Highly Productive"
    elif total >= 60:
        tag = "Balanced & Efficient"
    elif total >= 40:
        tag = "Inconsistent Routine"
    else:
        tag = "Low Productivity / Burnout Risk"

    return {"score": total, "tag": tag,
            "study_component": study_component,
            "sleep_component": sleep_component,
            "screen_component": screen_component}


def analyze_finance(income, expense):
    savings_rate = ((income - expense) / income) * 100 if income > 0 else 0
    score = clamp(50 + savings_rate, 0, 100)

    if savings_rate >= 30:
        remark = "Excellent financial discipline - strong saving habit."
    elif savings_rate >= 10:
        remark = "Healthy balance between spending and saving."
    elif savings_rate >= 0:
        remark = "Tight budget - minimal savings buffer."
    else:
        remark = "Spending exceeds income - financial risk detected."

    return {"score": score, "savings_rate": savings_rate, "remark": remark}


def analyze_skills(current_skills, career_goal):
    goal_key = career_goal.lower().strip()
    required = DEFAULT_REQUIRED_SKILLS
    matched_label = "General Skill Set"

    for key, skills in CAREER_SKILL_MAP.items():
        if key in goal_key or goal_key in key:
            required = skills
            matched_label = key.title()
            break

    current_lower = [s.lower() for s in current_skills]
    possessed = [s for s in required if s.lower() in current_lower]
    missing = [s for s in required if s.lower() not in current_lower]
    skill_score = (len(possessed) / len(required)) * 100 if required else 0

    return {"score": clamp(skill_score), "required": required,
            "possessed": possessed, "missing": missing,
            "matched_path": matched_label}


def calculate_growth_score(academic, productivity, finance, skills):
    return clamp(
        academic["score"] * 0.30 +
        productivity["score"] * 0.25 +
        finance["score"] * 0.15 +
        skills["score"] * 0.30
    )


def project_growth_trajectory(growth_score):
    gap = 100 - growth_score
    return {
        "3_month": clamp(growth_score + gap * 0.12),
        "6_month": clamp(growth_score + gap * 0.25),
        "12_month": clamp(growth_score + gap * 0.45),
    }


def build_recommendations(academic, productivity, finance, skills):
    tips = []

    if academic["score"] < 75:
        tips.append("Adopt the Pomodoro technique (25 min focus + 5 min break) "
                    "to deepen academic retention.")
    if productivity["sleep_component"] < 20:
        tips.append("Adjust sleep schedule toward 7-9 hours; recovery directly "
                    "boosts focus and memory consolidation.")
    if productivity["screen_component"] < 15:
        tips.append("Reduce non-academic screen time using app-limit tools; "
                    "reclaim 1-2 hours daily for skill building.")
    if productivity["study_component"] < 25:
        tips.append("Increase focused study time gradually toward 4-6 hours/day "
                    "using a fixed daily timetable.")
    if finance["savings_rate"] < 10:
        tips.append("Track monthly expenses in categories and set a 20% "
                    "savings target to build financial resilience.")
    if skills["missing"]:
        top_gap = ", ".join(skills["missing"][:3])
        tips.append(f"Prioritize learning: {top_gap} - these are core to your "
                    f"chosen path and currently missing from your profile.")
    if not tips:
        tips.append("You're performing well across all dimensions - focus on "
                    "advanced specialization and mentoring others to grow further.")
    return tips


# ----------------------------- REPORT -----------------------------

def render_report(data, academic, productivity, finance, skills, growth_score, trajectory, tips):
    digital_id = generate_digital_id(data["name"])

    header("LIFEOS AI - STUDENT DIGITAL TWIN REPORT")

    section("STUDENT DIGITAL PROFILE")
    print(f"   Name              : {data['name']}")
    print(f"   Digital Twin ID   : {digital_id}")
    print(f"   Career Goal       : {data['career_goal'].title()}")
    print(f"   Mapped Career Path: {skills['matched_path']}")

    section("ACADEMIC ANALYSIS")
    print(f"   Marks        : {academic['score']:.1f}%   Grade Band: {academic['grade']}")
    print(f"   {progress_bar(academic['score'])}  {academic['score']:.0f}/100")
    print(wrap(academic["remark"]))

    section("PRODUCTIVITY REPORT")
    print(f"   Productivity Tag : {productivity['tag']}")
    print(f"   {progress_bar(productivity['score'])}  {productivity['score']:.0f}/100")
    print(f"     - Study Routine Component : {productivity['study_component']:.1f}/40")
    print(f"     - Sleep Quality Component : {productivity['sleep_component']:.1f}/30")
    print(f"     - Screen-Time Component   : {productivity['screen_component']:.1f}/30")

    section("FINANCIAL BEHAVIOR")
    print(f"   Savings Rate : {finance['savings_rate']:.1f}%")
    print(f"   {progress_bar(finance['score'])}  {finance['score']:.0f}/100")
    print(wrap(finance["remark"]))

    section("SKILL IMPROVEMENT SUGGESTIONS")
    print(f"   Skill Match Score : {skills['score']:.0f}/100")
    print(f"   {progress_bar(skills['score'])}")
    have_txt = ", ".join(skills["possessed"]) if skills["possessed"] else "None matched yet"
    gap_txt = ", ".join(skills["missing"]) if skills["missing"] else "No major gaps detected!"
    print(f"   Skills You Have   : {have_txt}")
    print(f"   Skill Gaps Found  : {gap_txt}")

    band = grade_band(growth_score)
    section("PERSONAL GROWTH SCORE")
    print(f"   {progress_bar(growth_score)}  {growth_score:.1f}/100   [Band: {band}]")
    print(wrap(MOTIVATION_QUOTES[band]))

    section("FUTURE GROWTH RECOMMENDATIONS - PROJECTED TRAJECTORY")
    print("   (Estimated growth score if recommendations below are followed)")
    print(f"     - 3 Months  : {trajectory['3_month']:.1f}/100   {progress_bar(trajectory['3_month'], 20)}")
    print(f"     - 6 Months  : {trajectory['6_month']:.1f}/100   {progress_bar(trajectory['6_month'], 20)}")
    print(f"     - 12 Months : {trajectory['12_month']:.1f}/100   {progress_bar(trajectory['12_month'], 20)}")

    section("PERSONALIZED RECOMMENDATIONS")
    for i, tip in enumerate(tips, start=1):
        print(wrap(f"{i}. {tip}"))

    print()
    line("=")
    print(" Thank you for using LifeOS AI - Grow with Insight, Build with Purpose.".center(LINE_WIDTH))
    line("=")


# ------------------------------ MAIN ------------------------------

def main():
    data = collect_student_data()

    academic = analyze_academics(data["marks"])
    productivity = analyze_productivity(data["study_hours"], data["sleep_hours"], data["screen_time"])
    finance = analyze_finance(data["income"], data["expense"])
    skills = analyze_skills(data["current_skills"], data["career_goal"])

    growth_score = calculate_growth_score(academic, productivity, finance, skills)
    trajectory = project_growth_trajectory(growth_score)
    tips = build_recommendations(academic, productivity, finance, skills)

    render_report(data, academic, productivity, finance, skills, growth_score, trajectory, tips)


if __name__ == "__main__":
    main()
