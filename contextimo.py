# for getting the absolute path to the marimo icon
import os.path
import sys

from context_menu import menus
from context_menu.menus import ContextMenu


# adds all of the commands
def add_commands():
    # commands which appear in the context menu for .py files
    python_menu = ContextMenu(
        "Marimo", type=".py", icon_path=os.path.abspath("marimo_icon.ico")
    )

    edit_with_marimo = menus.ContextCommand(
        "edit", command="marimo edit ?", command_vars=["FILENAME"]
    )
    sandboxed_edit_with_marimo = menus.ContextCommand(
        "edit in a sandbox",
        command="marimo edit ? --sandbox",
        command_vars=["FILENAME"],
    )
    run_with_marimo = menus.ContextCommand(
        "run", command="marimo run ?", command_vars=["FILENAME"]
    )

    python_menu.add_items(
        [edit_with_marimo, sandboxed_edit_with_marimo, run_with_marimo]
    )
    python_menu.compile()

    # commands which appear when in a folder or the desktop
    general_menu = ContextMenu(
        "Marimo",
        type="DIRECTORY_BACKGROUND",
        icon_path=os.path.abspath("marimo_icon.ico"),
    )

    create_with_marimo = menus.ContextCommand(
        "new notebook", command="cmd /c marimo new"
    )
    marimo_home = menus.ContextCommand("marimo hub", command="cmd /c marimo edit")

    general_menu.add_items([create_with_marimo, marimo_home])
    general_menu.compile()


# removes all the created menus
def remove_commands():
    menus.removeMenu("Marimo", type=".py")
    menus.removeMenu("Marimo", type="DIRECTORY_BACKGROUND")


if sys.argv[1] == "add":
    add_commands()
elif sys.argv[1] == "remove":
    remove_commands()
else:
    pass
