import tkinter as tk
from config import Config

class TestConfig:
    """
    This tests all of the methods in the Config class
    """
    def root(self):
        return tk.Tk()

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

    def test_set_status_bar(self):
        """
        Tests the set_status_bar method
        """

        root = self.root()
        status_bar = tk.Text(root, height=1)
        status_bar.pack(fill=tk.X, side=tk.BOTTOM)

        Config.set_status_bar(status_bar, "whatever")

        assert status_bar.get("1.0", tk.END).strip() == "whatever"
        assert status_bar.cget("state") == "disabled"

        root.destroy()
