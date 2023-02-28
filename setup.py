from setuptools import find_packages , setup

def get_requirements():
    pass

setup(
    name='sensor',
    version="0.0.1",
    author='ineuron',
    author_email="mukulsingh078968",
    packages= find_packages(),
    install_require=get_requirements(),
)