from tkinter import *
import pymysql



def save_data():
    group_name = group_entry.get()
    room_number = room_entry.get()

    print("Group Name:", group_name)
    print("Room Number:", room_number)

    # очищаем поля ввода после сохранения данных
    group_entry.delete(0, 'end')
    room_entry.delete(0, 'end')




root = Tk()  # создаем корневой объект - окно
root.title("Кураторка")  # устанавливаем заголовок окна
root.geometry("600x300")  # устанавливаем размеры окна


label = Label(text="Программа для создания расписания\nВведите название группы и аудиторию")  # создаем текстовую метку
label.pack()  # размещаем метку в окне


group_label = Label(root, text="Group Name:")
group_label.pack()


group_entry = Entry(root)
group_entry.pack()


room_label = Label(root, text="Аудитория:")
room_label.pack()


room_entry = Entry(root)
room_entry.pack()


save_button = Button(root, text="Save", command=save_data)
save_button.pack()


root.mainloop()


save_button = Button(root, text="Save", command=save_data)
save_button.pack()

root.mainloop()
