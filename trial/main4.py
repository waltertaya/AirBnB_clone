import cmd

class Trial(cmd.Cmd):
    
    prompt = 'trial >> '
    
    def do_quit(self, arg):
        '''Quit command to exit the program'''
        return True
    
    def onecmd(self, line):
        if line.endswith('.all()'):
            # Extract the command part (excluding the '.all()')
            command = line.rsplit('.all()', 1)[0].strip()
            
            # Call the corresponding method
            return self.default(command)
        else:
            # If the input doesn't end with '.all()', use the default behavior
            return super().onecmd(line)

    def default(self, line):
        '''Default method for handling commands'''
        print(f"Executing command: {line}")

Trial().cmdloop()

