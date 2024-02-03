#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <folder_path> <FILENAME>"
    exit 1
fi

# Extract folder path and file name from command line arguments
folder_path="$1"
FILENAME="$2"

# Create the folder if it doesn't exist
mkdir -p "$folder_path"

# Create FILENAME.py
touch "$folder_path/$FILENAME.py"

# Create FILENAME_test.py
touch "$folder_path/${FILENAME}_test.py"

# Create FILENAME.md with template content
cat > "$folder_path/$FILENAME.md" <<EOL
## Details for question

Link: [here](problem-link-here)

Tags: adhoc, bit

Description:

- Point 1

Questions:

- Point 1

Thoughts:

- Point 1

Complexity:

- Time:
- Space:
EOL

cat > "$folder_path/${FILENAME}_test.py" <<EOL
import $FILENAME
import pytest

@pytest.mark.parametrize(
    ("input_1", "input_2", "output"),
    [
        ([1, 3, 4, 8, 7, 9, 3, 5, 1], 2, [[1, 1, 3], [3, 4, 5], [7, 8, 9]]),
        ([1,3,3,2,7,3], 2, []),
    ]
)

def test_problem(input_1, input_2, output):
    s = $FILENAME.Solution()
    # Call you program here. For example:
    # calculated_res = s.fn_name(input_1, input_2)
    # assert calculated_res == output
EOL

echo "Files created successfully in $folder_path"