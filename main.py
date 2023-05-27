from ui.main_window import MainWindow


# Точка входа
def main():
    main_window = MainWindow()
    main_window.start_mainloop()

    return 0


if __name__ == '__main__':
    main()