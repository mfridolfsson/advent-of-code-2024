##to do finish this day

with open('data.txt', 'r') as f:
   lines = f.read().split('\n')

output = 0
reports = []

for index, item in enumerate(lines):
    report = list(map(int, item.split(' ')))
    reports.append(report)

for index, report in enumerate(reports):
    is_safe = 1
    issues = 0
    print(report)
    sorted_report = report.copy()
    sorted_report.sort()
    reverse_sorted_report = report.copy()
    reverse_sorted_report.sort(reverse=True)
    ## not either all increasing or all decreasing.
    if report != sorted_report and report != reverse_sorted_report:
        is_safe = 0

    const_safe_dif = 3

    for index, item in enumerate(report):
        if index == 0:
            dif = abs(item - report[index+1])
            if dif > const_safe_dif or dif == 0:
                is_safe = 0
                issues += 1
        elif index == len(report)-1:
            dif = abs(item - report[index-1])
            if dif > const_safe_dif or dif == 0:
                is_safe = 0
                issues += 1
        else:
            dif = abs(item - report[index+1])
            if dif > const_safe_dif or dif == 0:
                is_safe = 0
                issues += 1
            dif = abs(item - report[index-1])
            if dif > const_safe_dif or dif == 0:
                is_safe = 0
                issues += 1
    
    print(is_safe)
    if issues < 3:
        output += 1
    print(output)
    


