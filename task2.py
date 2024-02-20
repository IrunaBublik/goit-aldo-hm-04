def total_salary(path):
    numeric_values = []
    count = 0
    try:
        with open(path, 'r') as file:
            for line in file.readlines():
                line = line.split(',')
                numeric_values.append(int(line[1]))
                count+=1
           
        
        total_salary = sum(numeric_values) 

        try:
            average_sum = sum(numeric_values)//count
        except ZeroDivisionError as e:
            average_sum = 0
            print("Не вірнее використання функції")
            return None
        
        return total_salary,average_sum
    except(IndexError,ValueError) as e:
        print(f"Помилка обробки рядка '{item}' : {e}")
        return None
        


result =total_salary("salary_file.txt")           
if result is not None:
    total_salary_value,average_sum_value=result
    print(f"Загальна сума заробітної плати: {total_salary_value}, Середня заробітна плата: {average_sum_value}")
    