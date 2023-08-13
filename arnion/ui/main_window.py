import tkinter as tk

from arnion.Data.departments_data import DepartmentDataHandler, DepartmentDataObject
from arnion.Data.employees_data import EmployeeDataHandler, EmployeeDataObject
from arnion.ui.departments_data_ui import DepartmentsWindow
from arnion.ui.departments_reports_ui import DepartmentsReportWindow
from arnion.ui.employees_data_ui import EmployeesWindow
from arnion.ui.employees_reports_ui import EmployeesReportWindow


class MainWindow:

    # Конструктор
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("310x380")
        self.window.title("Span")

        # Добавление метки заголовка
        lbl_title = tk.Label(text ="Span", font=('Helvetica', 16, 'bold'), fg='#0000cc', justify='center')
        lbl_title.place(x=25, y=15, width=250, height=50)

        # Добавление метки заголовка данных
        lbl_title = tk.Label(text="Данные", font=('Helvetica', 12, 'bold'), fg='#0066ff', justify='center')
        lbl_title.place(x=25, y=55, width=250, height=50)

        # Добавление кнопки данных ОТДЕЛЫ
        btn_report = tk.Button(self.window, text="Отделы",
                               font=('Helvetica', 10, 'bold'), bg='#ccffcc', command=self.do_list_departments)
        btn_report.place(x=25, y=100, width=120, height=50)

        # Добавление кнопки данных СОТРУДНИКИ
        btn_close = tk.Button(self.window, text="Сотрудники",
                               font=('Helvetica', 10, 'bold'), bg='#ccffcc', command=self.do_list_employees)
        btn_close.place(x=160, y=100, width=120, height=50)

        # Добавление метки заголовка отчетов
        lblTitle1 = tk.Label(text="Отчеты", font=('Helvetica', 12, 'bold'), fg='#0066ff', justify='center')
        lblTitle1.place(x=25, y=155, width=250, height=50)

        # Добавление кнопки отчетов ОТДЕЛЫ
        btn_report = tk.Button(self.window, text="Отделы",
                               font=('Helvetica', 10, 'bold'), bg='#ccffcc', command=self.do_report_departments)
        btn_report.place(x=25, y=200, width=120, height=50)

        # Добавление кнопки отчетов СОТРУДНИКИ
        btn_close = tk.Button(self.window, text="Сотрудники",
                              font=('Helvetica', 10, 'bold'), bg='#ccffcc', command=self.do_report_employees)
        btn_close.place(x=160, y=200, width=120, height=50)


        # # Добавление кнопки TEST
        # btn_test = tk.Button(self.window, text="TEST",
        #                       font=('Helvetica', 10, 'bold'), bg='#ffffcc', command=self.do_test)
        # btn_test.place(x=25, y=300, width=120, height=50)


        # Добавление кнопки закрытия программы
        btn_close = tk.Button(self.window, text="выход",
                              font=('Helvetica', 10, 'bold'), bg='#ccffcc', command=self.close)
        btn_close.place(x=160, y=300, width=120, height=50)
# Функция Тест
    def do_test(self):
        employee = EmployeeDataObject(first_name="Ирина", middle_name="Юрьевна",
                                      last_name="Костюченко", department_id="3")
        print(employee.employee_id)
        EmployeeDataHandler.insert(employee)
        print(employee.employee_id)
        print("Готово")

    # открытие списка Отделы
    def do_list_departments(self):
        rpt = DepartmentsWindow()
        rpt.open()

    # открытие списка сотрудники
    def do_list_employees(self):
        rpt = EmployeesWindow()
        rpt.open()


    # открытие отчета Отделы

    def do_report_departments(self):
        rpt = DepartmentsReportWindow()
        rpt.open()

    # открытие отчета Сотрудники

    def do_report_employees(self):
        rpt = EmployeesReportWindow()
        rpt.open()

    # Функция закрытия окна
    def close(self):
        self.window.destroy()


    # Запуск цикла окна
    def start_mainloop(self):
        self.window.mainloop()