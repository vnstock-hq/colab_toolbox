import os
import subprocess

def write_script(script_name, content):
    """
    Writes the script content to a file in the working directory.

    :param script_name: Name of the script file (e.g., 'setup_selenium.sh')
    :param content: Script content to be written to the file
    """
    script_path = os.path.join("/content", script_name)
    with open(script_path, "w") as script_file:
        script_file.write(content)
    os.chmod(script_path, 0o755)
    return script_path

def run_script(script_path):
    """
    Runs the specified script using subprocess.

    :param script_path: Path to the script file
    """
    process = subprocess.Popen(["bash", script_path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while True:
        output = process.stdout.readline()
        if output == b"" and process.poll() is not None:
            break
        if output:
            print(output.decode().strip())
    rc = process.poll()
    return rc

def get_script_content(script_name):
    """
    Retrieves the script content from the package.

    :param script_name: Name of the script file (e.g., 'setup_selenium.sh')
    :return: Script content as a string
    """
    script_path = os.path.join(os.path.dirname(__file__), '..', 'script', script_name)
    with open(script_path, "r") as script_file:
        content = script_file.read()
    return content
