import functions
import FreeSimpleGUI as sg

label=sg.Text("Type in a to-do")
input_box=sg.InputText(tooltip="enter to-do",key="todo")
add_button=sg.Button("Add")



window= sg.Window('My To-do App',
                  layout=[[label] , [input_box,add_button]],
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
        case sg.WIN_CLOSED:
            break

window.close()