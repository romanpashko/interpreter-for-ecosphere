import argparse
from rich import print
from rich.markdown import Markdown

confirm_mode_message = """
**Open Interpreter** will require approval before running code. Use `interpreter -y` to bypass this.

Press `CTRL-C` to exit.
"""


def cli(interpreter):
  """
  Takes an instance of interpreter.
  Modifies it according to command line flags, then runs chat.
  """

  parser = argparse.ArgumentParser(description='Chat with Open Interpreter.')
  parser.add_argument('-y',
                      '--yes',
                      action='store_true',
                      help='execute code without user confirmation')
  args = parser.parse_args()

  if args.yes:
    interpreter.auto_run = True
  else:
    print()  # Print newline
    print(Markdown(confirm_mode_message))
    print()  # Print newline

  # Now run the chat method
  interpreter.chat()
