import os
import subprocess
from typing import Union
from google.colab import auth
from google.colab import userdata

class GitTool:
    def __init__(self, secret_name: str, repo_url: str):
        """
        Initialize the class to work with a private Git repository.
        """
        self.secret_name = secret_name
        self.access_key = self._get_secret(secret_name)

        if repo_url:
            self.user_name = repo_url.split('/')[3]
            self.repo_name = repo_url.split('/')[4]

        self._config()

    def _get_secret(self, secret_name: str) -> str:
        """
        Get the secret value from Google Colab's secret storage.
        """
        # Authenticate the user
        auth.authenticate_user()
        # Get the secret
        access_key = userdata.get(secret_name)
        if not access_key:
            raise ValueError(f"Secret {secret_name} not found. Please add it to the Colab secrets.")
        return access_key

    def _config(self, user_name: Union[str, None] = None, email: Union[str, None] = None):
        """
        Configure the Git credentials.
        """
        # Create the Git credentials file
        try:
            with open(os.path.expanduser("~/.git-credentials"), "w") as f:
                f.write(f"https://{self.access_key}:x-oauth-basic@github.com\n")

            # Set the Git user configuration
            user_name = user_name or self.user_name
            email = email or f"{self.user_name}@users.noreply.github.com"
            
            subprocess.run(f"git config --global user.name '{user_name}'", shell=True, check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            subprocess.run(f"git config --global user.email '{email}'", shell=True, check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            subprocess.run("git config --global credential.helper 'store --file ~/.git-credentials'", shell=True, check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            error_message = e.stderr.decode('utf-8') if e.stderr else "An error occurred during Git configuration."
            print(f"Error during Git configuration: {error_message}")

    def clone(self, branch_name: Union[str, None] = None):
        """
        Clone a private repository to the current working directory.
        """
        # get current directory
        current_dir = os.getcwd()
        try:
            if branch_name:
                command = f"git clone -b {branch_name} https://{self.access_key}@github.com/{self.user_name}/{self.repo_name}.git"
            else:
                command = f"git clone https://{self.access_key}@github.com/{self.user_name}/{self.repo_name}.git"

            result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)         
            print(result.stdout.decode('utf-8'))
            print(f'Repository {self.repo_name} has been cloned successfully!')
            # get the repo directory
            self.repo_dir = os.path.join(current_dir, self.repo_name)
        except subprocess.CalledProcessError as e:
            error_message = e.stderr.decode('utf-8') if e.stderr else "An error occurred during cloning."
            print(f"Error during cloning: {error_message}")

    def commit(self, message: str, repo_dir: Union[str, None] = None):
        """
        Add changes to the Git staging area and commit them.
        """
        try:
            # change directory to the repo directory
            if repo_dir:
                os.chdir(repo_dir)
            else:
                os.chdir(self.repo_dir)
            
            # Print the current status of the git repository
            status_result = subprocess.run("git status", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            print(status_result.stdout.decode('utf-8'))

            # add changes to the staging area
            subprocess.run("git add .", shell=True, check=True)

            # Check for staged changes
            diff_result = subprocess.run("git diff --cached", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            if not diff_result.stdout:
                print("No changes to commit.")
                return
            
            # commit the changes
            subprocess.run(f"git commit -m '{message}'", shell=True, check=True)
            print("Changes have been committed.")
        except subprocess.CalledProcessError as e:
            error_message = e.stderr.decode('utf-8') if e.stderr else "An error occurred during adding changes."
            print(f"Error during adding changes: {error_message}")

    def push(self, message: str, branch: Union[str, None] = None):
        """
        Push changes to the Git repository.
        """
        try:
            self.commit(message)
            
            if branch:
                command = f"git push -u https://{self.access_key}@github.com/{self.user_name}/{self.repo_name}.git {branch}"
            else:
                command = "git push"

            result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            print(result.stdout.decode('utf-8'))

        except subprocess.CalledProcessError as e:
            error_message = e.stderr.decode('utf-8') if e.stderr else "An error occurred during push."
            print(f"Error during push: {error_message}")