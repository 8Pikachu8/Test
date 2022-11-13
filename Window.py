from matplotlib import pyplot as plt
from ChildWindows import *
import Population
import numpy as np


class Window:
    def __init__(self, width, height, title):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+100+75")
        # self.root.resizable(False, False)
        self.displayed_time = StringVar(value='0')

        self.button = None

    def run(self):
        self.draw()
        self.root.mainloop()

    def draw(self):
        self.draw_menu()

        frame = Frame(self.root, background='#3399FF',width=200,height=150)
        frame.pack(anchor=CENTER)
        Label(frame, text="Кол-во особей", background='#3399FF').pack()

        ent_count = Entry(frame, width=25, textvariable=self.displayed_time, background='#3399FF', state=DISABLED)
        ent_count.pack(anchor=CENTER)

        self.button = Button(frame, text="Start", command=self.start_exec, background='#3399FF')
        self.button.pack()


    def draw_menu(self):
        main_menu = Menu(self.root)

        file_menu = Menu(main_menu, tearoff=0)
        file_menu.add_command(label="Новая система", command=self.create_system)
        main_menu.add_cascade(label="Файл", menu=file_menu)

        main_menu.add_command(label="Параметры", command=self.change_params)
        self.root.configure(menu=main_menu)

    def create_system(self):
        Window1(self.root, "Новая система")

    def change_params(self):
        a = Window2(self.root, "Параметры")
        a.draw()

    def start_exec(self):
        print('\nStarted execution...')
        a = 0
        Population_array = []
        for i in Config.param_values:
            Population_array.append(Population.Population(i[1], i[0], i[2]))
        T_array = np.arange(0, Config.time + Config.delta, Config.delta)
        for i in T_array:

            for population in Population_array:
                population.method_runge_kutta(Population_array)
                a += population.N
            print("Alln= ", a)
            self.displayed_time.set(str(a))

        for population in Population_array:
            plt.plot(T_array, population.array_N, linestyle='--', label=f"id = {population.id}")
        plt.legend()
        plt.show()
