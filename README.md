# Python-Tkinter-RPG
A complete 2D open-world RPG built using Python’s Tkinter library and TerraForge, a procedural generation library I created.

This project focuses on procedural generation, sandbox gameplay, and RPG systems.

The project also serves as the foundation for an evolving tutorial series where I break down the systems used to create the game step-by-step.

***
# Current Features

## Procedural World Generation

- Procedurally generated overworld maps powered by [TerraForge](https://github.com/BriannaLadson/TerraForge)
- Multi-noise terrain generation using elevation, moisture, and temperature maps
- Rule-based biome generation system
- Configurable island generation settings
- Large configurable world sizes
- Configurable local map sizes
- Wraparound overworld generation and rendering
- Procedural biome map rendering
- Biome-colored local maps

---

## Civilization & Settlement Generation

- Procedurally generated civilizations
- Race-based civilization generation
- Procedurally generated capitals
- Procedurally generated settlements
- Biome-restricted settlement placement
- Civilization culture systems
- Procedural civilization naming
- Procedural settlement naming
- JSON-driven naming systems
- Custom settlement map icons and colors

---

## Gameplay Systems

- Overworld exploration
- Local tile-based exploration
- Enterable locations
- Overworld-to-local map transitions
- 8-directional movement system
- Command-based input system
- Player location tracking across world and local maps
- Save system with persistent world data
- Save slot creation and overwrite handling

---

## Rendering & UI

- Canvas-based tile map renderer
- Player-centered camera system
- Zoomable map display
- Dynamic tile resizing
- Settlement/location markers displayed on the overworld
- Dedicated world generation screen
- Interactive procedural generation settings UI
- Character creation flow
- Start screen with new game/load game options
- Multi-screen Tkinter UI architecture
- Fullscreen/windowed Tkinter application framework

---

## Procedural Generation Controls

- Editable procedural generation settings directly from the UI
- Configurable seeds
- Adjustable octaves
- Adjustable persistence
- Adjustable lacunarity
- Adjustable falloff settings
- Adjustable zoom values
- Adjustable redistribution values
- Randomize buttons for generation settings

---

## Architecture & Data Systems

- JSON-driven data architecture
- External world settings configuration
- External race configuration
- External biome configuration
- External naming system configuration
- Prefix-based modular data loader system
- Modular project structure
- Expandable procedural generation pipeline
- Expandable RPG framework
- Utility systems for save management and procedural color handling

***

## Project Structure
### /project
Contains the latest evolving version of the RPG project.

This is the primary development directory where new systems and features are added.

### /old_tutorial

Contains the original tutorial code for the first version of the tutorial series.

These folders are preserved for compatibility with the original articles and tutorials.

***

## Tutorial Series
The tutorial series will be available in this repo’s Wiki.

This is a long-term evolving project. New systems and tutorials will continue to be added over time.

***

## Installation
### Clone the Repository
```
git clone https://github.com/YOUR_USERNAME/Python-Tkinter-RPG.git
```

### Install Dependencies
Navigate to the ```project``` directory and install the required packages:
```
pip install -r requirements.txt
```

Or manually install TerraForge:
```
pip install --upgrade terraforge-core
```

***

## Running the Project
From inside the ```project``` directory:
```
python main.py
```

***

## Dependencies
Current dependencies include:
* terraforge-core
* numpy
* pillow
* noise

***

## About TerraForge
TerraForge is a procedural generation library I created for building overworld maps, biome systems, and other procedural game content.

You can find it [here](https://github.com/BriannaLadson/TerraForge).

***

## License
This project is licensed under the MIT License.
