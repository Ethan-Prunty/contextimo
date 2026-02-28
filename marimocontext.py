from context_menu import menus

fc = menus.FastCommand("TEST COMMAND", type="FILES", command="cmd /c echo 'Hello world'")
marimo = menus.FastCommand("Edit with marimo", type=".py", command="cmd /c marimo edit", command_vars=["FILENAME"])
marimo.compile()