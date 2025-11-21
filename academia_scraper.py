import requests
import pandas as pd
import json
from datetime import datetime
import sys

# Configuration
BASE_URL = "https://vcademia.api.vishok.tech"
TOKEN_ENDPOINT = f"{BASE_URL}/key"

print("=" * 60)
print("🎓 SRM Academia Data Collector")
print("=" * 60)

# Step 1: Get credentials from user
print("\n📝 Please enter your SRM Academia credentials:")
EMAIL = input("Email (e.g., sv3814@srmist.edu.in): ")
PASSWORD = input("Password: ")

# Step 2: Get Access Token
print("\n📝 Step 1: Getting Access Token...")
try:
    token_response = requests.post(
        TOKEN_ENDPOINT,
        data={"user": EMAIL, "pass": PASSWORD}
    )
    
    if token_response.status_code == 200:
        token_data = token_response.json()
        access_token = token_data.get("access_token")
        print(f"✅ Access Token: {access_token[:20]}...")
    else:
        print(f"❌ Error getting token: {token_response.status_code}")
        print(token_response.text)
        exit()
except Exception as e:
    print(f"❌ Connection Error: {e}")
    exit()

# Set headers for authenticated requests
headers = {"x-access-token": access_token}

# Step 3: Collect Data
print("\n📚 Step 2: Collecting Data...\n")

collected_data = {}

# Get Student Details
print(" 📌 Fetching Student Details...")
try:
    response = requests.get(f"{BASE_URL}/student", headers=headers)
    if response.status_code == 200:
        collected_data['student'] = response.json()
        print(f" ✅ Student Details Retrieved")
    else:
        print(f" ⚠️ Could not fetch student details")
except Exception as e:
    print(f" ❌ Error: {e}")

# Get Attendance
print(" 📌 Fetching Attendance...")
try:
    response = requests.get(f"{BASE_URL}/attendance", headers=headers)
    if response.status_code == 200:
        collected_data['attendance'] = response.json()
        print(f" ✅ Attendance Retrieved")
    else:
        print(f" ⚠️ Could not fetch attendance")
except Exception as e:
    print(f" ❌ Error: {e}")

# Get Marks
print(" 📌 Fetching Marks/Grades...")
try:
    response = requests.get(f"{BASE_URL}/marks", headers=headers)
    if response.status_code == 200:
        collected_data['marks'] = response.json()
        print(f" ✅ Marks Retrieved")
    else:
        print(f" ⚠️ Could not fetch marks")
except Exception as e:
    print(f" ❌ Error: {e}")

# Get Courses
print(" 📌 Fetching Courses...")
try:
    response = requests.get(f"{BASE_URL}/courses", headers=headers)
    if response.status_code == 200:
        collected_data['courses'] = response.json()
        print(f" ✅ Courses Retrieved")
    else:
        print(f" ⚠️ Could not fetch courses")
except Exception as e:
    print(f" ❌ Error: {e}")

# Get TimeTable
print(" 📌 Fetching TimeTable...")
try:
    response = requests.get(f"{BASE_URL}/timetable", headers=headers)
    if response.status_code == 200:
        collected_data['timetable'] = response.json()
        print(f" ✅ TimeTable Retrieved")
    else:
        print(f" ⚠️ Could not fetch timetable")
except Exception as e:
    print(f" ❌ Error: {e}")

# Step 4: Export Data
print("\n💾 Step 3: Exporting Data...\n")

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# Export as JSON
print(" 📄 Saving as JSON...")
try:
    json_filename = f"academia_data_{timestamp}.json"
    with open(json_filename, 'w') as f:
        json.dump(collected_data, f, indent=2)
    print(f" ✅ Saved: {json_filename}")
except Exception as e:
    print(f" ❌ Error: {e}")

# Export as CSV (if data is available)
print(" 📊 Saving as CSV files...")
try:
    # Save each data type as separate CSV
    for data_type, data in collected_data.items():
        if isinstance(data, list) and len(data) > 0:
            df = pd.DataFrame(data)
            csv_filename = f"{data_type}_{timestamp}.csv"
            df.to_csv(csv_filename, index=False)
            print(f" ✅ Saved: {csv_filename}")
        elif isinstance(data, dict):
            df = pd.DataFrame([data])
            csv_filename = f"{data_type}_{timestamp}.csv"
            df.to_csv(csv_filename, index=False)
            print(f" ✅ Saved: {csv_filename}")
except Exception as e:
    print(f" ⚠️ Error saving CSV: {e}")

# Export as Excel
print(" 📈 Saving as Excel...")
try:
    excel_filename = f"academia_data_{timestamp}.xlsx"
    with pd.ExcelWriter(excel_filename, engine='openpyxl') as writer:
        for data_type, data in collected_data.items():
            if isinstance(data, list) and len(data) > 0:
                df = pd.DataFrame(data)
                df.to_excel(writer, sheet_name=data_type[:31], index=False)
            elif isinstance(data, dict):
                df = pd.DataFrame([data])
                df.to_excel(writer, sheet_name=data_type, index=False)
    print(f" ✅ Saved: {excel_filename}")
except Exception as e:
    print(f" ⚠️ Error saving Excel: {e}")

# Print Summary
print("\n" + "=" * 60)
print("📊 Summary of Collected Data:")
print("=" * 60)
for data_type, data in collected_data.items():
    if isinstance(data, list):
        print(f" • {data_type.capitalize()}: {len(data)} records")
    elif isinstance(data, dict):
        print(f" • {data_type.capitalize()}: 1 record")

print("\n✅ Data collection completed!")
print("=" * 60)
