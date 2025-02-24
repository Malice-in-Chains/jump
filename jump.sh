#!/bin/bash
# Written by MaliceInChains - maliceinchains106@gmail.com 
# -----------------------------------------------------------------
# jump.sh Allows you to set a specific directory (-s) that you can jump back to later without excessive typing of the full directory
# -----------------------------------------------------------------

jump() {
    local jump_file="$HOME/.jump"

    case "$1" in
        -s)
            pwd > "$jump_file"
            echo "Jump point set to: $(pwd)"
            ;;
        "")
            if [[ -f "$jump_file" ]]; then
                jumpdir=$(<"$jump_file")
                cd "$jumpdir" || echo "ERROR: Failed to change directory to $jumpdir"
            else
                echo "ERROR: Jump not set. Use -s to set the current directory."
            fi
            ;;
        *)
            echo "ERROR: Bad Jump Command. Use -s to set a jump point or no argument to jump."
            ;;
    esac
}
