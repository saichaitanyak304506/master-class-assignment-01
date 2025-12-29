# =====================================================
# DATA PROCESSING & TRANSFORMATION PROGRAM
# Concepts:
# Functional Programming | Comprehensions
# Data Transformation | Sorting | File Handling
# =====================================================

from functools import reduce
import json
import csv

# -----------------------------------------------------
# DATA SOURCE (Simulated API / Backend Response)
# -----------------------------------------------------
records = [
    {"uid": 101, "username": "Aarav", "role": "Engineering", "country": "India", "amount": 650, "enabled": True},
    {"uid": 102, "username": "Maya", "role": "HR", "country": "USA", "amount": 420, "enabled": True},
    {"uid": 103, "username": "John", "role": "Finance", "country": "India", "amount": 800, "enabled": False},
    {"uid": 104, "username": "Neha", "role": "Engineering", "country": "India", "amount": 550, "enabled": True},
    {"uid": 105, "username": "Leo", "role": "Design", "country": "UK", "amount": 300, "enabled": True},
]

# =====================================================
# 1️⃣ FUNCTIONAL UTILITIES
# =====================================================

def get_active_records(data):
    return list(filter(lambda r: r["enabled"], data))

def extract_amounts(data):
    return list(map(lambda r: r["amount"], data))

def calculate_total_amount(data):
    return reduce(lambda total, r: total + r["amount"], data, 0)

active_records = get_active_records(records)
amount_list = extract_amounts(records)
grand_total = calculate_total_amount(records)

# =====================================================
# 2️⃣ COMPREHENSION OPERATIONS
# =====================================================

# Names from Engineering department
engineering_users = [r["username"] for r in records if r["role"] == "Engineering"]

# Username mapped to country
user_country_map = {r["username"]: r["country"] for r in records}

# Character breakdown of usernames
username_chars = [(r["username"], ch) for r in records for ch in r["username"]]

# =====================================================
# 3️⃣ DATA TRANSFORMATION PIPELINE
# =====================================================

# Step 1: Filter active Indian users
india_active = [r for r in records if r["enabled"] and r["country"] == "India"]

# Step 2: Add category field
categorized = [
    {**r, "category": "Premium" if r["amount"] >= 600 else "Standard"}
    for r in india_active
]

# Step 3: Sort alphabetically
final_output = sorted(categorized, key=lambda r: r["username"])

# =====================================================
# 4️⃣ FILE EXPORT OPERATIONS
# =====================================================

# TXT Export
with open("output_users.txt", "w") as file:
    for r in records:
        file.write(f"{r['uid']} | {r['username']} | {r['role']} | {r['amount']}\n")

# JSON Export
with open("output_users.json", "w") as file:
    json.dump(records, file, indent=4)

# CSV Export
with open("output_users.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["uid", "username", "role", "country", "amount", "enabled"]
    )
    writer.writeheader()
    writer.writerows(records)

# =====================================================
# RESULT DISPLAY
# =====================================================

print("Active Records:", active_records)
print("All Amounts:", amount_list)
print("Total Amount:", grand_total)
print("Engineering Users:", engineering_users)
print("User-Country Map:", user_country_map)
print("Username Characters:", username_chars)
print("Final Transformed Data:",
      [(r["username"], r["category"], r["amount"]) for r in final_output])
