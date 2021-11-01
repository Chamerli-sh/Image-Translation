from tkinter import filedialog, Tk, Button




def choose_file():
    file_chooser = filedialog.askopenfile(initialdir="~", title="Select an image", filetypes=(("Png Files", "*.png"), ("Jpg Files", "*.jpg"), ("All Files", "*.*")))

root = Tk()
root.title("Image Translator")
# root.iconbitmap("assets/icons/icon.png")



choose_file_button = Button(root, text="hello world", command=choose_file).pack()

root.mainloop()