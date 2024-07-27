import os
import readline
import subprocess

def list_files(path="."):
    try:
        for entry in os.listdir(path):
            print(entry)
    except FileNotFoundError:
        print(f"\033[1;37;41mls: cannot access '{path}': No such file or directory\033[0m")

def print_working_directory():
    print(os.getcwd())

def change_directory(path):
    try:
        os.chdir(path)
    except FileNotFoundError:
        print(f"\033[1;37;41mcd: {path}: No such file or directory\033[0m")

def make_directory(path):
    try:
        os.makedirs(path)
    except FileExistsError:
        print(f"\033[1;37;41mmkdir: cannot create directory '{path}': File exists\033[0m")

def move_or_rename(src, dest):
    try:
        os.rename(src, dest)
    except FileNotFoundError:
        print(f"\033[1;37;41mmv: cannot stat '{src}': No such file or directory\033[0m")

def copy_file(src, dest):
    try:
        with open(src, 'rb') as fsrc, open(dest, 'wb') as fdest:
            fdest.write(fsrc.read())
    except FileNotFoundError:
        print(f"\033[1;37;41mcp: cannot stat '{src}': No such file or directory\033[0m")

def remove_file_or_directory(path):
    try:
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.remove(path)
    except FileNotFoundError:
        print(f"\033[1;37;41mrm: cannot remove '{path}': No such file or directory\033[0m")

def create_empty_file(path):
    try:
        with open(path, 'w') as file:
            pass
        print(f"File '{path}' created successfully.")
    except Exception as e:
        print(f"\033[1;37;41mcreate: {str(e)}\033[0m")

def create_symbolic_link(target, link_name):
    try:
        os.symlink(target, link_name)
    except FileExistsError:
        print(f"\033[1;37;41mln: failed to create symbolic link '{link_name}': File exists\033[0m")

def clear_screen():
    os.system('clear')

def display_file_contents(path):
    try:
        with open(path, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"\033[1;37;41mcat: {path}: No such file or directory\033[0m")

def print_text(text):
    print(text)

def display_paged_output(path):
    os.system(f'less {path}')

def access_manual_pages(command):
    os.system(f'man {command}')

def get_os_information():
    os.system('uname -a')

def display_active_username():
    os.system('whoami')

def edit_file_with_nano(path):
    try:
        subprocess.run(['nano', path])
    except FileNotFoundError:
        print(f"\033[1;37;41mnano: {path}: No such file or directory\033[0m")

def execute_command(command):
    args = command.split()
    if not args:
        return

    cmd = args[0]
    try:
        if cmd == "ls":
            list_files(args[1] if len(args) > 1 else ".")
        elif cmd == "pwd":
            print_working_directory()
        elif cmd == "cd":
            change_directory(args[1] if len(args) > 1 else ".")
        elif cmd == "mkdir":
            make_directory(args[1])
        elif cmd == "mv":
            move_or_rename(args[1], args[2])
        elif cmd == "cp":
            copy_file(args[1], args[2])
        elif cmd == "rm":
            remove_file_or_directory(args[1])
        elif cmd == "touch":
            create_empty_file(args[1])
        elif cmd == "ln":
            create_symbolic_link(args[1], args[2])
        elif cmd == "clear":
            clear_screen()
        elif cmd == "cat":
            display_file_contents(args[1])
        elif cmd == "echo":
            print_text(" ".join(args[1:]))
        elif cmd == "less":
            display_paged_output(args[1])
        elif cmd == "man":
            access_manual_pages(args[1])
        elif cmd == "uname":
            get_os_information()
        elif cmd == "whoami":
            display_active_username()
        elif cmd == "nano":
            if len(args) > 1:
                edit_file_with_nano(args[1])
            else:
                print(f"\033[1;37;41mnano: missing file operand\033[0m")
        elif cmd == "create":
            if len(args) > 1:
                create_empty_file(args[1])
            else:
                print(f"\033[1;37;41mcreate: missing file operand\033[0m")
        elif cmd == "exit":
            exit(0)
        else:
            print(f"\033[1;37;41mCommand not found: {cmd}\033[0m")
    except IndexError:
        print(f"\033[1;37;41m{cmd}: missing operand\033[0m")
    except FileNotFoundError:
        print(f"\033[1;37;41m{cmd}: {args[1]}: No such file or directory\033[0m")
    except Exception as e:
        print(f"\033[1;37;41m{cmd}: {str(e)}\033[0m")

def main():
    while True:
        try:
            current_dir = os.path.basename(os.getcwd())
            user_input = input(f"\033[1;32mPyTerm ~ {current_dir} ~\033[0m >>> ").strip()
            if user_input:
                execute_command(user_input)
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt: Use 'exit' to quit.")

if __name__ == "__main__":
    main()
  
