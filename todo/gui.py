import functions
import FreeSimpleGUI as sg

label=sg.Text("Type in a to-do")
input_box=sg.InputText(tooltip="enter to-do",key="todo")
add_button=sg.Button("Add")
edit_button=sg.Button("Edit")
list_box=sg.Listbox(values=functions.get_todos(),key='todo_edit',enable_events=True,
                    size=[45,10])


window= sg.Window('My To-do App',
                  layout=[[label] , [input_box,add_button],[list_box,edit_button]],
                  font=('Helvetica',12))
while True:
    event,values=window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos=functions.get_todos()
            new_todo=values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todo_edit'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todo_edit'][0]
            new_todo=values['todo']+"\n"

            todos=functions.get_todos()
            index=todos.index(todo_to_edit)
            todos[index]=new_todo
            functions.write_todos(todos)

            window['todo_edit'].update(values=todos)
        case 'todo_edit':
            window['todo'].update(value=values['todo_edit'][0])


        case sg.WIN_CLOSED:
            break

window.close()