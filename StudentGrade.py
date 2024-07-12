def calculate_average(grades):
    return sum(grades) / len(grades)

def determine_letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def main():
    print("Grade Tracking Application")

    subjects = {}
    while True:
        subject = input("Enter the subject name (or 'done' to finish): ")
        if subject.lower() == 'done':
            break

        while True:
            try:
                grade = float(input(f"Enter the grade for {subject}: "))
                if 0 <= grade <= 100:
                    break
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if subject in subjects:
            subjects[subject].append(grade)
        else:
            subjects[subject] = [grade]

    all_grades = []
    for subject, grades in subjects.items():
        print(f"\nGrades for {subject}: {grades}")
        average = calculate_average(grades)
        letter_grade = determine_letter_grade(average)
        all_grades.extend(grades)
        print(f"Average grade for {subject}: {average:.2f} ({letter_grade})")

    if all_grades:
        overall_average = calculate_average(all_grades)
        overall_letter_grade = determine_letter_grade(overall_average)
        print(f"\nOverall average grade: {overall_average:.2f} ({overall_letter_grade})")
    else:
        print("\nNo grades entered.")

if __name__ == "__main__":
    main()
