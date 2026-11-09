# The Last Engineer on Mars

## Project Description

*The Last Engineer on Mars* is a Python text-console science-fiction survival adventure developed for MS539.

On Sol 247 at Ares Colony, Mars, a critical systems failure leaves the chief systems engineer responsible for investigating the damage, protecting the colony's oxygen supply, and restoring essential systems.

This project is being developed over multiple course assignments.

## Development Track

**Core Developer Track**

## Game Objective

The player must investigate the colony's failures, repair critical equipment, conserve resources, and ultimately restore communications with Earth.

The planned completed game will contain ten scenarios with multiple endings determined by player decisions and survival statistics.

## Current Features — Assignment 2.1

- Interactive introduction and player name input
- Three difficulty settings: Easy, Medium, and Hard
- Health, oxygen, and score statistics
- Scenario 1: Darkness in the Control Room
- Three decisions with different consequences and numerical calculations
- Input validation using `while` loops
- Five colony locations represented using Python dictionaries
- A master dictionary connecting the locations
- Display of current room descriptions and available exits
- One movement between connected rooms
- Validation of destination choices

## Starting Statistics

| Difficulty | Health | Oxygen | Score |
|---|---:|---:|---:|
| Easy | 100% | 100% | 10 |
| Medium | 100% | 75% | 0 |
| Hard | 80% | 50% | 0 |

## Colony Locations

1. **Main Control Room:** Colony monitoring and reactor diagnostics.
2. **Engineering Bay:** Electrical maintenance and equipment repairs.
3. **Central Corridor:** Connects the colony's operational facilities.
4. **Life Support:** Oxygen generation and environmental controls.
5. **Storage Room:** Emergency supplies, replacement components, and medical equipment.

Each location includes descriptive information, available exits, and associated items, hazards, or events.

## Game Controls

- **Enter:** Continue through story sections.
- **Player name:** Type your name and press Enter.
- **Difficulty selection:** Enter A, B, or C.
- **Scenario decisions:** Enter A, B, or C.
- **Movement:** Enter the name of an available destination exactly as displayed.
- **Invalid input:** The program displays an error message and requests another selection.

## Running the Program

1. Install Python 3.
2. Open the project folder in Visual Studio Code.
3. Open a terminal.
4. Execute the following command:

`python main.py`

5. Follow the displayed instructions.

No additional Python packages are required for the current version.

## Known Limitations

- Navigation currently allows one movement rather than continuous exploration.
- Items and hazards have been defined in the location dictionaries, but an operational inventory system has not yet been implemented.
- Random events are not yet functioning.
- Automatic win and lose conditions are planned for future development.
- Only the first of the ten planned scenarios is currently playable.

## Planned Development

Future development will expand the existing project with continuous navigation, inventory management, collectible items, equipment repairs, random hazards, additional survival mechanics, and working victory and failure conditions.

The completed adventure is planned to include all ten scenarios and the mystery surrounding the colony's automated systems.

## Course Information

**Course:** MS539 — Programming Concepts

**Project:** Adventure / Survival Game

**Current Milestone:** Assignment 2.1

**Python Code:** Written by the student.

**Storyline and README Documentation:** Developed with permitted AI assistance.