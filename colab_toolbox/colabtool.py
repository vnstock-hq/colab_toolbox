from colab_toolbox.common.utils import *
class ColabInstall:
    def __init__(self, tool_name=None):
        """
        Setup the specified tool in the Colab environment.
        Args:
            tool_name: Name of the tool to be setup. List of available tools:
                - selenium: WebDriver for automated testing of web applications
                - quarto: open-source scientific and technical publishing system 
                - talib: Technical Analysis Library for Stock Trading in Python
                - pytesseract: OCR tool for extracting text from images
                - ocrmypdf: OCR tool for extracting text from PDF files
                - xterm: Terminal emulator for Google Colab environment
        """
        all_tools = ['selenium', 'quarto', 'talib', 'pytesseract', 'xterm', 'ocrmypdf']
        # all_preset = ['terminal', 'trading', 'publishing', 'extracting']

        if tool_name not in all_tools:
            raise ValueError(f'Invalid tool name, available option are: {", ".join(all_tools)}')

        self.tool_name = tool_name
        self.content = get_script_content(f'setup_{tool_name}.sh')
        self.script_path = write_script(f'setup_{tool_name}.sh', self.content)
        self.run_script()

    def run_script(self):
        run_script(self.script_path)