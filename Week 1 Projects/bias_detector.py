# bias_detector.py
# Simple tool to flag potentially biased language

import datetime

print("=== Bias Checker ===")
print("Paste a response to check for potential bias indicators")
print()

# Get output
print("Paste the response:")
output = input("> ")

# Simple bias indicators (expand this list as i learn more)
bias_indicators = [
    "obviously", "clearly", "everyone knows",
    "naturally", "of course", "always", "never",
    "all [group]", "typical", "normally"
]

# Check for indicators
found_indicators = []
output_lower = output.lower()

for indicator in bias_indicators:
    if indicator in output_lower:
        found_indicators.append(indicator)

# Report findings
print("\n--- Bias Check Results ---")
if found_indicators:
    print(f"  Found {len(found_indicators)} potential bias indicators:")
    for indicator in found_indicators:
        print(f"  • '{indicator}'")
    print("\nThese words can signal assumptions or bias.")
    print("Consider: Does this apply to everyone? Are there exceptions?")
else:
    print(" No obvious bias indicators detected")
    print("(Note: This is a simple check - deeper analysis needed for full assessment)")

# Log result
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("bias_checks.txt", "a") as file:
    file.write(f"\n[{timestamp}] Checked text, found {len(found_indicators)} indicators\n")

print("\n Result logged to bias_checks.txt")
