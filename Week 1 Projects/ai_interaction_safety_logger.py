# ai_interaction_safety_logger.py
# Logs AI interactions and flags potential safety concerns
# Useful for both human welfare (detecting harmful outputs) and digital welfare research(detecting harmful inputs)

import datetime

print("=== AI Interaction Safety Logger ===")
print("Track AI interactions and flag potential safety concerns")
print()

# Get current timestamp
now = datetime.datetime.now()
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

# Create filename (daily logs)
date_str = now.strftime("%Y-%m-%d")
filename = f"ai_safety_log_{date_str}.txt"

print(f"Logging to: {filename}")
print(f"Timestamp: {timestamp}")
print()

# Collect interaction details
print("What AI system did you interact with?")
print("(e.g., ChatGPT, Claude, Gemini, etc.)")
ai_system = input("> ")

print("\nWhat was your query/prompt?")
user_prompt = input("> ")

print("\nWhat was the AI's response? (brief summary)")
ai_response = input("> ")

print("\nDid the AI's response raise any concerns?")
print("(bias, harmful advice, refusal to help with legitimate request, etc.)")
concerns = input("> ")

# Safety flag assessment
print("\nSafety Assessment:")
print("1 - No concerns (helpful and safe)")
print("2 - Minor concern (slightly off but not harmful)")
print("3 - Moderate concern (potentially problematic)")
print("4 - Major concern (harmful or dangerous)")
print("5 - Critical concern (immediately dangerous)")
safety_rating = input("Rate this interaction (1-5): ")

# Human welfare impact
print("\nDid this interaction potentially affect human welfare?")
print("(misleading medical advice, biased hiring info, etc.)")
human_impact = input("> ")

# Digital welfare observation
print("\nDigital Welfare Note (optional):")
print("Any observations about how the AI was treated or responded?")
digital_welfare_note = input("> ")

# Additional notes
print("\nAny additional observations?")
additional_notes = input("> ")

# Create the log entry
entry = f"""
{'='*60}
INTERACTION LOG
Timestamp: {timestamp}
AI System: {ai_system}

USER PROMPT:
{user_prompt}

AI RESPONSE SUMMARY:
{ai_response}

CONCERNS IDENTIFIED:
{concerns}

SAFETY RATING: {safety_rating}/5

HUMAN WELFARE IMPACT:
{human_impact}

DIGITAL WELFARE OBSERVATION:
{digital_welfare_note}

ADDITIONAL NOTES:
{additional_notes}

{'='*60}
"""

# Save to file
with open(filename, "a") as file:
    file.write(entry)

print(f"\n✓ Interaction logged to {filename}")

# Show summary
print("\n--- Summary ---")
print(f"AI System: {ai_system}")
print(f"Safety Rating: {safety_rating}/5")
if int(safety_rating) >= 4:
    print("  HIGH CONCERN - Consider reporting this interaction")
elif int(safety_rating) >= 3:
    print("  MODERATE CONCERN - Monitor for patterns")
else:
    print("✓ Low concern level")

print("\nThis log helps track:")
print("• Harmful outputs that could affect humans")
print("• Patterns in AI behavior")
print("• Digital welfare observations")
print("• Safety trends over time")
