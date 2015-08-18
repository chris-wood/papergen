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
s=0
g=0
tops=0
psfile=""
topdf=0
pdffile=""
texfile=""

while getopts "f:sg-:" option; do
    case "${option}" in
        f)
            texfile=${OPTARG}
            ;;
        s)
            s=1
            ;;
        g)
            g=1
            ;;
        ps)
            tops=1
            # TODO: check for OPTARG length, and defer to default name
            psfile=${OPTARG}
            ;;
        pdf)
            topdf=1
            # TODO: same as above
            pdffile=${OPTARG}
            ;;
        *)
            usage
            ;;
    esac
done
shift $((OPTIND-1))

echo "Building ${texfile}..."

# TODO: run tex-parser to get raw text

if [ "$s" -eq 1 ]; then
    echo spell check... 
    # TODO: run raw text through the spell checker
fi
if [ "$g" -eq 1 ]; then
    echo grammar check...
    # TODO: run raw text through grammar checker
fi

echo "s = ${s}"
echo "g = ${g}"

