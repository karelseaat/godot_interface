# godot_interface

A Python tool to generate GDScript GUI code from JSON-defined node trees for Godot 4 projects.

## Features

- Generates complete GDScript classes (`.gd`) from hierarchical JSON node definitions
- Supports Godot 4 node types, properties, signals, and scripts
- Handles node paths, groups, and custom script properties (including `@export` variables)
- Outputs self-contained GDScript code with proper `class_name`, `extends`, and `_ready()` initialization
- Validates JSON schema against Godot 4 node property types
- Supports nested node trees with `children` arrays

## Getting Started

### Installation

```bash
git clone https://github.com/yourusername/godot_interface.git
cd godot_interface
pip install -r requirements.txt
```

### Usage

Create a JSON file describing your UI (e.g., `ui.json`):

```json
{
  "class_name": "MyHUD",
  "extends": "Control",
  "nodes": [
    {
      "name": "Panel",
      "type": "Panel",
      "properties": {
        "theme_overrides/font_sizes/font_size": 16
      },
      "children": [
        {
          "name": "Label",
          "type": "Label",
          "properties": {
            "text": "Hello World",
            "theme_overrides/font_colors/font_color": "#FFFFFFFF"
          }
        }
      ]
    }
  ]
}
```

Generate GDScript:

```bash
python main.py ui.json -o hud.gd
```

Output (`hud.gd`):

```gdscript
class_name MyHUD extends Control

func _ready():
	var Panel = Panel.new()
	Panel.theme_overrides.font_sizes.font_size = 16
	add_child(Panel)

	var Label = Label.new()
	Label.text = "Hello World"
	Label.theme_overrides.font_colors.font_color = Color(1, 1, 1, 1)
	Panel.add_child(Label)
```

Run with `-h` for additional options:

```bash
python main.py -h
```

## Requirements

- Python 3.9+
- `pydantic>=2.0` (for JSON schema validation)
- `click>=8.0` (CLI interface)

## More from Karelseaat

For more projects and experiments, visit my GitHub Pages site: [karelseaat.github.io](https://karelseaat.github.io/)

<!-- KEEP-EXPLORING-START -->
## Keep Exploring

If you made it to the bottom, jump straight into a few related repos:

- [Nodeventure](https://github.com/karelseaat/nodeventure)
- [Pygamepad](https://github.com/karelseaat/pygamepad)
- [Socialpad](https://github.com/karelseaat/socialpad)

- [Full project index](https://karelseaat.github.io/)
<!-- KEEP-EXPLORING-END -->
