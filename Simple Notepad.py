# Egena Sylvester
import tkinter as tk
from tkinter import filedialog


class NotepadApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Notepad")
        self.text_widget = tk.Text(self.root, wrap='word', undo=True)
        self.text_widget.pack(expand=True, fill='both')
        self.create_menu()

    # Ali Andrew
    def create_menu(self):
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        # ... (File menu options)
        file_menu.add_command(label='Save', command=self.save_file)
        file_menu.add_command(label='Save as', command=self.save_as_file)
        file_menu.add_command(label='New File', command=self.new_file)
        file_menu.add_command(label='Open File', command=self.open_file)
        edit_menu = tk.Menu(menubar, tearoff=0)
        # ... (Edit menu options)
        edit_menu.add_command(label='Copy Text', command=self.copy_text)
        edit_menu.add_command(label='Cut Text', command=self.cut_text)
        edit_menu.add_command(label='Select All', command=self.select_all)
        edit_menu.add_command(label='Paste Text', command=self.paste_text)
        
        menubar.add_cascade(label="File", menu=file_menu)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        self.root.config(menu=menubar)

    # Alpha Jesse
    def shortcuts(self, event):
        # Ctrl+S
        if (event.keysym, event.state) == ('s', 4):
            self.save_file()
        # Ctrl+N
        if (event.keysym, event.state) == ('n', 4):
            self.new_file()
        # Ctrl+O
        if (event.keysym, event.state) == ('o', 4):
            self.open_file()
    
    def new_file(self):
        self.text_widget.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                               filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.text_widget.delete(1.0, tk.END)
                self.text_widget.insert(tk.END, content)
            self.root.title(f"Simple Notepad - {file_path}")

    def save_file(self):
        if hasattr(self, 'file_path'):
            content = self.text_widget.get(1.0, tk.END)
            with open(self.file_path, 'w') as file:
                file.write(content)
        else:
            self.save_as_file()

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            content = self.text_widget.get(1.0, tk.END)
            with open(file_path, 'w') as file:
                file.write(content)
            self.file_path = file_path
            self.root.title(f"Simple Notepad - {file_path}")

    # Kayode Miracle
    def cut_text(self):
        self.text_widget.event_generate("<<Cut>>")

    def copy_text(self):
        self.text_widget.event_generate("<<Copy>>")

    def paste_text(self):
        self.text_widget.event_generate("<<Paste>>")

    def select_all(self):
        self.text_widget.tag_add(tk.SEL, "1.0", tk.END)


# Onyukwu Giddel
if __name__ == "__main__":
    root = tk.Tk()
    app = NotepadApp(root)
    root.mainloop()
