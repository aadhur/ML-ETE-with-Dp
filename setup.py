from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]: #function takes in str pth and returns list
    '''
    This function will take the modelues mentioned in the requirements.txt
    '''
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", " ") for req in requirements ]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)


setup(
    name='ml-ete-dp',
    version='0.0.1',
    author='aadhur',
    author_email='aadhurshini.chitra@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')    
)