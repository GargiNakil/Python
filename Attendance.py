import time

attendance_file = "attendance.txt"

def mark_attendance():
    emp_id = input("Enter your Employee ID: ")  
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")  

    with open(attendance_file, "a") as file:
        file.write(f"{timestamp} - Employee ID: {emp_id}\n")

    print(f"Attendance marked for Employee ID: {emp_id} at {timestamp}")

def display_attendance():
    print("\n--- Attendance List ---")
    try:
        with open(attendance_file, "r") as file:
            records = file.readlines()
            if records:
                for record in records:
                    print(record.strip())  
            else:
                print("No attendance records found.")
    except FileNotFoundError:
        print("No attendance records found.")

while True:
    print("\n--- Employee Attendance System ---")
    mark_attendance()
    display_attendance()

    more = input("\nMark another attendance? (yes/no): ").strip().lower()
    if more != "yes":
        print("\nExiting Attendance System.")
        break
