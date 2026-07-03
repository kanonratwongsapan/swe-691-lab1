def calculate_grade(scores):
    # 1. ตรวจสอบก่อนว่าลิสต์ว่างหรือไม่ เพื่อป้องกัน ZeroDivisionError
    if not scores:
        return "No data", 0
    
    # 2. ใช้ฟังก์ชัน sum() แทนการใช้ loop manual เพื่อความเร็วและอ่านง่าย
    total = sum(scores)
    average = total / len(scores)
    
    # 3. การจัดลำดับเงื่อนไข (Logic เดิมถูกต้องแล้ว แต่เขียนให้กระชับได้)
    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"
        
    return grade, average

# ทดสอบด้วยข้อมูลปกติ
scores = [85, 92, 78, 88, 95]
grade, avg = calculate_grade(scores)
print(f"Grade: {grade}, Average: {avg:.2f}")

# ทดสอบด้วยลิสต์ว่าง (เพื่อดูว่า Bug หายไปหรือยัง)
empty_scores = []
print(f"Empty case: {calculate_grade(empty_scores)}")
