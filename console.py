import cmd
from models.base_model import BaseModel
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    # aliasing
    do_EOF = do_quit

    def emptyline(self):
        """Empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id"""
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_instance = BaseModel()
                storage.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class
        name and id"""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in ["BaseModel"]:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                try:
                    eval(args[0])()
                except NameError:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in ["BaseModel"]:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                try:
                    eval(args[0])()
                except NameError:
                    print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on
        the class name"""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in ["BaseModel"]:
                print("** class doesn't exist **")
            else:
                try:
                    eval(args[0])()
                except NameError:
                    print("** no instance found **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
        updating attribute"""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in ["BaseModel"]:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                try:
                    eval(args[0])()
                except NameError:
                    print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
