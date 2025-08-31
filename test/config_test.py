import tkinter as tk
from config import Config
from ney import NeyEditor

class TestConfig:
    """
    This tests all of the methods in the Config class
    """
    def root(self):
        """
        Sets up the root Tkinter window for testing
        """
        return tk.Tk()

    def test_add_editor_bindings(self):
        """
        Tests the add_editor_bindings method
        """

        editor = NeyEditor()
        Config.add_editor_bindings(editor)

        assert "<Control-Key-n>" in editor.root.bind()
        assert "<Control-Key-s>" in editor.root.bind()
        assert "<Control-Key-o>" in editor.root.bind()
        assert "<Control-Key-S>" in editor.root.bind()

    def test_add_text_area_bindings(self):
        """
        Tests the add_text_area_bindings method
        """

        root = self.root()
        text_area = tk.Text(root)
        text_area.pack()

        Config.add_text_area_bindings(text_area)

        assert "<Control-Key-b>" in text_area.bind()
        assert "<Control-Key-i>" in text_area.bind()
        assert "<Control-Key-u>" in text_area.bind()

        root.destroy()
