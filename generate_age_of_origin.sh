#!/bin/bash

cd MetaGPT/

# Read content of age_of_origin.md into a variable
idea_content=$(<prompts/age_of_origin.md)
echo $idea_content
# Run the python script with the idea_content as argument
python startup.py "$idea_content" 10.0
