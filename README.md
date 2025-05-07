# Streamlit Project Template

A modern Streamlit project template using GitHub templates and uv package manager for efficient Python development.

## Getting Started

### Forking the Template Repository

To create your own project based on this template, follow these steps:

1. **Navigate to the template repository**:
   - Go to [https://github.com/RutgersGRID/streamlit-template](https://github.com/RutgersGRID/streamlit-template) in your web browser

2. **Fork the repository**:
   - Click the "Fork" button in the top-right corner of the repository page
   - This creates a copy of the template in your own GitHub account

3. **Customize your fork (optional)**:
   - You can rename your repository by clicking on "Settings" in your forked repository
   - Under the "General" tab, you can update the repository name and description

4. **Clone your forked repository**:
   ```bash
   git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY-NAME.git
   cd YOUR-REPOSITORY-NAME
   ```
   Replace `YOUR-USERNAME` with your GitHub username and `YOUR-REPOSITORY-NAME` with the name of your repository

Alternatively, you can use the GitHub CLI to create a new repository from the template:

```bash
gh repo create YOUR-REPOSITORY-NAME --template RutgersGRID/streamlit-template --public --clone
cd YOUR-REPOSITORY-NAME
```

After forking or creating from the template, you'll have a new repository with all the template files ready for your customization.

## Prerequisites

Before setting up your project, make sure you have the following installed:

- Python 3.12 or higher
- Git
- `uv` package manager:
  ```bash
  # Install uv
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```
  On Windows, you can install `uv` using pip:
  ```bash
  pip install uv
  ```

- (Optional) `pipx` for tool installation:
  ```bash
  # On macOS
  brew install pipx
  pipx ensurepath

  # On Windows
  python -m pip install --user pipx
  python -m pipx ensurepath
  ```

- (Optional) `pre-commit` for code quality checks:
  ```bash
  pipx install pre-commit
  ```

## Setting Up Your Development Environment

After cloning your repository, follow these steps to set up your development environment:

1. **Create and activate a virtual environment**:
   ```bash
   # Create a virtual environment using uv
   uv venv

   # Activate the virtual environment
   # On Windows:
   .venv\Scripts\activate

   # On macOS/Linux:
   source .venv/bin/activate
   ```

2. **Install dependencies**:
   ```bash
   # Install all project dependencies
   uv sync
   ```

3. **(Optional) Set up pre-commit hooks**:
   ```bash
   # If you installed pre-commit
   pre-commit install
   ```

4. **Run the Streamlit app**:
   ```bash
   # Run the application using streamlit
   streamlit run src/uoes_learning_objectives/app.py
   ```
   The app will be accessible at http://localhost:8501 by default.

   Alternatively, you can use uv to run the application:
   ```bash
   uv run streamlit run src/uoes_learning_objectives/app.py
   ```

## Project Structure

The template follows a standard Python project structure:

```
.
├── README.md                      # Project overview (this file)
├── pyproject.toml                 # Python project metadata and dependencies
├── Dockerfile                     # For containerizing the application
├── docker-compose.yml             # For running the application in Docker
├── pre-commit-config.yml          # Pre-commit hooks configuration
└── src/
    ├── tests/                     # Test directory
    │   ├── __init__.py            
    │   ├── conftest.py            # Test configurations and fixtures
    │   └── test_utils.py          # Example tests
    └── streamlit_template/        # Main package (rename to your project name)
        ├── __init__.py            # Package initialization
        ├── app.py                 # Main Streamlit application entry point
        ├── utils.py               # Utility functions
        └── py.typed               # Marker file for type information
```

When adapting this template to your own project, you should:

1. Rename the `streamlit_template` directory to match your project name
2. Update import paths in your code to reflect the new package name
3. Update the package name in `pyproject.toml`

## Dependency Management with uv

This project uses the [uv](https://github.com/astral-sh/uv) package manager for faster, more reliable Python dependency management.

### Adding Dependencies

```bash
# Add a package
uv add streamlit

# Add multiple packages
uv add pandas numpy matplotlib

# Add a package with specific version
uv add pandas==2.2.0

# Add a development dependency
uv add --dev pytest
```

### Syncing Dependencies

To install all dependencies defined in `pyproject.toml`:

```bash
uv sync
```

### Updating Dependencies

To update all dependencies to their latest versions:

```bash
uv pip compile --upgrade
uv sync
```

## Development Workflow

### Code Quality and Testing

This template comes with tools for maintaining code quality and testing your application:

1. **Running Tests**:
   ```bash
   # Run all tests
   pytest

   # Run tests with coverage report
   pytest --cov=uoes_learning_objectives
   ```

2. **Code Quality Checks with Pre-commit**:
   If you've set up pre-commit hooks, they'll run automatically when you commit changes. You can also run them manually:
   ```bash
   pre-commit run --all-files
   ```

   Pre-commit hooks included in this template:
   - trailing-whitespace removal
   - end-of-file-fixer
   - yaml validation
   - python formatting with black
   - python linting with ruff

### Git Workflow

We recommend following this git workflow for your development process:

1. **Create a feature branch for your changes**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes and commit them**:
   ```bash
   # Stage your changes
   git add .

   # Commit (this will trigger pre-commit hooks if installed)
   git commit -m "type: descriptive message"
   ```
   
   Recommended commit message types:
   - `feat`: new features
   - `fix`: bug fixes
   - `docs`: documentation changes
   - `style`: formatting, missing semi colons, etc.
   - `refactor`: code restructuring
   - `test`: adding tests
   - `chore`: maintenance tasks

3. **Push your changes and create a pull request**:
   ```bash
   git push origin feature/your-feature-name
   ```
   
   Then create a pull request on GitHub to merge your changes.

## Deployment Options

### Running Locally

For local development and testing:
```bash
streamlit run src/uoes_learning_objectives/app.py
```

### Using Docker

The template includes a Dockerfile and docker-compose.yml for containerized deployment:

```bash
# Build and run with Docker Compose
docker-compose up --build
```

This will make the application available at http://localhost:8501.

### Deploying to Streamlit Cloud

1. Push your code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your GitHub repository
4. Select your main file: `src/uoes_learning_objectives/app.py`

## Customizing the Template

### Renaming the Project

To rename the project to match your needs:

1. Rename the source directory:
   ```bash
   # Rename the directory
   mv src/streamlit_template src/your_project_name
   ```

2. Update imports in your Python files
3. Update the project name in `pyproject.toml`
4. Update app paths in this README

### Adding Your Own Components

The template provides a minimal structure that you can extend:

1. Add new Python modules in the main package directory
2. Create additional Streamlit pages in separate `.py` files
3. Add tests for your new components in the `tests` directory

## Troubleshooting

### Common Issues

1. **Package not found errors**:
   - Make sure your virtual environment is activated
   - Verify you've installed all dependencies with `uv sync`

2. **Pre-commit failures**:
   - Let pre-commit fix the issues automatically
   - Commit the changes after fixes are applied

3. **Streamlit connection errors**:
   - Check if another Streamlit app is running on port 8501
   - Specify a different port if needed: `streamlit run --server.port 8502 src/streamlit_template/app.py` 
   - Remember to replace `streamlit_template` with `your_project_name`

## License

This project is licensed under the MIT License.