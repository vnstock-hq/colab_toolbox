from colab_toolbox.common.utils import get_script_content, write_script, run_script
class ColabTool:
    def __init__(self, tool_name):
        self.tool_name = tool_name
        self.content = get_script_content(f'setup_{tool_name}.sh')
        self.script_path = write_script(f'setup_{tool_name}.sh', self.content)
        self.run_script()

    def run_script(self):
        run_script(self.script_path)