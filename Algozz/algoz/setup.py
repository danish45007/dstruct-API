from setuptools import setup, find_packages

setup(name='Algoz',
      version='1.0',
      description='Cmd based file searching util',
      author='Danish Sharma',
      author_email='danish45007@gmail.com',
      url='https://danish45007.github.io/CLI_Resume/',
      packages=find_packages(),
      entry_points={"console_scripts":["algoz=app:main"]},
     )