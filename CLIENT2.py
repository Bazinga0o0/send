"""import tkinter as tk

class ChatGUI:
    def __init__(self, chats):
        self.chats = chats
        self.root = tk.Tk()
        self.root.geometry("400x400")
        

        self.chat_listbox = tk.Listbox(self.root)
        self.chat_listbox.pack(fill="both", expand=True, side="left")
        scrollbar = tk.Scrollbar(self.root)
        scrollbar.pack(fill="y", side="right")
        self.chat_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.chat_listbox.yview)
        
        for chat in self.chats:
            self.chat_listbox.insert(tk.END, chat["name"])
        self.chat_listbox.bind("<Double-Button-1>", self.open_chat)
        
        self.root.mainloop()


    def open_chat(self, event):
        selection = self.chat_listbox.curselection()
        if selection:
            chat_index = selection[0]
            chat = self.chats[chat_index]
            chat_window = tk.Toplevel(self.root)
            chat_window.title(chat["name"])
            chat_window.geometry("400x400")
            

            input_frame = tk.Frame(chat_window)
            input_frame.pack(side="bottom", fill="x")
            input_entry = tk.Entry(input_frame)
            input_entry.pack(side="left", fill="x", expand=True)
            send_button = tk.Button(input_frame, text="Send", command=lambda: self.send_message(chat_text, input_entry))
            send_button.pack(side="right")
            

            chat_text = tk.Text(chat_window)
            chat_text.pack(fill="both", expand=True)
            scrollbar = tk.Scrollbar(chat_window)
            scrollbar.pack(side="right", fill="y")
            chat_text.config(yscrollcommand=scrollbar.set)
            scrollbar.config(command=chat_text.yview)
            chat_text.insert(tk.END, chat["messages"])
    
    def send_message(self, chat_text, input_entry):
        message = input_entry.get()
        if message:
            chat_text.insert(tk.END, "\n" + message)
            input_entry.delete(0, tk.END)

chats = [
    {"name": "Chat 1", "messages": "Hello from Chat 1!"},
    {"name": "Chat 2", "messages": "Greetings from Chat 2!"},
    {"name": "Chat 3", "messages": "Salutations from Chat 3!"}
]

ChatGUI(chats)"""
"""import tkinter as tk

class ChatGUI:
    def __init__(self, chats):
        self.chats = chats
        self.root = tk.Tk()
        self.root.geometry("400x400")  
        

        self.chat_listbox = tk.Listbox(self.root)
        self.chat_listbox.pack(fill="both", expand=True, side="left")
        scrollbar = tk.Scrollbar(self.root)
        scrollbar.pack(fill="y", side="right")
        self.chat_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.chat_listbox.yview)
        
        for chat in self.chats:
            self.chat_listbox.insert(tk.END, chat["name"])
        self.chat_listbox.bind("<Double-Button-1>", self.open_chat)
        

        self.root.after(1000, self.reload_chats)
        
        self.root.mainloop()


    def open_chat(self, event):
        selection = self.chat_listbox.curselection()
        if selection:
            chat_index = selection[0]
            chat = self.chats[chat_index]
            chat_window = tk.Toplevel(self.root)
            chat_window.title(chat["name"])
            chat_window.geometry("400x400")
            

            input_frame = tk.Frame(chat_window)
            input_frame.pack(side="bottom", fill="x")
            input_entry = tk.Entry(input_frame)
            input_entry.pack(side="left", fill="x", expand=True)
            send_button = tk.Button(input_frame, text="Send", command=lambda: self.send_message(chat_text, input_entry))
            send_button.pack(side="right")
            

            input_entry.bind("<Return>", lambda event: self.send_message(chat_text, input_entry))
            

            chat_text = tk.Text(chat_window)
            chat_text.pack(fill="both", expand=True)
            scrollbar = tk.Scrollbar(chat_window)
            scrollbar.pack(side="right", fill="y")
            chat_text.config(yscrollcommand=scrollbar.set)
            scrollbar.config(command=chat_text.yview)
            chat_text.insert(tk.END, chat["messages"])
            chat["text_widget"] = chat_text
    
    def send_message(self, chat_text, input_entry):
        message = input_entry.get()
        if message:
            chat_text.insert(tk.END, "\n" + message)
            input_entry.delete(0, tk.END)
    
    def send_message_to_chat(self, chat_index, message):
        chat = self.chats[chat_index]
        chat_text = chat["text_widget"]
        chat_text.insert(tk.END, "\n" + message)
    
    def reload_chats(self):
        selection = self.chat_listbox.curselection()
        
        self.chat_listbox.delete(0, tk.END)
        for chat in self.chats:
            self.chat_listbox.insert(tk.END, chat["name"])
        
        if selection:
            self.chat_listbox.selection_set(selection)
        
        self.root.after(1000, self.reload_chats)

chats = [
    {"name": "Chat 1", "messages": "Hello from Chat 1!"},
    {"name": "Chat 2", "messages": "Greetings from Chat 2!"},
    {"name": "Chat 3", "messages": "Salutations from Chat 3!"}
]

ChatGUI(chats)

"""

#wscat -c ws://localhost:8765

