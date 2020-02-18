from setuptools import setup
setup(
    name='trimmer-cli',
    version='0.1.0',
    packages=['trimmer'],
    entry_points={
        'console_scripts': [
            'trimmer = trimmer.__main__:main'
        ]
    })
