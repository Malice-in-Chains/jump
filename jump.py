#!/usr/bin/env python
# Written by MaliceInChains - maliceinchains106@gmail.com 
# -----------------------------------------------------------------
# jump.py Allows you to set a specific directory (-s) that you can jump back to later without excessive typing of the full directory
# -----------------------------------------------------------------

import os
import sys

def jump(command=None):
    jump_file = os.path.expanduser("~/.jump")

    if command == "-s":
        # Save the current directory to the jump file
        with open(jump_file, 'w') as f:
            f.write(os.getcwd())
        print(f"Jump point set to: {os.getcwd()}")

    elif command is None:
        # Attempt to read the jump file and change the directory
        if os.path.exists(jump_file):
            with open(jump_file, 'r') as f:
                jump_dir = f.read().strip()
                try:
                    os.chdir(jump_dir)
                    print(f"Changed directory to: {jump_dir}")
                except FileNotFoundError:
                    print(f"ERROR: The directory '{jump_dir}' does not exist.")
        else:
            print("ERROR: Jump not set. Use -s to set your current directory.")
    
    else:
        print("ERROR: Bad Jump Command. Use -s to set a jump point or no argument to jump.")

if __name__ == "__main__":
    # Pass command line arguments to the jump function
    jump_command = sys.argv[1] if len(sys.argv) > 1 else None
    jump(jump_command)
