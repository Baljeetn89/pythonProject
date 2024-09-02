def check_hemoglobin(gender, hemoglobin_value):
    if gender.lower() == 'female':
        if hemoglobin_value < 117:
            return "Low hemoglobin value for female."
        elif 117 <= hemoglobin_value <= 155:
            return "Normal hemoglobin value for female."
        else:
            return "High hemoglobin value for female."
    elif gender.lower() == 'male':
        if hemoglobin_value < 134:
            return "Low hemoglobin value for male."
        elif 134 <= hemoglobin_value <= 167:
            return "Normal hemoglobin value for male."
        else:
            return "High hemoglobin value for male."
    else:
        return "Invalid gender input. Please enter 'male' or 'female'."


def main():
    try:
        gender = input("Enter your biological gender (male/female): ").strip()
        hemoglobin_value = float(input("Enter your hemoglobin value (g/l): ").strip())

        result = check_hemoglobin(gender, hemoglobin_value)
        print(result)
    except ValueError:
        print("Invalid input. Please enter a numerical value for hemoglobin.")


if __name__ == "__main__":
    main()