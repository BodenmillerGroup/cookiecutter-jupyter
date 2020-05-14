# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Installation

To create a new conda environment (reproducible, recommended):
```bash
conda env create -f environment.yml
```

Alternatively, to update an existing environment to the most up-to-date dependency versions:
```bash
conda install --file requirements.txt
```

## Usage

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Authors

{{cookiecutter.author_name}}

## Contributors

## Acknowledgements

{% if cookiecutter.license != 'No license' %}
## License

{% if cookiecutter.license == 'GNU GPLv3' %}
[GNU GPLv3](LICENSE)
{% elif cookiecutter.license == 'Apache License 2.0' %}
[Apache License 2.0](LICENSE)
{% elif cookiecutter.license == 'MIT License' %}
[MIT License](LICENSE)
{% endif %}
{% endif %}
