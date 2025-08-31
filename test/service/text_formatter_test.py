import tkinter as tk
from service.text_formatter import TextFormatter


class TestTextFormatter:
    """
    Tests methods in the TextFormatter class
    """
    def root(self):
        """
        Creates root widget for testing
        """
        return tk.Tk()

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

        TextFormatter.toggle_tag(text_area, "bold")
        assert "bold" in text_area.tag_names("1.0")
        assert len(text_area.tag_names("1.0")) == 2

        TextFormatter.toggle_tag(text_area, "size_18")
        assert "bold,size_18" in text_area.tag_names("1.0")
        assert len(text_area.tag_names("1.0")) == 2

        TextFormatter.toggle_tag(text_area, "italic")
        assert "bold,italic,size_18" in text_area.tag_names("1.0")
        assert len(text_area.tag_names("1.0")) == 2

        TextFormatter.toggle_tag(text_area, "italic")
        assert "bold,size_18" in text_area.tag_names("1.0")
        assert len(text_area.tag_names("1.0")) == 2

        TextFormatter.toggle_tag(text_area, "size_14")
        assert "bold,size_14" in text_area.tag_names("1.0")
        assert len(text_area.tag_names("1.0")) == 2

        root.destroy()

    def test_configure_combined_tag(self):
        """
        Tests the configure_combined_tag method
        """
        root = self.root()
        text_area = tk.Text(root)
        text_area.pack()

        TextFormatter.configure_combined_tag(text_area, "bold,italic")
        assert "bold,italic" in text_area.tag_names()

        TextFormatter.configure_combined_tag(text_area, "bold,underline")
        assert "bold,underline" in text_area.tag_names()

        TextFormatter.configure_combined_tag(text_area, "color_red")
        assert "color_red" in text_area.tag_names()

        TextFormatter.configure_combined_tag(text_area, "size_24")
        assert "size_24" in text_area.tag_names()

        root.destroy()
