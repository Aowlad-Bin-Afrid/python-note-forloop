
# for loop examples
# Created by Afrid
# Date: 2025-10-28
# Description: examples of Python for loop



# ---------------------------------------------------------
# for_loop_advanced.py
# ---------------------------------------------------------
# 🎯 Purpose:
# This file explains everything about the Python "for loop":
# - range() function
# - if, break, continue, else
# - nested loops
# - using for loop with list, string, and dictionary
# ---------------------------------------------------------

# 🟩 1️⃣ Basic for loop — print numbers from 1 to 10
for i in range(1, 11):
    print(i)

# range(1, 11) means:
#   start = 1
#   stop = 11 (but 11 is not included)
# ---------------------------------------------------------

# 🟦 2️⃣ for loop with step value
for i in range(1, 11, 2):
    print("Odd number:", i)
# range(1, 11, 2) → starts from 1, ends before 11, increases by 2 each time
# ---------------------------------------------------------

# 🟨 3️⃣ Reverse loop
for i in range(10, 0, -1):
    print("Reverse:", i)
# ---------------------------------------------------------

# 🟧 4️⃣ Using if condition inside loop
for i in range(1, 6):
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")
# ---------------------------------------------------------

# 🟥 5️⃣ Using break — stop the loop early
for i in range(1, 11):
    if i == 5:
        print("Loop stopped at", i)
        break
    print("Number:", i)
# break → stops the loop when condition is met
# ---------------------------------------------------------

# 🟪 6️⃣ Using continue — skip a specific step
for i in range(1, 6):
    if i == 3:
        continue
    print("Value:", i)
# continue → skips the current iteration and moves to the next
# ---------------------------------------------------------

# 🟫 7️⃣ Using else with for loop
for i in range(1, 4):
    print(i)
else:
    print("Loop finished successfully!")
# else → runs only when loop finishes normally (no break)
# ---------------------------------------------------------

# ⬛ 8️⃣ Nested loop — loop inside another loop
for i in range(1, 4):
    for j in range(1, 3):
        print(f"i = {i}, j = {j}")
# ---------------------------------------------------------

# 🟨 9️⃣ Calculate the sum of numbers
total = 0
for i in range(1, 6):
    total += i
print("Sum from 1 to 5:", total)
# ---------------------------------------------------------

# 🟩 🔟 Looping through a string
name = "Python"
for letter in name:
    print("Letter:", letter)
# ---------------------------------------------------------

# 🟦 1️⃣1️⃣ Looping through a list
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print("Fruit:", fruit)
# ---------------------------------------------------------

# 🟧 1️⃣2️⃣ Looping through a dictionary
student = {"name": "Arafat", "age": 20, "country": "Bangladesh"}
for key, value in student.items():
    print(key, ":", value)
# ---------------------------------------------------------

# ✅ Summary:
# ---------------------------------------------------------
# 🔹 for loop — used when you know how many times to iterate
# 🔹 range() — generates a sequence of numbers
# 🔹 if — checks a condition
# 🔹 break — stops the loop immediately
# 🔹 continue — skips one iteration
# 🔹 else — runs when the loop finishes without break
# 🔹 nested loop — loop inside another loop
# 🔹 list/string/dict — can be iterated with for loop
# ---------------------------------------------------------


name = "afrit "
for i in name:
  print(i)
  if i == "t":
    print("d")




