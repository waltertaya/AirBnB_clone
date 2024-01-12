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

    # help quit
    def help_quit(self):
        print("Quit command to exit the program\n")

    def help_EOF(self):
        print("Quit command to exit the program\n")

    def emptyline(self):
        """Empty line + ENTER shouldn’t execute anything"""
        pass

    # help emptyline
    def help_emptyline(self):
        print("Empty line + ENTER shouldn’t execute anything\n")

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

    # help create
    def help_create(self):
        print("Creates a new instance of BaseModel, saves it (to the JSON "
              "file) and prints the id\n")

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
            elif args[0] + "." + args[1] not in storage.all():
                print("** no instance found **")
            else:
                try:
                    instance_id = args[0] + "." + args[1]
                    if instance_id not in storage.all():
                        print("** no instance found **")
                        return
                    print(storage.all()[instance_id])
                except NameError:
                    print("** no instance found **")

    # help show
    def help_show(self):
        print("Prints the string representation of an instance based on the "
              "class name and id\n")

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
                    instance_id = args[0] + "." + args[1]
                    if instance_id not in storage.all():
                        print("** no instance found **")
                        return

                    del storage.all()[instance_id]
                    storage.save()
                except NameError:
                    print("** no instance found **")

    # help destroy
    def help_destroy(self):
        print("Deletes an instance based on the class name and id\n")

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
                    my_list = []
                    new_instance = storage.all()
                    for k, v in new_instance.items():
                        my_list.append(str(storage.all()[k]))
                    print(my_list)
                except NameError:
                    print("** no instance found **")

    # help all
    def help_all(self):
        print("Prints all string representation of all instances based or not "
              "on the class name\n")

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
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                try:
                    instance_id = args[0] + "." + args[1]
                    if instance_id not in storage.all():
                        print("** no instance found **")
                        return

                    updated_instance = storage.all()[instance_id]
                    setattr(updated_instance, args[2], args[3])
                    storage.save()
                except NameError:
                    print("** no instance found **")

    # help update
    def help_update(self):
        print("Updates an instance based on the class name and id by adding "
              "or updating attribute\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
