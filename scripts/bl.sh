#!/bin/bash

usage() { 
    echo "usage: $0 [-s] [-g] [--ps] [--pdf] <tex-prefix>" 1>&2
    exit 1
}

# preliminary command line argument check
if [ "$#" -eq 0 ] || [[ "$1" == "-h" ]]; then
    usage
fi

# spell check and grammar check
s=0
g=0
tops=0
psfile=""
topdf=0
pdffile=""

while getopts "sg-:" option; do
    case "${option}" in
        s)
            s=1
            ;;
        g)
            g=1
            ;;
        ps)
            tops=1
            psfile=${OPTARG}
            ;;
        pdf)
            topdf=1
            pdffile=${OPTARG}
            ;;
        *)
            echo " here" 
            usage
            ;;
    esac
done
shift $((OPTIND-1))


echo "s = ${s}"
echo "g = ${g}"

