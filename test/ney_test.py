import tkinter as tk
from ney import NeyEditor

class TestNey:
    """
    This tests all of the methods in the Ney class
    """

    def editor(self):
        """
        Sets up the NeyEditor instance for testing
        """
        return NeyEditor()

    def test_add_editor_bindings(self):
        """
        Tests the add_editor_bindings method
        """

        editor = self.editor()
        editor.add_editor_bindings()

        assert "<Control-Key-n>" in editor.root.bind()
        assert "<Control-Key-s>" in editor.root.bind()
        assert "<Control-Key-o>" in editor.root.bind()
        assert "<Control-Key-S>" in editor.root.bind()

    def test_build_root(self):
        """
        Tests the build_root method
        """

        editor = self.editor()
        editor.build_root()
        editor.root.update_idletasks()
        assert editor.root.title() == "Ney Editor - Sans titre"
        assert editor.root.geometry().split("+")[0] == "800x600"

    def test_build_menu_bar(self):
        """
        Tests the build_menu_bar method
        """

        editor = self.editor()
        editor.build_menu_bar()
        menu_name = editor.root.cget("menu")
        assert menu_name is not None

        menu = editor.root.nametowidget(menu_name)
        assert isinstance(menu, tk.Menu)

    def test_build_toolbar(self):
        """
        Tests the build_toolbar method
        """

        editor = self.editor()
        editor.build_toolbar()
        # Find the toolbar frame by looking for a tk.Frame with the expected buttons
        toolbar = None
        for child in editor.root.winfo_children():
            if isinstance(child, tk.Frame):
                children = child.winfo_children()
                if (len(children) >= 3 and
                    children[0].cget("text") == "B" and
                    children[1].cget("text") == "I" and
                    children[2].cget("text") == "U"):
                    toolbar = child
                    break
        assert toolbar is not None, "Toolbar frame not found"
        assert isinstance(toolbar, tk.Frame)
        assert toolbar.winfo_children()[0].cget("text") == "B"
        assert toolbar.winfo_children()[1].cget("text") == "I"
        assert toolbar.winfo_children()[2].cget("text") == "U"

    def test_file_menu(self):
        """
        Tests the file_menu method
        """

        editor = self.editor()
        menu = editor.file_menu()
        assert isinstance(menu, tk.Menu)

        end_index = menu.index("end")
        labels = [
            menu.entrycget(i, "label") if menu.type(i) != "separator" else None
            for i in range(1, end_index + 1) if end_index is not None
        ] if end_index is not None else []
        expected_labels = [
            "Nouveau", "Ouvrir", None, "Enregistrer",
            "Enregistrer sous", None, "Quitter"
        ]
        assert labels == expected_labels
