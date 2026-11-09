# The Last Engineer on Mars

## Project Description

*The Last Engineer on Mars* is a text-based science-fiction survival adventure developed in Python for MS539. The story takes place at Ares Colony on Mars, where a critical systems failure leaves the player—the colony's chief systems engineer—responsible for restoring essential equipment and keeping the colony operational.

The game is being developed incrementally throughout the course. This repository currently contains the first playable prototype, not the completed ten-scenario game.

## Development Track

**[Core Developer Track]**

## Game Setting and Objective

- **Setting:** Ares Colony, Mars — Sol 247
- **Player role:** Chief systems engineer
- **Primary objective:** Restore power, oxygen generation, and communications; investigate the failures; and keep the colony alive long enough to contact Earth.
- **Planned win condition:** Complete the adventure with a sufficient mission score and viable colony systems.
- **Planned lose condition:** Reach a failing mission outcome due to poor decisions, depleted resources, or loss of health.

The win and lose conditions describe the intended full game; they are **not yet enforced in this prototype**.

## Current Prototype Features (Assignment 1)

- Interactive story introduction and prompts to advance the text
- Player name input, reused in the narrative
- Three difficulty choices: Easy, Medium, and Hard
- Starting values for player health, colony oxygen, and mission score based on difficulty
- Scenario 1: **Darkness in the Control Room**, featuring three engineering decisions
- Distinct narrative outcomes for choices A, B, and C
- Calculations that change health, oxygen, and score according to the chosen action
- Updated statistics displayed after the scenario
- Python functions for difficulty setup, statistics updates, and statistics display

### Starting Statistics

| Difficulty | Health | Colony Oxygen | Score |
| --- | ---: | ---: | ---: |
| Easy | 100% | 100% | 10 |
| Medium | 100% | 75% | 0 |
| Hard | 80% | 50% | 0 |

### Scenario 1 Decision Effects

| Choice | Health change | Oxygen change | Score change |
| --- | ---: | ---: | ---: |
| A — Inspect the electrical panel | 0 | -5 | +10 |
| B — Activate emergency generators | +5 | -10 | +5 |
| C — Restart the reactor immediately | -15 | -20 | -5 |

These effects describe the current Python prototype.

## How to Run

1. Install Python 3 and Visual Studio Code.
2. Open the project folder in Visual Studio Code.
3. Open the integrated terminal.
4. Run:

   ```bash
   python main.py
   ```

5. Follow the on-screen prompts, enter your name, select a difficulty, and make a decision in Scenario 1.

If your system uses `py` rather than `python` to launch Python, use `py main.py` instead.

No third-party Python packages are required for the current prototype.

## Planned Development

Future course milestones will expand the prototype into a ten-scenario survival adventure with additional system failures, engineering choices, and a larger mystery surrounding the colony's automated controls. Planned work includes persistent player statistics across scenarios, resource management, additional scenarios, input validation, win/lose outcomes, and whatever additional architecture or testing is required by later assignments.

## Course Project

MS539 — Semester-long Adventure / Survival Game Project  
Assignment 1: Initial Functional Prototype

**Programming:** Student-authored Python code.  
**Story and documentation:** Developed with permitted AI assistance.
