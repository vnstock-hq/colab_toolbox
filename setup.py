from setuptools import setup, find_packages

setup(
    name='colab_toolbox',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'colab_toolbox': ['script/*.sh'],
    },
    install_requires=[
        # Add any additional packages required by your project
    ],
    entry_points={
        'console_scripts': [
            'colab_toolbox=colab_toolbox.__main__:main',
        ],
    },
)
