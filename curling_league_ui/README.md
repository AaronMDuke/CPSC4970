# Curling League Manager

A PyQt5 app for managing curling leagues, teams, and their members.

## How to Run

```bash
python main_app.py
```

## Requirements

- Python 3
- PyQt5>=5.15

## Project Structure

- `curling_league_ui/` - top-level package containing all of the project solutions
- `gui/` - package containing the PyQt5 interface
- `main_app.py` - run this to start the app
- `gui/main_window.py` - main window which shows list of leagues
- `gui/league_editor.py` - window for editing teams in the league
- `gui/team_editor.py` - window for editing members on a team

## Features

### Main Window
- Load and save menu items using the File menu
- Add a new league by typing a league name and clicking Add League
- Delete a current league by selecting that league and clicking Delete League
- Edit a current league by selecting it and clicking Edit League

### League Editor
- Import and export teams from a CSV File
- Add a new team by typing a team name and clicking Add Team
- Delete a current team by selecting that team and clicking Delete Team
- Edit a current team by selecting the team and clicking Edit Team

### Team Editor
- Add a new member by filling in the fields and clicking Add Member
- Delete a current member by selecting them and clicking Delete Member
- Update a current member by selecting the member, editing their fields, and clicking Update Member

