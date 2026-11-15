controlRoom = {
        "name": "Main Control Room",
        "description": "The colony's central command center. Emergency lights illuminate rows of monitoring equipment. \n"
        "The main computer displays warnings about the reactor shutdown and rapidly declining oxygen reserves.",
        "exit": "Engineering Bay",
        "event": "The central computer reports a damaged electrical distribution relay requiring replacement."
}
EngineeringBay = {
        "name": "Engineering Bay",
        "description": "The Engineering Bay is the colony's primary maintenance and repair facility. "
        "Workbenches line the walls, surrounded by diagnostic equipment, electrical tools, and partially disassembled machinery. "
        "Emergency lighting reveals a damaged electrical distribution panel. Scorch marks surround a failed power relay, and the smell of burned insulation hangs in the air. "
        "A nearby diagnostic terminal indicates that the damaged relay must be replaced before the colony's main electrical distribution system can be safely restored.",
        "exit": ["Main Control Room", "Central Corridor"],
        "item": "Engineering Toolkit — Used to inspect and repair damaged electrical equipment.",
        "hazard": "Exposed electrical connections near the damaged distribution panel present a risk of injury.",
        "event": "You discover that a compatible replacement relay is available in the colony's Storage Room.",
}
centralCorridor = {
        "name": "Central Corridor",
        "description": "The Central Corridor connects the colony's primary operational facilities. Emergency lights flicker along the narrow passageway, casting long shadows across the metal floor. "
        "The ventilation system has stopped, leaving the air unnaturally still. Electrical conduits and oxygen supply pipes run along the walls, providing essential connections between the colony's critical systems. "
        "An emergency monitoring panel displays warnings about fluctuating electrical power and declining oxygen reserves. "
        "Emergency lighting illuminates the path, while warning signs indicate a possible oxygen leak.",
        "exit": ["Engineering Bay", "Life Support", "Storage Room"],
        "item": "Emergency Flashlight — A portable lighting device that allows the engineer to navigate areas where emergency lighting has failed.",
        "hazard": "Damaged electrical wiring occasionally produces sparks near the corridor's maintenance access panels.",
        "event": "A random electrical discharge may injure the engineer while traveling through the corridor, reducing their health by 10%."
        }
lifeSupport = {
        "name": "Life Support",
        "description": "The Life Support chamber houses the colony's oxygen generation, atmospheric filtration, and environmental monitoring systems. Normally filled with the steady hum of machinery, the room is now eerily quiet. "
        "Red warning lights illuminate the oxygen generation equipment. A large monitoring screen displays declining oxygen reserves and an urgent filtration system failure warning. "
        "A diagnostic panel identifies a severely clogged oxygen filter. Without a replacement, the system cannot safely resume normal operation. ",
        "exit": ["Central Corridor"],
        "item": "Replacement Oxygen Filter — A critical component required to restore the colony's oxygen generation system. A replacement can be found in the Storage Room.",
        "hazard": "Reduced oxygen concentration makes prolonged work in the chamber dangerous. Failure to restore adequate oxygen levels may affect the engineer's health.",
        "event": "If the engineer possesses the replacement oxygen filter, they can install it and restore oxygen generation, increasing the colony's oxygen reserves by 25%."
        }
storageRoom = {
        "name": "Storage Room",
        "description": "The Storage Room contains the colony's emergency supplies, replacement equipment, and maintenance materials. Metal shelving units line the walls, holding containers of electronic components, mechanical tools, medical supplies, and life-support equipment. "
        "Emergency lights flicker overhead, revealing several storage containers scattered across the floor. The recent electrical failures appear to have disrupted the automated inventory system. "
        "A wall-mounted inventory terminal operates on emergency power. Its display identifies several replacement components necessary to restore the colony's damaged systems.",
        "exit": ["Central Corridor"],
        "items": [
                "Replacement Power Relay: Required to repair the damaged electrical distribution panel in the Engineering Bay.\n\n",
                "Replacement Oxygen Filter: Required to restore oxygen generation in Life Support.\n\n",
                "Emergency Medical Kit: Contains medical supplies capable of restoring 20 percent of the engineer's health.",
        ],
        "hazard": "Unstable storage shelves and scattered equipment create a risk of injury while searching for supplies.",
        "event": "The engineer discovers three useful items. Each can be collected and added to the player's inventory. The power relay and oxygen filter are required for their respective repairs, while the medical kit can restore lost health."
        }

rooms = {
        "Main Control Room": controlRoom,
        "Engineering Bay": EngineeringBay,
        "Central Corridor": centralCorridor,
        "Life Support": lifeSupport,
        "Storage Room": storageRoom,
}