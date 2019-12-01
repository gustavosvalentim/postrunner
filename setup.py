from setuptools import setup


setup(
    name='postrunner',
    version='1.0',
    description='Run Postman collections using Python',
    packages=['postrunner'],
    python_requires='>3.6',
    install_requires=[
        'requests',
        'jsonpath_rw'
    ]
)