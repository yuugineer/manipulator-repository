import sys

def reverse_file(input_path,output_path):
    with open(input_path,"r") as input_file:
        content = input_file.read()
    with open(output_path,"w") as output_file:
        output_file.write(content[::-1])

def copy_file(input_path,output_path):
    with open(input_path,"r") as input_file:
        content = input_file.read()
    with open(output_path,"w") as output_file:
        output_file.write(content)

def duplicate_contents(input_path,n):
    with open(input_path,"r") as file:
        content = file.read()
    with open(input_path,"w") as file:
        file.write(content * (n+ 1))

def replace_string(input_path,needle,newstring):
    with open(input_path,"r") as file:
        content = file.read()
    content = content.replace(needle,newstring)
    with open(input_path,"w") as file:
        file.write(open)

def validate_args(command,args):
    if command == "reverse" and len(args) !=2:
        return False
    elif command == "copy" and len(args) !=2:
        return False
    elif command =="duplicate-contents" and len(args) !=2:
        return False
    elif command == "replace-string" and len(args) != 3:
        return False
    return True

def main():
    if len(sys.argv) < 3:
        print("Usage: python file_manipulator.py <command> <args>")
        sys.exit(1)
    
    command = sys.argv[1]
    args = sys.argv[2:]

    if not validate_args(command,args):
        print(f"Invalid arguments for command: {command}")
        sys.exit(1) 
    

    try:
        if command == "reverse":
            reverse_file(args[0],args[1])
        elif command == "copy":
            copy_file(args[0],args[1])
        elif command == "duplicate-contents":
            duplicate_contents(args[0], int(args[1]))
        elif command == "replace-string":
            replace_string(args[0], args[1], args[2])
        else:
            print(f"Unknown command: {command}")
            sys.exit(1)
    except FileNotFoundError:
        print(f"Eroor: File not found - {args[0]}")
    except ValueError:
        print("Eroor: Invalid number for duplicate-contents command")
    except Exception as e:
        print(f"An error occurred:{str(e)}")
    
if __name__ == "__main__":
    main()
