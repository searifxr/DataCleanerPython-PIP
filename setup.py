from setuptools import setup, find_packages

setup(
    name='datacleanerPython',
    version='1.0.0',
    description='Automated data cleaning and visualization tool',
    author='Krishna Nihal Pothapragada',
    packages=find_packages(),
    package_data={},
    exclude_package_data={
        '': ['*.csv', 'outputs/*'],
    },
    install_requires=[
        'pandas>=2.0.0',
        'matplotlib>=3.7.0',
    ],
    entry_points={
        'console_scripts': [
            'datacleaner=process_data:main',
        ],
    },
    python_requires='>=3.7',
)
