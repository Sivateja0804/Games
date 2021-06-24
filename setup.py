from setuptools import setup,find_packages
setup(
    name='Games',    # This is the name of your PyPI-package.
    version='0.1.13',
    packages=find_packages(),# Update the version number for new releases
    entry_points={"console_scripts": ["games=src.play_games:main"]}                 # The name of your script, and also the command you'll be using for calling it
)
