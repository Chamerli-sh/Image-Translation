from tkinter import Label, filedialog, Tk, Button


SUPPORTED_FILE_TYPES = ("Png Files", "*.png"), ("Jpg Files", "*.jpg"), ("All Files", "*.*")

def choose_file():
    file_chooser = filedialog.askopenfile(initialdir="~", title="Select an image", filetypes=(SUPPORTED_FILE_TYPES))
    return file_chooser
root = Tk()
root.title("Image Translator")
# root.iconbitmap("assets/icons/icon.png")

choose_file_button = Button(root, text="hello world", command=choose_file).pack()


root.mainloop()