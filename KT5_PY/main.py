import datetime

def read_tasks(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks

def calculate_days(task_date):
    today = datetime.date.today()
    task_date = datetime.datetime.strptime(task_date, "%Y-%m-%d").date()
    delta = (task_date - today).days
    return delta

def categorize_tasks(tasks):
    categorized_tasks = {'past': [], 'today': [], 'future': []}
    for task in tasks:
        description, date_str = task.split(' - ')
        days = calculate_days(date_str)
        if days < 0:
            categorized_tasks['past'].append(f"Прошло {-days} дней от {description}")
        elif days > 0:
            categorized_tasks['future'].append(f"Осталось {days} дней до {description}")
        else:
            categorized_tasks['today'].append(f"Прямо щас происходит {description}")
    return categorized_tasks

def display_tasks(categorized_tasks):
    print("\nМои текущие задачи\n")
    for task in categorized_tasks['past']:
        print(f"\033[91m{task}\033[0m")
    for task in categorized_tasks['today']:
        print(f"\033[93m{task}\033[0m")
    for task in categorized_tasks['future']:
        print(f"\033[92m{task}\033[0m")

def main():
    tasks = read_tasks('tasks.txt')
    categorized_tasks = categorize_tasks(tasks)
    display_tasks(categorized_tasks)

if __name__ == "__main__":
    main()
