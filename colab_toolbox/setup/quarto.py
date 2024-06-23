from colab_toolbox.common.utils import get_script_content, write_script, run_script

def setup_selenium():
    script_name = 'setup_quarto.sh'
    content = get_script_content(script_name)
    script_path = write_script(script_name, content)
    run_script(script_path)
