import nbformat


def generate_toc(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = nbformat.read(f, as_version=4)

    # Extract headers
    toc = []
    for cell in notebook.cells:
        if cell.cell_type == 'markdown':
            lines = cell.source.split('\n')
            for line in lines:
                if line.startswith('#'):
                    # Count the number of '#' to determine the level
                    level = line.count('#')
                    title = line.strip('#').strip()
                    toc.append((level, title))

    toc_md = "## Table of Contents\n"
    for level, title in toc:
        indent = '  ' * (level - 1)
        toc_md += f"{indent}- [{title}](#{title.lower().replace(' ', '-')})\n"

    return toc_md


if __name__ == '__main__':
    notebook_path = 'notebooks/mixed_topics/ornstein_uhlenbeck_estimation.ipynb'
    toc = generate_toc(notebook_path)
    print(toc)
