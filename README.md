# The Last Engineer on Mars

**A Python text-based science-fiction survival adventure**  
**Course:** MS539 — Programming Concepts  
**Development Track:** Core Developer Track

## Project Overview

*The Last Engineer on Mars* is a command-line adventure set at Ares Colony on Mars. On Sol 247, at 03:17 colony time, a critical systems failure shuts down main power, oxygen generation, and communications. The colony's AI is unresponsive, and backup battery power is at just 18%.

The player takes the role of the colony's chief engineer, who is alone while the other six colonists are away on a geological expedition. The objective is to investigate the failures, manage limited resources, repair essential equipment, and ultimately restore communications and the colony's systems.

The complete story is planned as **10 scenarios** with multiple possible endings. The current program implements the introduction, difficulty selection, and **Scenario 1: Darkness in the Control Room**, followed by an initial room-navigation interaction.

## Current Implemented Features

- Personalized story introduction using the player's name.
- Three selectable difficulty levels with different initial health, oxygen, and score values.
- Four displayed statistics: **health, colony oxygen, mission score, and backup battery power**.
- Function-based organization for the title, introduction, instructions, difficulty selection, statistics, and first scenario.
- Validated difficulty and Scenario 1 choices using `while` loops, with repeat prompts for invalid selections.
- Three Scenario 1 decisions, each with a distinct story outcome and battery-power adjustment.
- Numerical updates to health, oxygen, and score through the `update_stats()` function.
- Five described colony locations held in a **separate `rooms.py` module** and accessed from `main.py` through an import.
- A room lookup dictionary, available-exit display, destination validation, and one move to a connected location.
- Console formatting with headings, separators, and Enter-to-continue prompts.

## Project Files

```text
The-Last-Engineer-on-Mars/
├── main.py       # Main program: story, user input, functions, statistics, Scenario 1, movement
├── rooms.py      # Five location dictionaries and the combined rooms lookup dictionary
└── README.md     # Project description, usage, features, and development status
```

`main.py` uses `from rooms import rooms` to access the location lookup dictionary directly. Keeping the room definitions in `rooms.py` reduces the size of the main program and separates location data from the game's execution flow.

## Starting Statistics

The selected difficulty establishes the player's initial statistics. Backup battery power starts at **18%** for all three difficulty levels.

| Difficulty | Selection | Health | Colony Oxygen | Score | Backup Battery |
|---|---|---:|---:|---:|---:|
| Easy | A | 100% | 100% | 10 | 18% |
| Medium | B | 100% | 75% | 0 | 18% |
| Hard | C | 80% | 50% | 0 | 18% |

The program displays these values after difficulty selection and again after the first scenario's result.

## Scenario 1 — Darkness in the Control Room

The engineer enters the Main Control Room to investigate the colony's power failure. The player chooses one of three responses:

| Choice | Action | Story Assessment | Battery Change | Battery After Choice |
|---|---|---|---:|---:|
| A | Inspect the electrical distribution panel | Excellent | +70 percentage points | 88% |
| B | Activate portable emergency generators | Acceptable | +40 percentage points | 58% |
| C | Attempt an immediate main-reactor restart | Poor | −10 percentage points | 8% |

The program also updates health, oxygen, and score using `update_stats()`. **In the current implementation, that function selects those three adjustments using the difficulty setting**, while the battery adjustment and displayed decision outcome use the Scenario 1 choice. The existing scoring logic is preserved as implemented in the submitted code.

### Statistics Update Rules in the Current Program

| Selected Difficulty | Health Change | Oxygen Change | Score Change |
|---|---:|---:|---:|
| A — Easy | 0 | −5 | +10 |
| B — Medium | +5 | −10 | +5 |
| C — Hard | −15 | −20 | −5 |

## Colony Locations

Location definitions are stored in `rooms.py`:

| Location | Purpose / Description | Available Exits |
|---|---|---|
| Main Control Room | Colony command center, reactor monitoring, and electrical diagnostics | Engineering Bay |
| Engineering Bay | Maintenance equipment, engineering toolkit, and damaged electrical distribution panel | Main Control Room; Central Corridor |
| Central Corridor | Passageway connecting the operational facilities, with damaged wiring | Engineering Bay; Life Support; Storage Room |
| Life Support | Oxygen generation, environmental controls, and filtration-system failure | Central Corridor |
| Storage Room | Emergency supplies, replacement power relay, oxygen filter, and medical kit | Central Corridor |

The room dictionaries contain descriptive text and information about items, hazards, and events. These data entries establish the foundation for later gameplay; most corresponding interactions are not yet active.

## Controls

| Input | Purpose |
|---|---|
| **Enter** | Advance through story screens |
| **Player name** | Identify the engineer in the story |
| **A / B / C** | Choose difficulty |
| **A / B / C** | Choose an action in Scenario 1 |
| **Destination name** | Move to an available adjacent room after Scenario 1 |

Difficulty and Scenario 1 prompts accept lowercase letters and surrounding spaces because input is normalized using `.strip().upper()`. Invalid selections are rejected and prompted again.

For movement, type the destination's name as shown (for example, `Engineering Bay`). The current program validates it against the available exit from the Main Control Room.

## How to Run

1. Install **Python 3**.
2. Keep **`main.py` and `rooms.py` in the same folder**.
3. Open that folder in Visual Studio Code or a terminal.
4. Run:

   ```bash
   python main.py
   ```

5. Follow the on-screen story, Enter prompts, difficulty selection, and Scenario 1 decision.

The program uses Python's built-in functionality; **no third-party packages are required**.

## Functions in `main.py`

| Function | Role |
|---|---|
| `display_title()` | Prints the game's title |
| `display_introduction(userName)` | Presents the opening story, requests the player's name, and returns it |
| `gameInstructions()` | Displays the game directions and scoring explanation |
| `difficulty_stats(...)` | Assigns starting statistics for the selected difficulty |
| `choseDifficulty(...)` | Validates the difficulty selection and displays starting statistics |
| `display_statistics(...)` | Displays health, oxygen, score, and battery power |
| `update_stats(...)` | Applies the current health, oxygen, and score adjustments |
| `Level1(...)` | Presents Scenario 1, validates a decision, applies battery changes, and shows updated statistics |

The program uses function arguments and return values to carry statistics from one section to the next.

## Current Scope and Known Limitations

This is a **work-in-progress course project**, not the completed 10-scenario adventure.

- Only Scenario 1 is currently playable.
- The current navigation section allows **one move** and then ends the simulation; it does not yet provide a continuous exploration loop.
- Room descriptions are stored in `rooms.py`, but the movement section currently displays the available exit and the arrival message rather than automatically displaying the destination's full description.
- Items are described in the room data, but inventory collection and item use are not implemented.
- Hazards and random events are described but are not yet executable gameplay mechanics.
- Equipment repair interactions, automatic win/lose conditions, and final endings are planned rather than implemented.
- The current `update_stats()` implementation bases health, oxygen, and score changes on difficulty; battery-power changes follow the selected Scenario 1 action.

## Planned Development

Future work may expand room navigation into a continuous exploration loop, introduce inventory and usable repair components, activate hazards and random events, add further scenarios, and implement victory/failure conditions. The full story is intended to explore the cause of Ares Colony's failures and the behavior of its automated systems.

## Course and Authorship

**Course:** MS539 — Programming Concepts  
**Project:** Adventure / Survival Game  
**Track:** Core Developer Track  
**Language:** Python 3  
**Repository:** https://github.com/GlennTruett/The-Last-Engineer-on-Mars

**Python program:** Written by the student.  
**Storyline and README documentation:** Developed with permitted AI assistance.
