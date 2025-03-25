import time


attendance_file = "attendance.txt"

def mark_attendance():
    emp_id = input("Enter your Employee ID: ")  
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")  

    
    with open(attendance_file, "a") as file:
        file.write(f"{timestamp} - Employee ID: {emp_id}\n")

    print(f"Attendance marked for Employee ID: {emp_id} at {timestamp}")


while True:
    print("\n--- Employee Attendance System ---")
    mark_attendance()

    
    more = input("Mark another attendance? (yes/no): ").strip().lower()
    if more != "yes":
        print("Exiting Attendance System.")
        break
