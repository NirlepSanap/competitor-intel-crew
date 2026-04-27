from crewai_tools import FileWriterTool
import os

# Ensure output folder exists before the tool is used
os.makedirs("./output", exist_ok=True)

# FileWriterTool lets the Report Writer agent save the
# final markdown report directly to disk as part of its task.
#
# directory= locks ALL writes to ./output/ so files never
# scatter across the project folder.
#
# Used by: Report Writer
# No API key needed.

file_writer_tool = FileWriterTool(directory="./output/")