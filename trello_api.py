import requests
import sys

auth_params = {
    'key':"",
    'token':"",
}

base_url = "https://api.trello.com/1/{}"
board_id = ""

def read():
    column_data = requests.get(base_url.format('boards')+'/'+board_id+'/lists',params=auth_params).json()
    for column in column_data:
        task_data = requests.get(base_url.format('lists')+'/'+column['id']+'/cards', params=auth_params).json()
        print(column['name'] + ' ['+str(len(task_data))+']')
        if not task_data:
            print('\t'+'Нет задач')
            continue
        for task in task_data:
            print('\t' + task['name'])

def create(name, column_name):
    column_data = requests.get(base_url.format('boards')+'/'+board_id+'/lists',params=auth_params).json()
    for column in column_data:
        if column['name']==column_name:
            requests.post(base_url.format('cards'),data={'name':name,'idList':column['id'],**auth_params})
            break

def move(name, column_name):
    task_dict = {}
    count = 0
    column_data = requests.get(base_url.format('boards')+'/'+board_id+'/lists',params=auth_params).json()
    task_id = None
    for column in column_data:
        column_tasks = requests.get(base_url.format('lists')+'/'+column['id']+'/cards',params=auth_params).json()
        for task in column_tasks:
            task_dict.update({task['dateLastActivity']:[task['name'],column['name'], task['id']]})
    for i in task_dict.keys():
        if task_dict[i][0] == name:
            count+=1    
    if count>1:
        print('Внимание! Найдено несколько одинаковых задач:')
        for i in task_dict.keys():
            if task_dict[i][0] == name:
                print('Имя: '+task_dict[i][0]+' Колонка: '+task_dict[i][1]+' Время последней активности: '+i)
        
        date = input('Скопируйте дату и вставьте здесь: ')
        for i in task_dict.keys():
            if i == date:
                task_id=task_dict[i][2]
    else:
        for i in task_dict.keys():
            if task_dict[i][0] == name:
                task_id=task_dict[i][2]
                break 

    for column in column_data:
        if column['name']==column_name:
            requests.put(base_url.format('cards')+'/'+task_id+'/idList',data={'value':column['id'],**auth_params})
            break

def create_list(name):
    requests.post(base_url.format('boards')+'/'+board_id+'/lists', data={'name':name,**auth_params})
    

if __name__ == "__main__":
    if len(sys.argv)<=1:
        read()
    elif sys.argv[1] == 'create':
        create(sys.argv[2],sys.argv[3])
    elif sys.argv[1] == 'move':
        move(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == 'create_list':
        create_list(sys.argv[2])

