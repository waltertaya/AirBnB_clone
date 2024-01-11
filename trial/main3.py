import cmd


class MyCommand(cmd.Cmd):
    prompt = '(our_command) > '

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    # aliasing -> using another command to execute the same function
    do_exit = do_quit


MyCommand().cmdloop()
