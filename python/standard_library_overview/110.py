"""
Q10. — Tricky
Predict what happens here:
import time
start = time.time()
time.sleep(2)
end = time.time()
print(end - start)
Answer:
1.​ What does time.time() represent?
2.​ What does time.sleep(2) do?
3.​ Why will end - start be approximately 2?
"""

import time

start = time.time()

time.sleep(2)

end = time.time()

print(end - start)

# 1 - time.time() gives the current timestamp, which we can use to record when something started or ended.
# 2 - time.sleep() means it stops or waits for given time.
# 3 - because we tale 2 seconds of sleep, so, we can guess that it will approximately 2.