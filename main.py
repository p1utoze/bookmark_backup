import os
from src.bookmark_extract import Bookmark

parent = os.getcwd()
# Set the location of the python file
python_file = os.path.join(parent, "src", "json_file.py")

# Set the frequency of the cron job.
# This example runs the job every 3 hours.
frequency = "0 */3 * * *"

# Create the command to be run by the cron job
python_path = Bookmark.python_path()

command = f"{frequency} {python_path} {python_file} &"

# Add the cron job to the crontab file
cron_path = os.path.join(parent, 'src', 'crontab.txt')

os.system(f"crontab -l > {cron_path}")
with open(cron_path, "a") as f:
    f.write(f"{command}\n")
os.system(f"crontab {cron_path}")

# Print a message to confirm that the cron job was added
os.system(f"Cron job added for Bookmarks")
