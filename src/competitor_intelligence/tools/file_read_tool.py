from crewai_tools import FileReadTool

# FileReadTool lets an agent read a file that already exists.
# The Report Writer uses this to read back the report it just
# saved, verify nothing is missing, and optionally add a
# summary section at the top.
#
# Used by: Report Writer (optional verification step)
# No API key needed.

file_read_tool = FileReadTool()