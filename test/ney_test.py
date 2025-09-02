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
