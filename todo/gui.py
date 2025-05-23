import functions
import FreeSimpleGUI as sg
import time

sg.theme("black")
clock=sg.Text('',key="clock")
label=sg.Text("Type in a to-do")
input_box=sg.InputText(tooltip="enter to-do",key="todo")
add_button=sg.Button(key="Add",image_source="add.png",size=2,mouseover_colors="LightBlue2",tooltip="add button")
edit_button=sg.Button("Edit")
list_box=sg.Listbox(values=functions.get_todos(),key='todo_listbox',enable_events=True,
                    size=[45,10])
complete_button=sg.Button(key="Complete",image_source="complete.png",size=2,mouseover_colors="LightBlue2",tooltip="complete button")
exit_button=sg.Button("Exit")


window= sg.Window('My To-do App',
                  layout=[[clock],[label] , [input_box,add_button],[list_box,edit_button,complete_button],[exit_button]],
                  font=('Helvetica',12))
while True:
    event,values=window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d,%Y %H:%M:%S"))
    match event:
        case "Add":
            todos=functions.get_todos()
            new_todo=values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todo_listbox'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todo_listbox'][0]
                new_todo=values['todo']+"\n"

                todos=functions.get_todos()
                index=todos.index(todo_to_edit)
                todos[index]=new_todo
                functions.write_todos(todos)
                window['todo_listbox'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item",font=('Helvetica',12))

        case 'todo_listbox':
            window['todo'].update(value=values['todo_listbox'][0])
        case "Complete":
            try:
                todo_to_complete=values["todo_listbox"][0]
                todos=functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todo_listbox"].update(values=todos)
                window["todo"].update(value='')
            except IndexError:
                sg.popup("Please select an item", font=('Helvetica', 12))
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break


window.close()