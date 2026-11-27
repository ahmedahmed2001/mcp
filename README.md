# MCP

## Description

Repository for the MCP project. It contains the source code, configuration files, and documentation necessary to build, test, and deploy the application.

## Structure

- `backend/` – server‑side code and APIs.
- `frontend/` – client‑side application.
- `services/` – auxiliary services and Docker configurations.
- `scripts/` – automation scripts for CI/CD.
- `tests/` – unit and integration test suites.
- `config/` – configuration files.
- `Dockerfile` – container definition.
- `package.json` – Node.js dependencies.
- `requirements.txt` – Python dependencies.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ahmedahmed2001/mcp.git
   ```
2. Install backend dependencies:
   ```bash
   cd mcp/backend
   pip install -r requirements.txt
   ```
3. Install frontend dependencies:
   ```bash
   cd ../frontend
   npm install
   ```

## Usage

- Run the backend:
  ```bash
  cd backend
  python main.py
  ```
- Run the frontend:
  ```bash
  cd frontend
  npm start
  ```

## Contributing

Contributions are welcome. Please follow the standard pull‑request workflow and ensure that all tests pass before merging.

## License

This project is licensed under the MIT License.