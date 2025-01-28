# Mynews Crew

Welcome to the Mynews Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Prerequisites

- Python >=3.10 <3.13
- OpenAI API key
  
## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/mynews-crew.git
cd mynews-crew
```

2. Install project dependencies:
```bash
crewai install
```

1. Set up environment variables:
   - Create a `.env` file in the root directory
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

## Configuration

The project uses YAML files for configuration:

- `src/mynews/config/agents.yaml`: Define AI agents and their properties
- `src/mynews/config/tasks.yaml`: Define tasks for the agents to perform
- `src/mynews/crew.py`: Customize logic, tools, and arguments
- `src/mynews/main.py`: Configure custom inputs for agents and tasks

## Running the Project

1. From the project root directory, run:
```bash
crewai run
```

1. The system will generate a "News Article in the folder "news" file containing the AI agents' research on LLMs.

## Project Structure

```
mynews/
├── src/
│   └── mynews/
│       ├── config/
│       │   ├── agents.yaml
│       │   └── tasks.yaml
│       ├── crew.py
│       └── main.py
├── .env
└── README.md
```

## Output

The default configuration will generate a `News Article.md` file in the "news directory containing research on specific topic. You can customize the output by modifying the task configurations in `tasks.yaml`.

## Support

Need help? Here are some resources:
- [Official Documentation](https://docs.crewai.com)
- [GitHub Repository](https://github.com/joaomdmoura/crewai)
- [Discord Community](https://discord.com/invite/X4JWnZnxPb)
- [Documentation Chat](https://chatg.pt/DWjSBZn)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Understanding Your Crew

The myNews Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.
