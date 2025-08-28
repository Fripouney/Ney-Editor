import tkinter as tk

from utils import Utils

class TestUtils:
    """
    Tests all util methods
    """

    def root(self):
        """
        Sets up the root Tkinter window for testing
        """
        return tk.Tk()

    def test_set_status_bar(self):
        """
        Tests the set_status_bar method
        """

        root = self.root()
        status_bar = tk.Text(root, height=1)
        status_bar.pack(fill=tk.X, side=tk.BOTTOM)

        Utils.set_status_bar(status_bar, "whatever")

        assert status_bar.get("1.0", tk.END).strip() == "whatever"
        assert status_bar.cget("state") == "disabled"

        root.destroy()