from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QListWidget, QLineEdit,
                             QHBoxLayout, QPushButton, QMessageBox)

from module5.league_database import LeagueDatabase
from module5.team_member import TeamMember
from module5.custom_exception import DuplicateEmail, DuplicateOid


class TeamEditor(QWidget):

    def __init__(self, team, parent=None):
        super().__init__(parent)
        self.setMinimumSize(420, 400)

        self._team = team
        self._setup_ui()
        self._refresh_member_list()


    def _setup_ui(self):
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        self._team_label = QLabel()
        self._team_label.setStyleSheet("font-weight: bold;")
        main_layout.addWidget(self._team_label)

        main_layout.addWidget(QLabel("Memebers (click to select):"))

        self._member_list = QListWidget()
        self._member_list.itemClicked.connect(self._load_member_into_fields)
        main_layout.addWidget(self._member_list)

        main_layout.addWidget(QLabel("Name:"))
        self._name_input = QLineEdit()
        main_layout.addWidget(self._name_input)

        main_layout.addWidget(QLabel("Email:"))
        self._email_input = QLineEdit()
        main_layout.addWidget(self._email_input)

        button_layout = QHBoxLayout()
        main_layout.addLayout(button_layout)

        add_button = QPushButton("Add Member")
        add_button.clicked.connect(self._add_member)
        button_layout.addWidget(add_button)

        update_button = QPushButton("Update Member")
        update_button.clicked.connect(self._update_member)
        button_layout.addWidget(update_button)

        delete_button = QPushButton("Delete Member")
        delete_button.clicked.connect(self._delete_member)
        button_layout.addWidget(delete_button)

        clear_button = QPushButton("Clear All Fields")
        clear_button.clicked.connect(self._clear_fields)
        main_layout.addWidget(clear_button)


    def load_team(self, team):
        self._team = team
        self._clear_fields()
        self._refresh_member_list()


    def _refresh_member_list(self):
        self.setWindowTitle(f"Editing team: {self._team.name}")
        self._team_label.setText(f"Team: {self._team.name}")
        self._member_list.clear()
        for member in self._team.members:
            self._member_list.addItem(f"{member.name} <{member.email}>")


    def _get_current_member(self):
        row = self._member_list.currentRow()
        if row == -1:
            return None
        return self._team.members[row]


    def _load_member_into_fields(self):
        member = self._get_current_member()
        if member is not None:
            self._name_input.setText(member.name)
            self._email_input.setText(member.email if member.email is not None else "")


    def _clear_fields(self):
        self._name_input.clear()
        self._email_input.clear()
        self._member_list.clearSelection()


    def _add_member(self):
        name = self._name_input.text().strip()
        email = self._email_input.text().strip()

        if name == "":
            QMessageBox.warning(self, "Error", "Enter a member name.")
            return

        if email == "":
            email = None

        try:
            new_member = TeamMember(LeagueDatabase.instance().next_oid(), name, email)
            self._team_add_member(new_member)
            self._clear_fields()
            self._refresh_member_list()
        except DuplicateEmail as e:
            QMessageBox.warning(self, "Duplicate Email", str(e))
        except DuplicateOid as e:
            QMessageBox.warning(self, "Duplicate OID", str(e))


    def _update_member(self):
        member = self._get_current_member()
        if member is None:
            QMessageBox.information(self, "No Selection", "Enter a member name first.")
            return

        name = self._name_input.text().strip()
        email = self._email_input.text().strip()

        if name == "":
            QMessageBox.warning(self, "Error", "Enter a member name.")
            return

        if email == "":
            email = None

        for other_member in self._team.members:
            if other_member is member:
                continue
            if other_member.email is not None and email is not None:
                if other_member.email.lower() == email.lower():
                    QMessageBox.warning(self, "Duplicate Email",
                                        f"Email {email} is already in use.")
                    return

        member.name = name
        member.email = email
        self._refresh_member_list()


    def _delete_member(self):
        member = self._get_current_member()
        if member is None:
            QMessageBox.information(self, "No Selection", "Select a member first.")
            return

        user_response = QMessageBox.question(self, "Confirm delete",
                                             f"Are you sure you want to delete {member.name}?",
                                             QMessageBox.Yes | QMessageBox.No,)
        if user_response == QMessageBox.Yes:
            self._team_remove_member(member)
            self._clear_fields()
            self._refresh_member_list()