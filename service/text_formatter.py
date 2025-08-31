import tkinter as tk
from tkinter import colorchooser
from utils import Utils

class TextFormatter:
    """
    Class for formatting text in the editor
    """
    @staticmethod
    def toggle_tag(text_widget: tk.Text, tag: str, index_start=None, event=None):
        """
        Apply the specified tag to the selected text in the text widget
        """
        index_end = "sel.last"
        if index_start is None:
            index_start = "sel.first"
        else:
            index_end = tk.END

        current_tags = []
        try:
            current_tags = list(text_widget.tag_names(index_start))
        except tk.TclError:
            print("No text selected to toggle tag.")
            return "break"

        if len(current_tags) <= 1 or tag not in current_tags[1].split(','):
            current_tags = [t for t in current_tags if t != "sel"] + [tag]
            combined_tag = ",".join(sorted(current_tags))
            TextFormatter.configure_combined_tag(text_widget, combined_tag)
            for tag_name in current_tags:
                text_widget.tag_remove(tag_name, index_start, index_end)
            text_widget.tag_add(combined_tag, index_start, index_end)

        else:
            current_tags = [t for t in current_tags if t != "sel"]
            tag_to_remove = current_tags[0]
            new_tags = tag_to_remove.split(',')
            new_tags.remove(tag)
            combined_new_tag = ",".join(sorted(new_tags)) if new_tags else None

            text_widget.tag_remove(tag_to_remove, index_start, index_end)

            if combined_new_tag:
                TextFormatter.configure_combined_tag(text_widget, combined_new_tag)
                text_widget.tag_add(combined_new_tag, index_start, index_end)

        return "break"
    
    @staticmethod
    def configure_combined_tag(text_widget: tk.Text, combined_tag: str):
        """
        Configures a combined tag
        e.g. bold + italic
        """
        components = combined_tag.split(",")
        font_name = "Arial"
        font_weight = "normal"
        font_slant = "roman"
        underline = False
        color = "black"
        font_size = 12

        for component in components:
            match component:
                case "bold":
                    font_weight = "bold"
                case "italic":
                    font_slant = "italic"
                case "underline":
                    underline = True

            if component.startswith("color_"):
                color = component.split("_")[1]
                
            elif component.startswith("size_"):
                font_size = int(component.split("_")[1])

        text_widget.tag_configure(
            combined_tag,
            font=(font_name, font_size, font_weight, font_slant),
            underline=underline,
            foreground=color
        )

    @staticmethod
    def change_text_color(editor):
        """
        Open a color picker dialog to change the text color
        """
        color = colorchooser.askcolor(title="Choisir la couleur du texte")[1]

        if color:
            TextFormatter.toggle_tag(editor.text_area, f"color_{color}")

    # @staticmethod
    # def change_text_size(editor, size):
    #     """
    #     Change the font size of the selected text
    #     """
    #     try:
    #         tag_name = f"size_{size}"
    #         if tag_name not in editor.text_area.tag_names():
    #             editor.text_area.tag_configure(tag_name, font=("Arial", size))

    #         editor.text_area.tag_add(tag_name, "sel.first", "sel.last")
    #     except tk.TclError:
    #         Utils.set_status_bar(
    #             editor.status_bar,
    #             "Pas de texte sélectionné pour changer la taille."
    #         )
