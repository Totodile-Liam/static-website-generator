import os
import markdown
import jinja2
import yaml

# Load configuration from config.yaml
with open('config.yaml', 'r') as config_file:
    config = yaml.load(config_file, Loader=yaml.FullLoader)

# Create Jinja2 environment
template_loader = jinja2.FileSystemLoader('templates')
template_env = jinja2.Environment(loader=template_loader)

# Ensure the output directory exists
if not os.path.exists(config['output_dir']):
    os.makedirs(config['output_dir'])

# Load templates
base_template = template_env.get_template('base.html')
post_template = template_env.get_template('post.html')

# Loop through all files in the content directory
for filename in os.listdir(config['input_dir']):
    if filename.endswith('.md'):
        # Read the Markdown content
        with open(os.path.join(config['input_dir'], filename), 'r') as f:
            markdown_content = f.read()

        # Convert Markdown to HTML
        html_content = markdown.markdown(markdown_content)

        # Get metadata if available
        metadata = {}
        metadata_file = os.path.join(config['input_dir'], os.path.splitext(filename)[0] + '.yaml')
        if os.path.exists(metadata_file):
            with open(metadata_file, 'r') as md_file:
                metadata = yaml.load(md_file, Loader=yaml.FullLoader)

        # Render the post template
        post_html = post_template.render(content=html_content, metadata=metadata)

        # Create the corresponding HTML file in the output directory
        output_filename = os.path.splitext(filename)[0] + '.html'
        with open(os.path.join(config['output_dir'], output_filename), 'w') as f:
            final_html = base_template.render(content=post_html)
            f.write(final_html)

print("Website generation complete.")

