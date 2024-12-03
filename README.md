# Kvitka Project

Kvitka Poloniny is a medical AI chatbot project designed to leverage the capabilities of advanced AI agents to streamline and assist in healthcare workflows, file management, and project organization. The project incorporates specialized GPT agents **Arti** and **Floya**, each tailored to support specific aspects of the development process.

## Project Overview

The goal of the Kvitka project is to build a robust medical AI chatbot that aids healthcare professionals and manages resources effectively. With the help of **GPT Agents** like Arti and Floya, this project is structured to provide an organized, efficient approach to AI development and implementation in healthcare.

## Repository Structure

This repository is organized to facilitate modular development and make it easy for contributors to navigate. Below is a summary of the main directory structure:

```plaintext
fAis/
├── kvitka/
│   ├── docs/          # Documentation files, including user guides and technical manuals
│   ├── src/           # Source code for the main application
│   │   ├── FloRT/     # Sub-project focused on GPT agents Arti and Floya
│   │   │   ├── floya/ # Files specific to the Floya agent
│   │   │   ├── arti/  # Files specific to the Arti agent
│   │   │   └── shared/# Shared resources between Floya and Arti
│   ├── tests/         # Testing scripts and resources
│   └── config/        # Configuration files and settings
```

### Main Directories

- **docs/**: Contains all project documentation, including user guides, technical specifications, and instructions for developers and users.
- **src/**: Houses the main application code, with dedicated subdirectories for the Arti and Floya agents, as well as shared resources.
- **tests/**: Contains test scripts and resources to ensure functionality and reliability.
- **config/**: Stores configuration files needed for project setup and deployment.

## GPT Agents

### Arti
**Arti** (https://chatgpt.com/g/g-a1yULBC7Y-artie) is a customized GPT agent designed to help manage the Kvitka project’s workflow, file organization, and architectural design. Arti assists with integrating API connections, automating workflows, and structuring project files for optimized collaboration. This agent plays a critical role in coordinating development efforts and maintaining the overall structure of the project.

### Floya
**Floya** (https://chatgpt.com/g/g-idyWhaIDG-floya) is another GPT agent specialized in supporting project tasks and file management. Floya is focused on enhancing productivity by streamlining scheduling, managing files, and helping organize resources within the Kvitka project. Together with Arti, Floya helps ensure that the project runs smoothly and remains well-organized.

### Shared Resources
The `shared/` directory under `src/FloRT` contains code and resources that are used by both Arti and Floya, such as common helper functions, data-processing scripts, and configuration files essential for their combined functionality.

## Getting Started

To get started with Kvitka, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/fais-world/kvitka.git
   cd kvitka
   ```

2. **Install Dependencies**:
   Ensure all necessary dependencies are installed as listed in `requirements.txt`.
   ```bash
   pip install -r requirements.txt
   ```

3. **Configuration**:
   Add any configuration files needed to the `config/` directory. Specific configuration instructions can be found in `config/README.md`.

4. **Running the Application**:
   Run the main application with:
   ```bash
   python src/main.py
   ```

5. **Testing**:
   Run test scripts located in the `tests/` directory to verify that the system functions as expected.
   ```bash
   pytest tests/
   ```

## Contributing

We welcome contributions! Please read `CONTRIBUTING.md` for guidelines on how to participate in this project.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact and Support

For questions or support, please open an issue on this repository, or reach out to the project maintainers.

