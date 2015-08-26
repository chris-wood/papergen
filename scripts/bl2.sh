#!/bin/bash

usage() { 
    echo "usage: $0 [-s] [-g] [--ps] [--pdf] <tex-prefix>" 1>&2
    exit 1
}

# preliminary command line argument check
if [ "$#" -eq 0 ] || [[ "$1" == "-h" ]]; then
    usage
fi

# flags and options
SPELLING=0
GRAMMAR=0
TOPS=0
PSFILE=""
TOPDF=0
PDFFILE=""
TEXFILE=""

while [[ $# -gt 0 ]]; do
    opt="$1"
    shift; # swallow front of the line
    current_arg="$1"

    case "$opt" in
        "-s"|"--spelling" ) SPELLING=1; shift ;;
        "-g"|"--grammar"  ) GRAMMAR=1; shift ;;
        "-ps"             ) TOPS=1; PSFILE="$1"; shift ;;
        "-pdf"            ) TOPDF=1; PDFFILE="$1"; shift ;;
        "-f"|"--file"     ) 
            # if the next argument is another flag, something's gone wrong
            if [[ "$current_arg" =~ ^-{1,2} ]]; then
                usage # exits
            fi;
            TEXFILE="$1"; shift ;;
        *                 ) echo "ERROR: Invalid option: \""$opt"\"" >&2; exit 2 ;;
    esac
done

echo "Building ${texfile}..."

# TODO: run tex-parser to get raw text

if [ "$SPELLING" -eq 1 ]; then
    echo spell check... 
    # TODO: run raw text through the spell checker
fi
if [ "$GRAMMAR" -eq 1 ]; then
    echo grammar check...
    # TODO: run raw text through grammar checker
fi
if [ "$TOPS" -eq 1 ]; then
    echo "generate PS..."
    echo "PSFILE = ${PSFILE}" 
fi
if [ "$TOPDF" -eq 1 ]; then
    echo "generate PDF..."
    echo "PDFFILE = ${PDFFILE}"
fi

echo "SPELLING? = ${SPELLING}"
echo "GRAMMAR? = ${GRAMMAR}"

