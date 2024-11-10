from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    """
    This function will return the list of requirements
    """
    
    requirements = []
    with open('requirements.txt') as file_obj:
        requirements = file_obj.readlines()
        # Take out the "\n" caused by new line
        requirements = [req.replace('\n', ' ') for req in requirements]

        if HYPEN_E_DOT in requirements: # Remove element
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    name="SimpleLinearRegressionProject",
    version="0.0.1",
    author="Jacob",
    author_email="Jacobiv2001@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)