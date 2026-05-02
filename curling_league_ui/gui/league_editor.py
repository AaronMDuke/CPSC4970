from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget,
                             QLineEdit, QLabel, QMessageBox, QFileDialog)
from PyQt5.QtCore import Qt
from module5.league_database import LeagueDatabase
from module5.team import Team
from gui.team_editor import TeamEditor


class LeagueEditor(QWidget):

    def __init__(self, league, parent=None):
        super().__init__(parent)
        self.setWindowFlag(Qt.Window)
        self.setMinimumSize(500, 480)

        self._league = league
        self._team_editor = None
        self._setup_ui()
        self._refresh_team_list()


    def _setup_ui(self):
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        self._league_label = QLabel()
        self._league_label.setStyleSheet("font-weight: bold;")
        main_layout.addWidget(self._league_label)

        import_export_layout = QHBoxLayout()
        main_layout.addLayout(import_export_layout)

        import_button = QPushButton("Import teams")
        import_button.clicked.connect(self._import_teams)
        import_export_layout.addWidget(import_button)

        export_button = QPushButton("Export teams")
        export_button.clicked.connect(self._export_teams)
        import_export_layout.addWidget(export_button)

        main_layout.addWidget(QLabel("Teams:"))

        self._team_list = QListWidget()
        self._team_list.itemDoubleClicked.connect(lambda _: self._edit_team())
        main_layout.addWidget(self._team_list)

        main_layout.addWidget(QLabel("New team name:"))
        self._team_name_input = QLineEdit()
        main_layout.addWidget(self._team_name_input)

        button_layout = QHBoxLayout()
        main_layout.addLayout(button_layout)

        add_button = QPushButton("Add Team")
        add_button.clicked.connect(self._add_team)
        button_layout.addWidget(add_button)

        delete_button = QPushButton("Delete Team")
        delete_button.clicked.connect(self._delete_team)
        button_layout.addWidget(delete_button)

        edit_button = QPushButton("Edit Team")
        edit_button.clicked.connect(self._edit_team)
        button_layout.addWidget(edit_button)


    def _load_league(self, league):
        self._league = league

        if self._team_editor is not None:
            self._team_editor.close()
            self._team_editor = None

        self._refresh_team_list()



    def _refresh_team_list(self):
        self.setWindowTitle(f"Editing League: {self._league.name}")
        self._league_label.setText(f"League: {self._league.name}")
        self._team_list.clear()
        for team in self._league.teams:
            self._team_list.addItem(str(team))


    def _get_current_team(self):
        row = self._team_list.currentRow()
        if row == -1:
            return None
        return self._league.teams[row]


    def _import_teams(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Import Teams," "", "CSV Files (*.csv);;All Files (*.*)")
        if file_path == "":
            return
        LeagueDatabase.instance().import_league_teams(self._league, file_path)
        self._refresh_team_list()


    def _export_teams(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Export Teams", "", "CSV Files (*.csv);;All Files (*.*)")
        if file_path == "":
            return
        LeagueDatabase.instance().export_league_teams(self._league, file_path)


    def _add_team(self):
        team_name = self._team_name_input.text().strip()
        if team_name == "":
            QMessageBox.warning(self, "Error", "Please enter a name.")
            return

        try:
            new_team = Team(LeagueDatabase.instance().next_oid(), team_name)
            self._league.add_team(new_team)
            self._team_name_input.clear()
            self._refresh_team_list()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to add new team: {e}")



    def _delete_team(self):
        team = self._get_current_team()
        if team is None:
            QMessageBox.information(self, "No Team Selected", "Please select a team first.")
            return

        user_response = QMessageBox.question(self, "Confirm Delete",
                                             f"Are you sure you want to delete {team.name}?",
                                             QMessageBox.Yes | QMessageBox.No)
        if user_response == QMessageBox.Yes:
            try:
                self._league.remove_team(team)
                self._refresh_team_list()
            except Exception as e:
                QMessageBox.warning(self, "Cannot Delete", str(e))


    def _edit_team(self):
        team = self._get_current_team()
        if team is None:
            QMessageBox.information(self, "No Team Selected", "Please select a team first.")
            return

        if self._team_editor is not None and self._team_editor.isVisible():
            self._team_editor.load_team(team)
        else:
            self._team_editor = TeamEditor(team, self)
            self._team_editor.show()


