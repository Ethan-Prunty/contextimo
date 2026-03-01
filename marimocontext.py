from context_menu import menus
from context_menu.menus import ContextMenu

#.py-specific commands
edit_with_marimo = menus.FastCommand("Edit with marimo", type=".py", command="marimo edit ?", command_vars=["FILENAME"])
sandboxed_edit_with_marimo = menus.FastCommand("Edit in a sandbox", type=".py", command="marimo edit ? --sandbox", command_vars=["FILENAME"])
run_with_marimo = menus.FastCommand("Run with marimo", type=".py", command="marimo run ?", command_vars=["FILENAME"])

#General commands
create_with_marimo = menus.ContextCommand("Create a new notebook", command="cmd /c marimo new")
marimo_home = menus.ContextCommand("Open the marimo hub",  command="cmd /c marimo edit")

general_menu = ContextMenu("Marimo", type="DIRECTORY_BACKGROUND")
general_menu.add_items([create_with_marimo, marimo_home])
general_menu.compile()


