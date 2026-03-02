from context_menu import menus
from context_menu.menus import ContextMenu

#.py-specific commands
python_menu = ContextMenu("Marimo", type=".py", icon_path="C:\\Users\\elp83s\\Desktop\\MarimoContext\\marimo_icon.ico")
edit_with_marimo = menus.ContextCommand("edit",  command="marimo edit ?", command_vars=["FILENAME"])
sandboxed_edit_with_marimo = menus.ContextCommand("edit in a sandbox", command="marimo edit ? --sandbox", command_vars=["FILENAME"])
run_with_marimo = menus.ContextCommand("run", command="marimo run ?", command_vars=["FILENAME"])

python_menu.add_items([edit_with_marimo, sandboxed_edit_with_marimo, run_with_marimo])
python_menu.compile()

#General commands
general_menu = ContextMenu("Marimo", type="DIRECTORY_BACKGROUND", icon_path="C:\\Users\\elp83s\\Desktop\\MarimoContext\\marimo_icon.ico")
create_with_marimo = menus.ContextCommand("new notebook", command="cmd /c marimo new")
marimo_home = menus.ContextCommand("marimo hub",  command="cmd /c marimo edit")

general_menu.add_items([create_with_marimo, marimo_home])
general_menu.compile()


