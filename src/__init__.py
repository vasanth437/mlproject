from setuptools  import find_packages,setup
from typing import List

def get_requirements(filepath:str) -> List[str]:
    '''
    This function wyll return the list of requirements

    '''
    requirements= []
    with open(filepath) as file_obj:
        requirments = file_obj.readlines()


print(get_requirements('requirements.txt'))