# Sam Scout Summary
Sam Scout is a Discord bot that returns players from FIFA 22 based on user entered search parameters. Can be used by FIFA Career Mode players who are looking for new signings that meet their criteria.

How to use:
Sam Scout can be used through a series of filter commands in which the user can search for the player of his/her career mode dreams. As of now, the filter commands are 'name', 'nationality', 'position', 'overall', 'potential', 'age', 'club', 'parent_club', 'foot', 'transfer_value', and 'wage'.

Every command starts with a dollar sign ($). After the command, a space must be entered, and then the desired value. For example, if the user wants to see a list of French players, then the command would be the following: $nationality France

A space must separate multiple commands from each other. For example, if the user wants to see a list of French strikers, then the command would be the following: $nationality France $position ST

Information about options for each command:
position: GK, LB, CB, RCB, LCB, RB, CDM, LM, CM, RM, LAM, RAM, CAM, ST, RW, LW
foot: Right, Left
transfer_value: enter >val to see all players with a transfer value above val; <val to see all players with a transfer value below val; val1-val2 to see all players with a transfer value between val1 and val2 inclusive; val for a player whose transfer value is exactly val
wage: same syntax as transfer_value

Press enter after the entire command to see the information about the players who fit the search criteria.

# Upcoming Features:
Adding time remaining on contract as a search filter

# Installation
Use the package manager pip to install the required dependencies

Windows:
```
pip install -r requirements.txt 
```

macOS/Linux:
```
pip3 install -r requirements.txt
```

# Usage
Windows:
```
python main.py
```

macOS/Linux:
```
python3 main.py
```
