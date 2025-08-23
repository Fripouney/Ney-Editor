import tkinter as tk

class Config:
    @staticmethod
    def add_text_area_bindings(text_area):
        text_area.bind("<Control-b>", lambda event: Config.toggle_tag(text_area, "bold"))
        text_area.bind("<Control-i>", lambda event: Config.toggle_tag(text_area, "italic"))
        text_area.bind("<Control-u>", lambda event: Config.toggle_tag(text_area, "underline"))

    @staticmethod
    def config_tags(text_area):
        text_area.tag_configure("bold", font=("Arial", 12, "bold"))
        text_area.tag_configure("italic", font=("Arial", 12, "italic"))
        text_area.tag_configure("underline", font=("Arial", 12, "underline"))

    @staticmethod
    def toggle_tag(text_area, tag, event=None):
        try:
            current_tags = text_area.tag_names("sel.first")
            if tag in current_tags:
                text_area.tag_remove(tag, "sel.first", "sel.last")
            else:
                text_area.tag_add(tag, "sel.first", "sel.last")
        except tk.TclError:
            print("No text selected to toggle tag.")
            pass

        return "break"
    
    @staticmethod
    def set_status_bar(status_bar, text):
        status_bar.config(state="normal")
        status_bar.delete(1.0, tk.END)
        status_bar.insert(tk.END, text)
        status_bar.config(state="disabled")