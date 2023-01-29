"""Setup file for project english-lab."""


from setuptools import find_packages, setup

setup(
    name='english-lab',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-login',
        'flask-sqlalchemy',
        'flask-migrate',
        'flask-wtf',
        'bootstrap-flask',
        'python-dotenv'
    ]
)
