from setuptools import find_packages, setup

setup(
    name='macinfo',
    packages=find_packages(include=['macinfo', 'tests']),
    version='0.1.0',
    description='A tool to get mac-address info.',
    author='Kamil Bagautdinov',
    install_requires=['setuptools', 'wheel', 'twine'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==7.1.2', 'requests==1.26.12'],
    test_suite='tests',
)
