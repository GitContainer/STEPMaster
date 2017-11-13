import os

  # Flush and clean up the contents of output folder to make sure there is no files inside

output_directory = '../output'
for dirpath, dirnames, filenames in os.walk(output_directory):
    # Remove regular files and ignore directories
    for filename in filenames:
        os.unlink(os.path.join(dirpath, filename))