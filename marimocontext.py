from context_menu import menus

fc = menus.FastCommand("TEST COMMAND", type="FILES", command="cmd /c echo 'Hello world'")
fc.compile()