
from PyQt5.QtWidgets import (QMainWindow, QAction, QWidget, QVBoxLayout, QLabel, QListWidget,
                             QLineEdit, QHBoxLayout, QPushButton, QFileDialog, QMessageBox)

from module5.league_database import LeagueDatabase
from module5.league import League
from gui.league_editor import LeagueEditor


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Curling League Manager")
        self.setMinimumSize(400, 350)

        self._league_editor = None

        self._setup_menu()
        self._setup_ui()
        self._refresh_league_list()


    def _setup_menu(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")

        load_action = QAction("Load Database...", self)
        load_action.triggered.connect(self._load_database)
        file_menu.addAction(load_action)


    def _setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        main_layout.addWidget(QLabel("Leagues:"))

        self._league_list = QListWidget()
        main_layout.addWidget(self._league_list)

        main_layout.addWidget(QLabel("New league name:"))
        self._league_name_input = QLineEdit()
        main_layout.addWidget(self._league_name_input)

        button_layout = QHBoxLayout()
        main_layout.addLayout(button_layout)

        add_button = QPushButton("Add League")
        add_button.clicked.connect(self._add_league)
        button_layout.addWidget(add_button)

        edit_button = QPushButton("Edit League")
        edit_button.clicked.connect(self._edit_league)
        button_layout.addWidget(edit_button)

        delete_button = QPushButton("Delete League")
        delete_button.clicked.connect(self._delete_league)
        button_layout.addWidget(delete_button)


    def _refresh_league_list(self):
        self._league_list.clear()
        for league in LeagueDatabase.instance().leagues:
            self._league_list.addItem(league.name)


    def _get_current_league(self):
        row = self._league_list.currentRow()
        if row == -1:
            return None
        return LeagueDatabase.instance().leagues[row]


    def _load_database(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Load Database", "",
                                                   "Database Files (*.db);;All Files (*)")
        if file_path == "":
            return

        if self._league_editor is not None:
            self._league_editor.close()
            self._league_editor = None

        LeagueDatabase.load(file_path)
        self._refresh_league_list()


    def _save_database(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Database", "",
                                                   "Database Files (*.db);;All Files (*)")
        if file_path == "":
            return
        LeagueDatabase.instance().save(file_path)


    def _add_league(self):
        name = self._league_name_input.text().strip()
        if name == "":
            QMessageBox.warning(self, "Error", "Please enter a league name.")
            return

        new_league = League(LeagueDatabase.instance().next_oid(), name)
        LeagueDatabase.instance().add_league(new_league)
        self._league_name_input.clear()
        self._refresh_league_list()


    def _delete_league(self):
        league = self._get_current_league()
        if league is None:
            QMessageBox.information(self, "No selection", "Please select a league.")
            return

        user_response = QMessageBox.question(self, "Confirm delete",
                                             f"Are you sure you want to delete {league_name}?",
                                             QMessageBox.Yes | QMessageBox.No)
        if user_response == QMessageBox.Yes:
            LeagueDatabase.instance().remove_league(league)
            self._refresh_league_list()


    def _edit_league(self):
        league = self._get_current_league()
        if league is None:
            QMessageBox.information(self, "No selection", "Please select a league.")
            return

        if self._league_editor is not None and self._league_editor.isVisible():
            self._league_editor.load_league(league)
        else:
            self._league_editor = LeagueEditor(league, self)
            self._league_editor.show()













