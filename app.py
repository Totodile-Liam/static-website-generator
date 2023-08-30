import os
import markdown
import jinja2
import yaml
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_config(config_path):
    with open(config_path, 'r') as config_file:
        config = yaml.safe_load(config_file)
    return config

def read_markdown_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def load_metadata(metadata_path):
    metadata = {}
    if os.path.exists(metadata_path):
        with open(metadata_path, 'r') as md_file:
            metadata = yaml.safe_load(md_file)
    return metadata

def generate_html_content(markdown_content):
    return markdown.markdown(markdown_content)

def generate_output(output_dir, output_filename, base_template, post_html):
    final_html = base_template.render(content=post_html)
    output_path = os.path.join(output_dir, output_filename)
    with open(output_path, 'w') as f:
        f.write(final_html)
    logger.info(f"Generated: {output_path}")

def main():
    config = load_config('config.yaml')

    template_loader = jinja2.FileSystemLoader('templates')
    template_env = jinja2.Environment(loader=template_loader)

    base_template = template_env.get_template('base.html')
    post_template = template_env.get_template('post.html')

    if not os.path.exists(config['output_dir']):
        os.makedirs(config['output_dir'])

    for filename in os.listdir(config['input_dir']):
        if filename.endswith('.md'):
            input_file_path = os.path.join(config['input_dir'], filename)
            markdown_content = read_markdown_file(input_file_path)
            html_content = generate_html_content(markdown_content)

            metadata_path = os.path.join(config['input_dir'], os.path.splitext(filename)[0] + '.yaml')
            metadata = load_metadata(metadata_path)

            post_html = post_template.render(content=html_content, metadata=metadata)

            output_filename = os.path.splitext(filename)[0] + '.html'
            generate_output(config['output_dir'], output_filename, base_template, post_html)

    logger.info("Website generation complete.")

if __name__ == "__main__":
    main()
