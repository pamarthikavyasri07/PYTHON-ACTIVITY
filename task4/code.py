
print("EMPLOYEE PAYROLL SYSTEM")

name = input("Enter employee name: ")
basic = float(input("Enter basic pay: "))
hours = float(input("Enter overtime hours: "))
incentive = float(input("Enter incentives: "))

# Validate inputs
if basic < 0 or hours < 0 or incentive < 0:
    print("Invalid Input")

else:
    allowance = basic * 0.20
    overtime = hours * 200

    # Calculate gross salary
    gross = basic + allowance + overtime + incentive

    # Progressive deductions
    if gross <= 20000:
        deduction = gross * 0.05

    elif gross <= 40000:
        deduction = 20000 * 0.05 + (gross - 20000) * 0.10

    else:
        deduction = (20000 * 0.05 +
                     20000 * 0.10 +
                     (gross - 40000) * 0.15)

    # Calculate net salary
    net = gross - deduction

    # Salary statement
    print("\n------ SALARY STATEMENT ------")
    print("Employee Name :", name)
    print("Basic Pay     :", basic)
    print("Allowances    :", allowance)
    print("Overtime Pay  :", overtime)
    print("Incentives    :", incentive)
    print("------------------------------")
    print("Gross Salary  :", gross)
    print("Deductions    :", deduction)
    print("Net Salary    :", net)
    print("------------------------------")

