# static-website-generator

A simple tool written in Python for generating static websites from Markdown content and HTML templates.

## Features

- Converts Markdown content to HTML
- Applies Jinja2 templates for consistent styling
- Supports metadata for each post/page
- Configuration via `config.yaml`
- Basic logging for clear generation feedback

## Getting Started

1. Clone the repository: `git clone https://github.com/Totodile-Liam/static-website-generator.git`
2. Navigate to the project directory: `cd static-website-generator`

### Prerequisites

- Python 3.x
- Required dependencies: `markdown`, `jinja2`, `pyyaml`

You can install the required dependencies using the following command:

```bash
pip install markdown jinja2 pyyaml
```

## Usage
1. Place your Markdown content in the content/ directory.
2. Define HTML templates in the templates/ directory.
3. Configure your settings in config.yaml.

Run the generator script:
```bash
python app.py
```
Generated HTML files will be saved in the output/ directory.

## Configuration
You can configure the generator by editing config.yaml:

```yaml
Copy code
input_dir: content      # Directory containing your Markdown content
output_dir: output      # Directory to save generated HTML files
```

## Contributing
Contributions are welcome! If you have any improvements or bug fixes, feel free to submit a pull request.

