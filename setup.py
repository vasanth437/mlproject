from setuptools  import find_packages,setup
from typing import List

def get_requirements(filepath:str) -> List[str]:
    '''
    This function wyll return the list of requirements

    '''
    HYPEN_E_DOT = '-e .'
    requirements= []
    with open(filepath) as file_obj:
        requirements = [line.strip() for line in file_obj.readlines()]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements


setup(
name = 'ML project',
version =  '0.00.1',
author = 'Vasanth',
author_email = 'nanivasanth437@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)