# My Pelican Blog

This is a simple **Pelican-based blog** that renders **machine learning content**, including mathematical formulations and code examples, and deploys automatically to **GitHub Pages** using **GitHub Actions**.

The blog is designed to showcase tutorials, research, and explanations related to machine learning, with support for **Markdown**, **LaTeX math equations**, and **syntax highlighting**.

---

## Features

- **Markdown Support**: Easily write blog posts in Markdown format.
- **LaTeX Math Rendering**: Using MathJax to render mathematical equations in LaTeX.
- **GitHub Pages Deployment**: Automatically deploys the blog to GitHub Pages using GitHub Actions.
- **Syntax Highlighting**: Code snippets are highlighted using Pygments.
- **Responsive Design**: The blog is mobile-friendly and works across devices.
- **Customizable Themes**: Easily switch themes and customize your blog's appearance.

---

## Getting Started

### Prerequisites

Make sure you have the following tools installed:

- **Python 3.x** (for local development and Pelican setup)
- **Git** (for version control)
- **A GitHub account** (for hosting the blog on GitHub Pages)

### Installation

To get started with this blog on your local machine, follow these steps:

1. **Clone the repository**:

   Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/your-repository-name.git
   cd your-repository-name
   ```

2. **Create and activate a virtual environment**:

   It’s recommended to use a virtual environment to isolate your Python dependencies.

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install required dependencies**:

   Install Pelican and other necessary dependencies from `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

   If `requirements.txt` doesn't exist yet, you can manually install the required dependencies:

   ```bash
   pip install pelican markdown
   ```

4. **Preview the Blog Locally**:

   You can preview the site on your local machine by running the following command:

   ```bash
   pelican --listen
   ```

   This will start a local server (usually on `http://localhost:8000`), where you can view your blog in action.

---

## Writing Posts

To add a new blog post:

1. Create a new Markdown file in the `content/articles/` directory. For example:

   ```bash
   content/articles/my-new-post.md
   ```

2. The file should follow the standard Markdown syntax. Here's a basic template:

   ```markdown
   Title: My New Post
   Date: 2024-11-01
   Category: Machine Learning
   Tags: ML, Deep Learning, Tutorial
   Slug: my-new-post
   Author: Your Name
   Summary: This is a brief summary of the post.

   # Introduction

   This is the content of my blog post.

   $$ f(x) = x^2 + 2x + 1 $$

   Here is a code snippet:

   ```python
   import numpy as np
   def my_function():
       return np.linspace(0, 1, 10)
   ```

   ```

3. Save the file. Pelican will process it and generate a static page.

---

## Deploying to GitHub Pages

### Automatic Deployment

This project is configured to deploy to **GitHub Pages** automatically using **GitHub Actions**. Every time you push to the `main` branch, the GitHub Action workflow will:

1. Build the static site using Pelican.
2. Deploy the generated files to the `gh-pages` branch.
3. The blog will be publicly available at:

   ```
   https://yourusername.github.io/your-repository-name/
   ```

### Manual Deployment (Optional)

If you'd prefer to deploy the site manually instead of using GitHub Actions, you can build the site locally and push the output to the `gh-pages` branch:

1. **Build the site locally**:

   ```bash
   pelican content
   ```

2. **Switch to the `gh-pages` branch**:

   ```bash
   git checkout --orphan gh-pages
   git rm -rf .
   ```

3. **Add the generated output**:

   ```bash
   cp -r output/* .
   git add .
   git commit -m "Deploying blog to GitHub Pages"
   git push origin gh-pages
   ```

---

## Customizing the Blog

### Changing the Theme

Pelican supports various themes. To change the theme, modify the `THEME` variable in `pelicanconf.py`:

```python
THEME = "path/to/your/theme"
```

You can browse available themes [here](https://github.com/getpelican/pelican-themes).

### Adding Plugins

Pelican supports a range of plugins for additional functionality. For example, you can enable the `render_math` plugin in `pelicanconf.py` to render LaTeX equations:

```python
PLUGINS = ['render_math']
```

You can also install additional plugins via `pip` if required.

---

## Contributing

Feel free to fork the repository and create pull requests. Here are some ways you can contribute:

- Write blog posts or tutorials related to machine learning.
- Add new themes or improve the current theme.
- Implement new features or fix bugs.

---

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **Pelican**: A static site generator used to build this blog.
- **MathJax**: Used for rendering LaTeX equations.
- **GitHub Pages**: Free hosting service for static sites provided by GitHub.
```

---

### Key Sections in the README:

1. **Project Overview**: Describes what the project is about, its purpose, and features.
2. **Getting Started**: Instructions for setting up the blog locally, including prerequisites, installation, and local development setup.
3. **Writing Posts**: How to create new blog posts using Markdown and how to include LaTeX math equations and code snippets.
4. **Deploying**: Instructions on how the site is automatically deployed using **GitHub Actions** and how to manually deploy if necessary.
5. **Customization**: Information on how to change the theme and use plugins for additional functionality.
6. **Contributing**: Encourages contributions to the project, whether through writing posts or code.
7. **License and Acknowledgments**: Legal information and credits.

---

