from setuptools import find_packages, setup

setup(
    name='src',
    version='0.1.0',
    description='{{ cookiecutter.description }}',
    author='{{ cookiecutter.author_name }}',{% if cookiecutter.license != 'None' %}
    license='{% if cookiecutter.license == 'GNU GPLv3' %}License :: OSI Approved :: GNU General Public License v3 (GPLv3){% elif cookiecutter.license == 'Apache License 2.0' %}License :: OSI Approved :: Apache Software License{% elif cookiecutter.license == 'MIT License' %}License :: OSI Approved :: MIT License{% endif %}',{% endif %}
    packages=find_packages(include=['src']),
)
