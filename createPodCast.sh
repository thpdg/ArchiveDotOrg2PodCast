#! bin/bash
# Reference URL is https://archive.org/download/OA-2005-11

echo "Audio source URL is $1" 

# Download specified URL
curl $1 > sourceList.htm

python findMatches.py sourceList.htm $1 $2


# Prepare start of RSS file with initial podcast metadata

# Search stored file for links to mp3 files

    # Reconstruct path to mp3 file

    # Prepare metadata for specified mp3 file

    # Add mp3 file path to RSS file

# Complete RSS file for proper podcast format


