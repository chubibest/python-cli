from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()
setup(
        name='hr',
        version='0.1.0',
        description='Not really sure',
        long_description=readme,
        author='Chubi',
        author_email='chubi.best@gmail.com',
        packages=find_packages('src'),
        package_dir={'': 'src'},
        install_requires=[],
        entry_points={
            'console_scripts': [
                'hr=hr.cli:main',
                ]
            }
        )
# install_requires is for dependencies I think
