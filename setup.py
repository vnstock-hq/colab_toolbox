from setuptools import setup, find_packages
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='colab_toolbox',
    version='0.1.1',
    description='Effortlessly set up and configure multiple tools for Google Colab without the need for shell commands or extensive coding.',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/thinh-vu/colab_toolbox',  # Update this to your GitHub repo URL
    author='Thinh Vu',
    author_email='vnstock-hq@gmail.com',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(include=['colab_toolbox', 'colab_toolbox.*']),
    include_package_data=True,
    package_data={
        'colab_toolbox': ['script/*.sh'],
    },
    install_requires=[
        # Add any additional packages required by your project here
        # Example: 'some_package>=1.0.0',
    ],
    entry_points={
        'console_scripts': [
            'colab_toolbox=colab_toolbox.colabtool:main',
        ],
    },
)
