from colab_toolbox.common.utils import get_script_content, write_script, run_script
class ColabInstall:
    def __init__(self, tool_name):
        """
        Setup the specified tool in the Colab environment.
        Args:
            tool_name: Name of the tool to be setup. List of available tools:
                - selenium
                - quarto
                - talib
                - pytesseract
        """
        self.tool_name = tool_name
        self.content = get_script_content(f'setup_{tool_name}.sh')
        self.script_path = write_script(f'setup_{tool_name}.sh', self.content)
        self.run_script()

    def run_script(self):
        run_script(self.script_path)