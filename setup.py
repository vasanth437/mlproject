from setuptools  import find_packages,setup
from typing import List

def get_requirements(filepath:str) -> List[str]:
    '''
    This function wyll return the list of requirements

    '''
    requirements= []
    with open(filepath) as file_obj:
        requirments = file_obj.readlines()


setup(
name = 'ML project',
version =  '0.00.1',
author = 'Vasanth',
author_email = 'nanivasanth437@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)