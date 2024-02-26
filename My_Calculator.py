import tkinter as tk
import math

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry('600x600')
        self.root.configure(bg='#2C3E50')
        self.root.title('CALCULATOR')

        # Calculator state variables
        self.f_num = 0
        self.math_operation = None

        # First button of the window
        self.first_button = tk.Button(root, text='Starte den Taschenrechner!', font=('Helvetica', 15, 'bold'), fg='#2C3E50',
                                      bg='#3498DB', border=5, width=18, height=3, command=self.activate_calculator)
        self.first_button.pack(pady=20)

    def activate_calculator(self):
        self.first_button.destroy()  # destroy the first button when clicked

        # Frame of the calculator's buttons
        calculator_frame = tk.Frame(self.root, bg='#2C3E50')
        calculator_frame.pack()

        # Create an entry for the numbers
        self.display = tk.Entry(calculator_frame, width=16, font=('Helvetica', 30, 'bold'), bg='#34495E', fg='#ECF0F1', bd=10, relief=tk.FLAT)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'CLR', '=', '+',
            'cos', 'sin', 'tan', '.'
        ]

        row_val = 1
        col_val = 0
        for button_text in buttons:
            tk.Button(calculator_frame, text=button_text, width=6, height=3, font=('Helvetica', 15, 'bold'), fg='#2C3E50', bg='#3498DB', bd=5,
                      command=lambda text=button_text: self.button_click(text)).grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def button_click(self, button_text):
        if button_text == 'CLR':
            self.clear_display()
        elif button_text in {'+', '-', '*', '/'}:
            self.perform_operation(button_text)
        elif button_text == '=':
            self.calculate_result()
        elif button_text in {'cos', 'sin', 'tan'}:
            self.perform_trigonometric_operation(button_text)
        else:
            current = self.display.get()
            self.clear_display()
            self.display.insert(0, str(current) + str(button_text))

    def clear_display(self):
        self.display.delete(0, tk.END)

    def perform_operation(self, operator):
        first_number = self.display.get()
        self.math_operation = operator
        self.f_num = float(first_number)
        self.clear_display()

    def perform_trigonometric_operation(self, operation):
        current_value = float(self.display.get())
        result = None
        if operation == 'cos':
            result = math.cos(math.radians(current_value))
        elif operation == 'sin':
            result = math.sin(math.radians(current_value))
        elif operation == 'tan':
            result = math.tan(math.radians(current_value))
        self.clear_display()
        self.display.insert(0, result)

    def calculate_result(self):
        second_number = self.display.get()
        self.clear_display()

        try:
            if self.math_operation == "+":
                self.display.insert(0, self.f_num + float(second_number))
            elif self.math_operation == "-":
                self.display.insert(0, self.f_num - float(second_number))
            elif self.math_operation == "*":
                self.display.insert(0, self.f_num * float(second_number))
            elif self.math_operation == "/":
                self.display.insert(0, self.f_num / float(second_number))
        except ZeroDivisionError:
            self.display.insert(0, "Error")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
