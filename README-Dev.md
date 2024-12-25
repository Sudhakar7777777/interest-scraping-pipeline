### **Scraper Project - Developer Guide**

**Overview**

This project scrapes interest rate data from a website, processes the data, and stores it in an SQLite database. The system is containerized using Docker, with Airflow used for orchestration, Prometheus for monitoring, and Grafana for visualization.

This guide will help you set up the development environment, run the project locally, and understand the architecture and usage.

* * * * *

### **Prerequisites**

Before setting up the environment, make sure you have the following installed:

1.  **Docker**: Required for running the services in containers.

    -   Download Docker: https://www.docker.com/get-started
2.  **Miniconda** (Optional but recommended): A lightweight Python environment manager to manage dependencies.

    -   Install Miniconda: https://docs.conda.io/en/latest/miniconda.html
3.  **Git**: For cloning the repository and version control.

    -   Install Git: <https://git-scm.com/>

* * * * *

### **Install Dependencies**

#### **Install via Miniconda (Recommended)**

Miniconda is a lightweight Python package manager that helps you manage dependencies and Python environments. Here's how to set up the project using Miniconda:

1.  **Install Miniconda** (if not already installed).

2.  **Create a new conda environment** for the project:

    From the project root directory, run the following command to create and activate a new environment:

    ```lua
    conda create --name scraper-env python=3.9
    conda activate scraper-env
    ```

3.  **Install dependencies using `conda` and `pip`**:

    After activating the environment, install the necessary dependencies. Run the following commands:

    First, install the global dependencies:

    ```bash
    pip install -r requirements.txt
    ```

    Then install dependencies for the **scraper** and **Airflow**:

    ```bash
    pip install -r scraper/requirements.txt
    pip install -r airflow/requirements.txt
    ```

4.  **Verify the installation**:

    To verify everything is set up correctly, check the Python version and installed packages:

    ```bash
    python --version  # Should show Python 3.9 or greater
    conda list        # Shows installed packages in the environment
    ```

* * * * *

#### **Install via `pip` (Alternative)**

If you prefer not to use Miniconda, you can set up the environment using `pip`:

1.  **Create and activate a virtual environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

2.  **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    pip install -r scraper/requirements.txt
    pip install -r airflow/requirements.txt
    ```

* * * * *

### **Running the Project Locally**

The project is containerized using Docker. To get the system up and running, use Docker Compose to build and start all the services (Airflow, Scraper, Prometheus, Alertmanager, and Grafana):

#### **Start the Containers**

Run the following command to build and start all services:

```css
docker-compose up --build
```

This will start the following services:

-   **Airflow Web UI** on `http://localhost:8080`
-   **Prometheus UI** on `http://localhost:9090`
-   **Grafana UI** on `http://localhost:3000`
-   **Scraper service** running in the background

#### **Airflow Web UI**

Once the containers are up, you can access the **Airflow Web UI** at `http://localhost:8080`. You can monitor the scraping tasks, check logs, and trigger DAG runs manually from here.

-   **Default Credentials**:
    -   Username: `airflow`
    -   Password: `airflow`

#### **Prometheus**

Prometheus is used to monitor metrics for Airflow, the scraper, and itself. You can access the **Prometheus Web UI** at `http://localhost:9090`.

Here you can query the metrics exposed by your services. For example, to check the runtime of the scraper:

```bash
scraper_runtime_seconds
```

#### **Grafana**

Grafana is used to visualize metrics collected by Prometheus. You can access the **Grafana Web UI** at `http://localhost:3000`.

-   **Default Credentials**:
    -   Username: `admin`
    -   Password: `admin`

In Grafana, you can add Prometheus as a data source and create dashboards to visualize metrics such as scraper runtime, task failures in Airflow, etc.

#### **Scraper Logs**

The scraper logs are available in the `logs/` directory of the project. You can also view logs through Docker's log commands for the `scraper` container:

```bash
docker logs scraper
```

* * * * *

### **Testing**

#### **Unit Tests**

We use **pytest** for unit testing. There are tests for the scraper, Airflow DAGs, Prometheus metrics, and configuration files.

-   **Tests for the scraper** are located in `tests/test_scraper.py`.
-   **Tests for Airflow DAGs** are in `tests/test_airflow.py`.
-   **Tests for Prometheus metrics** are in `tests/test_metrics.py`.
-   **Tests for configuration files** are in `tests/test_config.py`.

#### **Running Tests Locally**

To run all the tests locally:

1.  Ensure that your environment is set up with the necessary dependencies (see **Install Dependencies**).

2.  Run the tests using `pytest`:

```bash
pytest tests/
```

This will run all the tests and provide output on success or failure.

* * * * *

### **CI/CD Integration**

#### **GitHub Actions**

This project integrates with **GitHub Actions** for continuous integration and continuous delivery (CI/CD). Every time you push changes to the repository, GitHub Actions will automatically run the tests and build the Docker containers.

The GitHub Actions configuration is located in `.github/workflows/ci.yml`. It includes steps for:

1.  Installing dependencies
2.  Running unit tests
3.  Building Docker containers
4.  Starting Docker containers and running tests in the containers

* * * * *

### **Project Structure**

Here's a breakdown of the project's directory structure:

```graphql
.
├── airflow/                    # Airflow DAGs and configurations
├── db/                         # SQLite database to store data
├── scraper/                    # Scraper logic and configurations
├── prometheus/                 # Prometheus, Alertmanager, and Grafana configs
├── config/                     # Configuration files for Airflow, Scraper, and Prometheus
├── tests/                      # Unit tests for scraper, Airflow, metrics, and configurations
├── docker-compose.yml          # Docker Compose setup to run services
├── .gitignore                  # Git ignore file
├── .dockerignore               # Docker ignore file
├── requirements.txt            # Global project dependencies
├── README.md                   # Project documentation
└── logs/                       # Logs from all services`
```

* * * * *

### **How to Contribute**

We welcome contributions to improve the project! Here's how you can contribute:

1.  **Fork the repository** and clone it to your local machine.
2.  **Create a new branch** for your changes:

```bash
git checkout -b feature/my-new-feature
```

3.  **Make your changes** and write tests if applicable.
4.  **Commit your changes**:

```bash
git commit -m "Add new feature"
```

5.  **Push your changes** to your fork:

```bash
git push origin feature/my-new-feature
```

6.  **Create a pull request** from your fork to the main repository.

* * * * *

### **Contact**

For any questions or issues related to this project, please contact the project maintainer:

-   **Email**: `developer@company.com`
-   **GitHub Issues**: You can raise issues directly on the [GitHub Issues page](https://github.com/yourusername/your-repository/issues).

* * * * *

Thank you for contributing to this project! We hope this guide helps you get started with setting up, developing, and testing this system.