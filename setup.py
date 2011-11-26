from setuptools import setup, find_packages

setup(
    name='simple-project',
    version='0.1',
    url='',
    packages=find_packages('.'),
    package_dir={'': '.'},
    install_requires=(
        'setuptools',
        'MySQL-python',
        'django-extensions',
        'South',      
    ),
)  


