from typing import TextIO
from io import StringIO

while True:
    task = input("What task do you have? (type 'exit' to quit): ")
    task = task.lower()
    tracker_file = task
    if task == "exit":
        print('Thank you')
        break
    try:
        with open(tracker_file, 'w') as file:
            file.write(task)
            print('Sucessfully recorded task')
    except FileNotFoundError:
        print('File not found')