import tkinter as tk

class MyGui:
    def __init__(self):
        self.setup_window()
        self.headerLabel = self.create_label(self.root, text='Simple Calculator', font=('Arial', 10, 'bold'), fg='red')
        self.textBox = self.create_textbox(self.root, 5, ('Arial', 10))
        
        # Define the button frame
        self.buttonFrame = tk.Frame(self.root)
        for i in range(0, 4):
            self.buttonFrame.columnconfigure(i, weight=1)
        
        rowVar, colVar = 0, 0
        # Define the buttons
        for i in range(1, 6):
            # Num pad 1-3
            if(i == 1):
                rowVar = 3
                for j in range(1, 5):
                    if(j < 4):
                        buttonName = "btn" + str(j)
                        self.buttonName = self.create_button(self.buttonFrame, str(j), font=('Arial', 10), row=rowVar, column=colVar, sticky=tk.W+tk.E+tk.N, command=lambda x=str(j): self.on_button_click(x))
                    else:
                        self.btnMinus = self.create_button(self.buttonFrame, '\u2212', ('Arial', 10), row=rowVar, column=colVar, sticky=tk.W+tk.E+tk.N, command=lambda x='\u2212': self.on_button_click(x))
                    colVar += 1
            # Num pad 4-6
            elif(i == 2):
                rowVar = 2
                colVar = 0
                for j in range(4, 8):
                    if(j < 7):
                        buttonName = "btn" + str(j)
                        self.buttonName = self.create_button(self.buttonFrame, str(j), font=('Arial', 10), row=rowVar, column=colVar, sticky=tk.W+tk.E+tk.N, command=lambda x=str(j): self.on_button_click(x))
                    else:
                        self.btnMultiply = self.create_button(self.buttonFrame, '\u00D7', ('Arial', 10), rowVar, colVar, sticky=tk.W+tk.E+tk.N, command=lambda x='\u00D7': self.on_button_click(x))
                    colVar += 1
            # Num pad 7-9
            elif(i == 3):
                rowVar = 1
                colVar = 0
                for j in range(7, 11):
                    if(j < 10):
                        buttonName = "btn" + str(j)
                        self.buttonName = self.create_button(self.buttonFrame, str(j), ('Arial', 10), rowVar, colVar, sticky=tk.W+tk.E+tk.N, command=lambda x=str(j): self.on_button_click(x))
                    else:
                        self.btnDivide = self.create_button(self.buttonFrame, '\u00F7', ('Arial', 10), rowVar, colVar, tk.W+tk.E+tk.N, command=lambda x='\u00F7': self.on_button_click(x))
                    colVar += 1
            # Num pad 0, =, +, .
            elif(i == 4):
                rowVar = 4
                colVar = 0
                for j in range(0, 4):
                    if(j == 0):
                        self.btn0 = self.create_button(self.buttonFrame, '0', ('Arial', 10), rowVar, colVar, tk.W+tk.E+tk.N, command=lambda x='0': self.on_button_click(x))
                    elif(j == 1):
                        self.btnDot = self.create_button(self.buttonFrame, '\u002E', ('Arial', 10), rowVar, colVar, tk.W+tk.E+tk.N, command=lambda x='\u002E': self.on_button_click(x))
                    elif(j == 2):
                        self.btnEqual = self.create_button(self.buttonFrame, '\u003D', ('Arial', 10), rowVar, colVar, tk.W+tk.E+tk.N, command=self.calculate)
                    else:
                        self.btnPlus = self.create_button(self.buttonFrame, '\u002B', ('Arial', 10), rowVar, colVar, tk.W+tk.E+tk.N, command=lambda x='\u002B': self.on_button_click(x))
                    colVar += 1
            else:
                rowVar = 0
                colVar = 0
                for j in range(0, 4):
                    if(j == 0):
                        self.btnBracketLeft = self.create_button(self.buttonFrame, '(', ('Arial', 10), rowVar, colVar, tk.W+tk.E, command=lambda x='(': self.on_button_click(x))
                    elif(j == 1):
                        self.btnBracketRight = self.create_button(self.buttonFrame, ')', ('Arial', 10), rowVar, colVar, tk.W+tk.E, command=lambda x=')': self.on_button_click(x))
                    elif(j == 2):
                        self.btnPercent = self.create_button(self.buttonFrame, '%', ('Arial', 10), rowVar, colVar, tk.W+tk.E, command=lambda x='%': self.on_button_click(x))
                    else:
                        self.btnClear = self.create_button(self.buttonFrame, '\u232B', ('Arial', 10), rowVar, colVar, tk.W+tk.E, command=self.clear_text)
                    colVar += 1
                
        
        # Pack the button frame to show the buttons
        self.buttonFrame.pack(fill='x')
        
        self.root.mainloop()
        
    def setup_window(self):
        self.root = tk.Tk()
        self.root.geometry('500x500')
        self.root.title('Calculator')
        
    def create_label(self, parent, text, font, fg):
        label = tk.Label(parent, text=text, font=font)
        label.config(fg=fg)
        label.pack(padx=10, pady=10)
        return label
        
    def create_textbox(self, parent, height, font):
        textBox = tk.Text(parent, height=height, font=font)
        textBox.pack(padx=10, pady=10)
        return textBox
        
    def create_button(self, parent, text, font, row, column, sticky, command):
        button = tk.Button(parent, text=text, font=font, command=command)
        button.grid(row=row, column=column, sticky=sticky)
        return button
        
    def on_button_click(self, value):
        self.textBox.insert(tk.END, value)
    
    def clear_text(self):
        self.textBox.delete('1.0', tk.END)
        
    def calculate(self):
        content = self.textBox.get('1.0', tk.END)
        contentLength = len(content.strip())
        contentExpression = content.strip()
        
        contentExpFinal = ""
        for i in contentExpression:
            # If divide icon
            if i == '\u00F7':
                contentExpFinal += "/"
            # If multiply icon
            elif i == '\u00D7':
                contentExpFinal += "*"
            # Ignore % sign
            elif i == '%':
                continue
            else:
                contentExpFinal += i
        
        
        finalAnswer = eval(contentExpFinal)
        self.textBox.delete('1.0', tk.END)
        self.textBox.insert(tk.END, str(finalAnswer))
        
        
        
MyGui()
    