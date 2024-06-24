import datetime
import tkinter as tk
from tkinter import scrolledtext

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
        elif days == 0:
            categorized_tasks['today'].append(f"Прямо сейчас происходит {description}")
        else:
            categorized_tasks['future'].append(f"Осталось {days} дней до {description}")
    return categorized_tasks

def display_tasks(categorized_tasks, text_widget):
    text_widget.config(state=tk.NORMAL)
    text_widget.delete(1.0, tk.END)

    text_widget.insert(tk.END, "\nМои текущие задачи\n\n", 'title')

    for task in categorized_tasks['past']:
        text_widget.insert(tk.END, f"{task}\n", 'past')
    for task in categorized_tasks['today']:
        text_widget.insert(tk.END, f"{task}\n", 'today')
    for task in categorized_tasks['future']:
        text_widget.insert(tk.END, f"{task}\n", 'future')

    text_widget.config(state=tk.DISABLED)

def main():
    tasks = read_tasks('tasks.txt')
    categorized_tasks = categorize_tasks(tasks)

    root = tk.Tk()
    root.title("Что мне делать, как мне жить?")

    text_widget = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, font=("Helvetica", 12))
    text_widget.pack(padx=10, pady=10)

    text_widget.tag_configure('title', font=("Helvetica", 16, 'bold'), justify='center')
    text_widget.tag_configure('past', foreground='red')
    text_widget.tag_configure('today', foreground='orange')
    text_widget.tag_configure('future', foreground='green')

    display_tasks(categorized_tasks, text_widget)

    root.mainloop()

if __name__ == "__main__":
    main()
