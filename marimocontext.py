from context_menu import menus
from context_menu.menus import ContextMenu

#.py-specific commands
python_menu = ContextMenu("Marimo", type=".py")
edit_with_marimo = menus.ContextCommand("Edit with marimo",  command="marimo edit ?", command_vars=["FILENAME"])
sandboxed_edit_with_marimo = menus.ContextCommand("Edit in a sandbox", command="marimo edit ? --sandbox", command_vars=["FILENAME"])
run_with_marimo = menus.ContextCommand("Run with marimo", command="marimo run ?", command_vars=["FILENAME"])

python_menu.add_items([edit_with_marimo, sandboxed_edit_with_marimo, run_with_marimo])
python_menu.compile()

#General commands
general_menu = ContextMenu("Marimo", type="DIRECTORY_BACKGROUND")
create_with_marimo = menus.ContextCommand("Create a new notebook", command="cmd /c marimo new")
marimo_home = menus.ContextCommand("Open the marimo hub",  command="cmd /c marimo edit")

general_menu.add_items([create_with_marimo, marimo_home])
general_menu.compile()


