"""
Q7.
A student has these marks:

[45, 72, 31, 90, 56, 28]

Use a loop to examine each mark and count how many subjects the student passed and how many they failed.

Use 33 as the passing mark.
"""

marks = [45, 72, 31, 90, 56, 28]
passed = 0
failed = 0

for num in marks:
    if num >= 33 and num <= 100:
        passed += 1
    else:
        failed += 1

print(f'Passed: {passed}')
print(f'Failed: {failed}')