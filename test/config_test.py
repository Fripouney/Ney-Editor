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

    def test_config_tags(self):
        """
        Tests the config_tags method
        """

        root = self.root()
        text_area = tk.Text(root)
        text_area.pack()

        Config.config_tags(text_area)

        assert "bold" in text_area.tag_names()
        assert "italic" in text_area.tag_names()
        assert "underline" in text_area.tag_names()

        root.destroy()

    def test_toggle_tag(self):
        """
        Tests the toggle_tag method
        """

        root = self.root()
        text_area = tk.Text(root)
        text_area.pack()

        text_area.tag_remove("sel", "1.0", tk.END)
        text_area.insert("1.0", "whatever")
        text_area.tag_add("sel", "1.0", "1.7")

        Config.toggle_tag(text_area, "bold")
        assert "bold" in text_area.tag_names("1.0")

        Config.toggle_tag(text_area, "bold")
        assert "bold" not in text_area.tag_names("1.0")

        root.destroy()
