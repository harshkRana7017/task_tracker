import fire
import json

def load_tasks(filename = "tasks.json"):
    try:
        with open(filename, 'r') as file:
            tasks= json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks, filename="tasks.json"):
    with open(filename,"w") as file:
        json.dump(tasks, file, indent=4)


def update_tasks(task_id, new_description=None, completed=None ):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            if new_description is not None:
                task["description"]= new_description
            if completed is not None :
                task["completed"] = completed
            break
    save_tasks(tasks)
    print(f"task with task id {task_id} updated")


def list_tasks():
        tasks = load_tasks()
        for task in tasks:
            status ="Completed" if task["completed"] else "Pending"
            print(f"{task['id']} {task['description']} - [{status}]") 

def add_task(description):
    tasks =load_tasks()
    task_id= len(tasks)+2
    task = {"id":task_id, "description":description, "completed": False}
    tasks.append(task)
    save_tasks(tasks)
    print(f"added task {description}")

def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if tasks["id"] != task_id]
    save_tasks(tasks)

class  TaskTracker:
    def add(self, description):
        add_task(description)

    def delete(self, task_id):
        delete_task(task_id)
    
    def list(self):
        list_tasks()

    def update(self,task_id, description, completed):
        update_tasks(task_id, description, completed)

if __name__ == '__main__':
    fire.Fire(TaskTracker)

