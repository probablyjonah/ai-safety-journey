# ai_safety_journal.py
# My learning journal for AI safety and welfare transition
# Saves entries to a text file with timestamp

import datetime

print("=== AI Safety Learning Journal ===")
print()

# Get both date and time
now = datetime.datetime.now()
today = now.date()
current_time = now.strftime("%H:%M")  # Format: 21:35

# Create filename (monthly organization)
year_month = today.strftime("%Y-%m")
filename = f"journal_{year_month}.txt"

print(f"Date: {today}")
print(f"Time: {current_time}")
print(f"Saving to: {filename}")
print()

# Count existing entries in this file
try:
    with open(filename, "r") as file:
        existing_entries = file.read()
        entry_count = existing_entries.count("ENTRY #")
except FileNotFoundError:
    entry_count = 0

print(f"This will be entry #{entry_count + 1} this month")
print()

# Ask journaling questions
print("What did you study today?")
topic = input("> ")

print("\nHow many hours did you study?")
hours = input("> ")

print("\nWhat's one thing you learned?")
learned = input("> ")

print("\nWhat was challenging?")
challenge = input("> ")

print("\nWhat will you focus on next session?")
next_focus = input("> ")

print("\nHow do you feel about your progress? (1-10)")
mood = input("> ")

# Create the entry with entry number, date, and time
entry = f"""
{'='*50}
ENTRY #{entry_count + 1}
DATE: {today}
TIME: {current_time}
TOPIC: {topic}
HOURS: {hours}
LEARNED: {learned}
CHALLENGE: {challenge}
NEXT: {next_focus}
PROGRESS FEELING: {mood}/10
{'='*50}
"""

# Save to file (appends to existing entries)
with open(filename, "a") as file:
    file.write(entry)
    
print(f"\n✓ Entry #{entry_count + 1} saved to {filename}! Keep going.")
