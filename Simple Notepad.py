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
        edit_menu = tk.Menu(menubar, tearoff=0)
        # ... (Edit menu options)
        menubar.add_cascade(label="File", menu=file_menu)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        self.root.config(menu=menubar)

    # Alpha Jesse
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
