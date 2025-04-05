import functions
import FreeSimpleGUI as sg

label=sg.Text("Type in a to-do")
input_box=sg.InputText(tooltip="enter to-do",key="todo")
add_button=sg.Button("Add")
edit_button=sg.Button("Edit")
list_box=sg.Listbox(values=functions.get_todos(),key='todo_listbox',enable_events=True,
                    size=[45,10])
complete_button=sg.Button("Complete")
exit_button=sg.Button("Exit")


window= sg.Window('My To-do App',
                  layout=[[label] , [input_box,add_button],[list_box,edit_button,complete_button],[exit_button]],
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
            todo_to_edit = values['todo_listbox'][0]
            new_todo=values['todo']+"\n"

            todos=functions.get_todos()
            index=todos.index(todo_to_edit)
            todos[index]=new_todo
            functions.write_todos(todos)

            window['todo_listbox'].update(values=todos)
        case 'todo_listbox':
            window['todo'].update(value=values['todo_listbox'][0])
        case "Complete":
            todo_to_complete=values["todo_listbox"][0]
            todos=functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window["todo_listbox"].update(values=todos)
            window["todo"].update(value='')
        case "Exit":
            break


        case sg.WIN_CLOSED:
            break

window.close()