import tkinter as tk
from tkinter import colorchooser
from utils import Utils

class TextFormatter:
    """
    Class for formatting text in the editor
    """
    @staticmethod
    def toggle_tag(text_widget, tag, event=None):
        """
        Apply the specified tag to the selected text in the text widget
        """
        current_tags = []
        try:
            current_tags = list(text_widget.tag_names("sel.first"))
        except tk.TclError:
            print("No text selected to toggle tag.")
            return "break"

        if len(current_tags) == 1 or tag not in current_tags[1].split(','):
            current_tags = [t for t in current_tags if t != "sel"] + [tag]
            combined_tag = ",".join(sorted(current_tags))
            TextFormatter.configure_combined_tag(text_widget, combined_tag)
            for tag_name in current_tags:
                text_widget.tag_remove(tag_name, "sel.first", "sel.last")
            text_widget.tag_add(combined_tag, "sel.first", "sel.last")

        else:
            current_tags = [t for t in current_tags if t != "sel"]
            tag_to_remove = current_tags[0]
            new_tags = tag_to_remove.split(',')
            new_tags.remove(tag)
            combined_new_tag = ",".join(sorted(new_tags)) if new_tags else None

            text_widget.tag_remove(tag_to_remove, "sel.first", "sel.last")

            if combined_new_tag:
                TextFormatter.configure_combined_tag(text_widget, combined_new_tag)
                text_widget.tag_add(combined_new_tag, "sel.first", "sel.last")

        return "break"
    
    @staticmethod
    def configure_combined_tag(text_widget, combined_tag):
        """
        Configures a combined tag
        e.g. bold + italic
        """
        components = combined_tag.split(",")
        font = ("Arial", 12)
        font_weight = "normal"
        font_slant = "roman"
        underline = False

        for component in components:
            match component:
                case "bold":
                    font_weight = "bold"
                case "italic":
                    font_slant = "italic"
                case "underline":
                    underline = True

            if component.startswith("color_"):
                color = component.split("_", 1)[1]
                text_widget.tag_configure(
                    combined_tag,
                    foreground=color
                )
            elif component.startswith("size_"):
                size = int(component.split("_")[1])
                text_widget.tag_configure(
                    combined_tag,
                    font=("Arial", size)
                )

        text_widget.tag_configure(
            combined_tag,
            font=(font[0], font[1], font_weight, font_slant),
            underline=underline
        )

    @staticmethod
    def change_text_color(editor):
        """
        Open a color picker dialog to change the text color
        """
        color = colorchooser.askcolor(title="Choisir la couleur du texte")[1]

        if color:
            try:
                tag_name = f"color_{color}"
                if tag_name not in editor.text_area.tag_names():
                    editor.text_area.tag_configure(tag_name, foreground=color)

                editor.text_area.tag_add(tag_name, "sel.first", "sel.last")
            except tk.TclError:
                Utils.set_status_bar(
                    editor.status_bar,
                    "Pas de texte sélectionné pour changer la couleur."
                )

    @staticmethod
    def change_text_size(editor, size):
        """
        Change the font size of the selected text
        """
        try:
            tag_name = f"size_{size}"
            if tag_name not in editor.text_area.tag_names():
                editor.text_area.tag_configure(tag_name, font=("Arial", size))

            editor.text_area.tag_add(tag_name, "sel.first", "sel.last")
        except tk.TclError:
            Utils.set_status_bar(
                editor.status_bar,
                "Pas de texte sélectionné pour changer la taille."
            )
