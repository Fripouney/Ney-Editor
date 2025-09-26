import tkinter as tk
from service.menu_bar_builder import MenuBarBuilder
from ney import NeyEditor

class TestMenubarBuilder():
    def instance(self):
        """
        Creates root widget for testing
        """
        return MenuBarBuilder(NeyEditor())
    
    def test_build_file_menu(self):
        """
        Tests the build_file_menu method
        """

        builder = self.instance()
        menu = builder.build_file_menu()
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

    def test_build_insert_menu(self):
        """
        Tests the build_insert_menu method
        """

        builder = self.instance()
        menu = builder.build_insert_menu()
        assert isinstance(menu, tk.Menu)

        end_index = menu.index("end")
        labels = [
            menu.entrycget(i, "label") if menu.type(i) != "separator" else None
            for i in range(1, end_index + 1) if end_index is not None
        ] if end_index is not None else []
        expected_labels = [
            "Image..."
        ]
        assert labels == expected_labels

    def test_build_menu_bar(self):
        """
        Tests the build method
        """

        builder = self.instance()
        menu_bar = builder.build()
        assert isinstance(menu_bar, tk.Menu)

        end_index = menu_bar.index("end")
        labels = [
            menu_bar.entrycget(i, "label") if menu_bar.type(i) != "separator" else None
            for i in range(1, end_index + 1) if end_index is not None
        ] if end_index is not None else []
        expected_labels = [
            "Fichier", "Insertion"
        ]
        assert labels == expected_labels
