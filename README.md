# Python Conditions and Loops — Scholarship & Pharmacy Management Systems

Two beginner-friendly Python console applications developed for a programming assessment on **conditional statements and loop structures**. The project demonstrates decision-making through a student scholarship scenario and repetition, counters, and accumulators through a pharmacy inventory and sales scenario.

## Repository Name

`python-conditions-loops-assessment`

## Project Overview

This assessment contains two separate applications:

1. **Student Scholarship Eligibility System:** Evaluates a student's scholarship eligibility using academic marks, attendance percentage, and monthly family income.
2. **Smart Pharmacy Inventory & Sales Management System:** Processes medicine inventory and sales, checks stock availability, calculates revenue, and identifies medicines that need restocking.

Both programs use console input and output. They are independent Python files and can be run separately.

## Task 1 — Student Scholarship Eligibility System

The program collects the student's name, academic marks, attendance percentage, and monthly family income. It validates the entered information before evaluating the scholarship requirements.

### Scholarship Eligibility Criteria

| Requirement | Eligibility Condition |
|---|---|
| Academic marks | At least 80% |
| Attendance | At least 85% |
| Monthly family income | Rs. 50,000 or less |

When all three requirements are satisfied, the scholarship category is selected according to academic marks:

| Academic Marks | Scholarship |
|---|---|
| 90% or above | Full Scholarship |
| 80% to below 90% | Partial Scholarship |

If one or more requirements are not satisfied, the program displays each applicable reason for ineligibility.

### Concepts Covered

- `if`, `elif`, and `else` for conditional decision-making.
- Comparison operators such as `<`, `<=`, `>=`, and `>`.
- `while` loops for repeating input until valid information is entered.
- `input()` and `print()` for console interaction.
- `float()` for accepting percentage and income values.
- `try/except` with `ValueError` for handling non-numeric input.
- Lists and `append()` for collecting multiple ineligibility reasons.
- Logical conditions for checking all scholarship requirements.
- F-strings and number formatting for a readable evaluation report.

### Program Logic and Validation

1. **Student name:** Rejects an empty name after removing surrounding spaces.
2. **Academic marks:** Accepts numeric values from 0 to 100, inclusive.
3. **Attendance:** Accepts numeric values from 0 to 100, inclusive.
4. **Family income:** Accepts numeric values greater than or equal to zero.
5. **Eligibility evaluation:** Checks all three requirements independently so that every failed requirement can be reported.
6. **Scholarship category:** Awards a full scholarship for eligible marks of at least 90%; otherwise, eligible marks receive a partial scholarship.
7. **Evaluation report:** Displays the student's information, scholarship result, and either confirmation of eligibility or all reasons for ineligibility.

**Important eligibility detail:** A student receives a scholarship only when all three conditions are satisfied. A high marks percentage alone does not override insufficient attendance or family income above the allowed limit. An income of exactly Rs. 50,000 and attendance of exactly 85% meet their respective requirements.

## Task 2 — Smart Pharmacy Inventory & Sales Management System

The program asks how many different medicines need to be processed and uses a `for` loop with `range()` to process each medicine. For every medicine, it collects the name, available stock, price per unit, and requested sales quantity.

The program completes a sale only when the requested quantity is available. It then calculates the sales amount and remaining stock. The total revenue and number of medicines requiring restocking are maintained throughout the processing loop.

### Concepts Covered

- `for` loop for processing multiple medicines.
- `range()` for repeating the process a specified number of times.
- `if` and `else` for checking stock availability.
- Comparison operators such as `<`, `>=`, and `<=`.
- `while` loops for input validation.
- `int()` for stock quantities and medicine count.
- `float()` for medicine prices and revenue calculations.
- `try/except` with `ValueError` for invalid numeric input.
- **Accumulator:** `total_pharmacy_revenue` adds the amount of every successful sale.
- **Counter:** `medicines_requiring_restocking` counts medicines with fewer than 10 units remaining.
- Arithmetic operators for sales and remaining-stock calculations.
- F-strings and number formatting for the sales report.

### Program Logic and Validation

1. **Medicine count:** Requires a whole number greater than zero.
2. **Medicine name:** Rejects an empty name after removing surrounding spaces.
3. **Available stock:** Accepts a whole number greater than or equal to zero.
4. **Unit price:** Accepts a numeric price greater than zero.
5. **Quantity sold:** Accepts a whole number greater than or equal to zero.
6. **Stock availability:** Compares the requested sales quantity with available stock before completing a sale.
7. **Sales calculation:** Multiplies quantity sold by price per unit when stock is sufficient.
8. **Remaining stock:** Subtracts the quantity sold from available stock after a successful sale.
9. **Insufficient stock:** Reports the shortage, leaves stock unchanged, and does not add revenue for that medicine.
10. **Low-stock warning:** Displays a warning when remaining stock is below 10 units.
11. **Restocking counter:** Increases once for each processed medicine whose remaining stock is below 10 units.
12. **Revenue accumulator:** Adds successful sales amounts to the pharmacy's total revenue.
13. **Final report:** Displays the total number of medicines processed, total pharmacy revenue, and number of medicines requiring restocking.

**Important stock detail:** The low-stock condition is checked against the remaining stock after a sale. If a sale cannot be completed because stock is insufficient, the original stock remains unchanged and is still checked for the low-stock warning. A medicine with exactly 10 units remaining does not trigger the warning because the requirement is strictly below 10.

## How to Run

### Requirements

- Python 3 installed on your computer.
- A terminal or command prompt.
- No external Python packages are required.

### Run Task 1

```bash
python student_scholarship_system.py
```

### Run Task 2

```bash
python pharmacy_inventory_system.py
```

On some systems, use `python3` instead of `python`.

## Example Run — Task 1

```text
===== STUDENT SCHOLARSHIP ELIGIBILITY SYSTEM =====
Enter student name: Ali
Enter academic marks percentage (0-100): 92
Enter attendance percentage (0-100): 90
Enter monthly family income (Rs.): 40000

===== SCHOLARSHIP EVALUATION REPORT =====
Student Name: Ali
Academic Marks: 92.00%
Attendance: 90.00%
Monthly Family Income: Rs. 40,000.00
Scholarship Result: Full Scholarship
Eligibility Status: All scholarship requirements are satisfied.
=========================================
```

### Additional Task 1 Test Scenarios

| Marks | Attendance | Monthly Income | Expected Result |
|---:|---:|---:|---|
| 95 | 90 | Rs. 40,000 | Full Scholarship |
| 85 | 85 | Rs. 50,000 | Partial Scholarship |
| 75 | 90 | Rs. 40,000 | Ineligible — marks |
| 95 | 80 | Rs. 40,000 | Ineligible — attendance |
| 95 | 90 | Rs. 60,000 | Ineligible — income |
| 75 | 80 | Rs. 60,000 | Ineligible — all three reasons |

## Example Run — Task 2

```text
===== SMART PHARMACY INVENTORY & SALES SYSTEM =====
How many different medicines will be processed? 2

----- Medicine 1 of 2 -----
Enter medicine name: Paracetamol
Enter available stock (units): 50
Enter price per unit (Rs.): 20
Enter quantity to sell (units): 15

Sale Status: Successful
Medicine: Paracetamol
Quantity Sold: 15 units
Sales Amount: Rs. 300.00
Remaining Stock: 35 units

----- Medicine 2 of 2 -----
Enter medicine name: Cough Syrup
Enter available stock (units): 12
Enter price per unit (Rs.): 150
Enter quantity to sell (units): 5

Sale Status: Successful
Medicine: Cough Syrup
Quantity Sold: 5 units
Sales Amount: Rs. 750.00
Remaining Stock: 7 units
Low-Stock Warning: This medicine requires restocking.

===== DAILY PHARMACY SALES REPORT =====
Total Medicines Processed: 2
Total Pharmacy Revenue: Rs. 1,050.00
Medicines Requiring Restocking: 1
========================================
```

### Additional Task 2 Test Scenarios

| Available Stock | Quantity Sold | Expected Result |
|---:|---:|---|
| 50 | 15 | Sale successful; 35 units remain |
| 12 | 5 | Sale successful; 7 units remain; low-stock warning |
| 8 | 12 | Sale not completed; 8 units remain; low-stock warning |
| 20 | 20 | Sale successful; 0 units remain; low-stock warning |
| 20 | 10 | Sale successful; 10 units remain; no low-stock warning |
| 0 | 0 | Sale successful with zero revenue; low-stock warning |

## UI/UX Notes

Both applications are **console-based Python programs**, not graphical user interfaces. Their basic user-experience choices include:

- Clear application titles and report headings.
- Direct prompts that explain what information the user must enter.
- Input validation with understandable error messages.
- Currency labels (`Rs.`) and two decimal places for monetary values.
- Percentage labels for academic marks and attendance.
- Separate medicine-processing sections for easy tracking.
- Clear sale-status messages and low-stock warnings.
- Final reports that summarize the important results.

These choices make both programs easier for a beginner to use and understand. A future extension could add file-based record storage, a graphical interface, or database integration, but those features are outside the scope of this assessment.

## Practice Challenges

1. Add a student category and introduce a scholarship rule for that category.
2. Add a maximum scholarship amount or a fixed scholarship value.
3. Display the exact percentage or amount by which an ineligible student missed a requirement.
4. Store all medicine records in a list and display them in a final inventory table.
5. Add a medicine search feature.
6. Add a daily sales transaction count.
7. Explain why an accumulator is used for total revenue and a counter is used for restocking medicines.
8. Explain why `range(1, total_medicines + 1)` processes the required number of medicines.

## Suggested Git Commit

```text
Add scholarship and pharmacy management assessment programs
```

## Suggested Repository Description

Beginner Python assessment demonstrating conditional statements, input validation, loops, stock checking, scholarship eligibility decisions, counters, accumulators, and console-based business applications.
