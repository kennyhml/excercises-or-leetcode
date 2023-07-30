"""
You are given two strings current and correct representing two 24-hour times.

24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM 
is between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59.

In one operation you can increase the time current by 1, 5, 15, or 60 minutes. 
You can perform this operation any number of times.

Return the minimum number of operations needed to convert current to correct.
"""

def convertTime(current: str, correct: str) -> int:

    current = (int(current[:2]) * 60) + int(current[3:])
    correct = (int(correct[:2]) * 60) + int(correct[3:])
    delta = correct - current
    operations = 0
    
    for op in (60, 15, 5, 1):
        operations += delta // op
        diff %= op

    return operations