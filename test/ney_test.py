import tkinter as tk
from ney import NeyEditor

class TestNey:
    """
    This tests all of the methods in the Ney class
    """

    editor = NeyEditor()

    def test_add_editor_bindings(self):
        """
        Tests the add_editor_bindings method
        """

        self.editor.add_editor_bindings()

        assert "<Control-Key-n>" in self.editor.root.bind()
        assert "<Control-Key-s>" in self.editor.root.bind()
        assert "<Control-Key-o>" in self.editor.root.bind()
        assert "<Control-Shift-Key-s>" in self.editor.root.bind()

    def test_build_root(self):
        """
        Tests the build_root method
        """
        self.editor.build_root()
        self.editor.root.update_idletasks()
        assert self.editor.root.title() == "Ney Editor"
        assert self.editor.root.geometry().split("+")[0] == "800x600"

    def test_build_menu_bar(self):
        """
        Tests the build_menu_bar method
        """
        self.editor.build_menu_bar()
        menu_name = self.editor.root.cget("menu")
        assert menu_name is not None

        menu = self.editor.root.nametowidget(menu_name)
        assert isinstance(menu, tk.Menu)

    def test_file_menu(self):
        """
        Tests the file_menu method
        """
        menu = self.editor.file_menu()
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
