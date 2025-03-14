task_list=[]
def add_task():
    task= input('Enetr the task: ')
    task_list.append({'Task':task, 'status':'pending'})
    print ('The task is added successfully ')

def complete_task():
    if len(task_list)==0:
        print ('List is empty')
    else:
        try:
            search_list= int(input('Enter the task that you want to complete: '))-1
            if 0<= search_list<len(task_list):
                task_list[search_list]['status']='complete'
                print(f'Task {task_list[search_list]['Task']}has been complete')
            else:
                print ('Enter a valid task list: ')

        except ValueError:
            print('Enter a valid task number')
    

def view_task():
    if len(task_list)==0:
        print('No pending Task')
    else:
        for index, task in enumerate(task_list,1):
            print(f'{index}  {task['Task']} - {task['status']}')



while True:
    print('\n***Main Menu***\n 1. Add\n 2. Status\n 3. View\n 4. Exit')
    choice= input('Enter your choice: ')
    if choice=='1':
        add_task()
    elif choice=='2':
        complete_task()
    elif choice=='3':
        view_task()
    elif choice=='4':
        break
    else:
        print ('invalid choice, Enter again')
        

