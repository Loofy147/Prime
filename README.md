# AI Prime

AI Prime is an advanced, AI-powered SaaS platform designed to deliver domain-tuned AI agents through a secure, scalable, and resilient API and dashboard. The platform is architected to be a robust, enterprise-grade solution from the ground up.

## Architecture

The AI Prime platform is built on a modern, cloud-native architecture that leverages a microservices-based approach for maximum flexibility and scalability.

### Core Components:

*   **Backend:** A high-performance backend built with **Python** and **FastAPI**, providing a robust and efficient API for serving AI models.
*   **Database:** A **PostgreSQL** database (provisioned as a high-availability AWS RDS Aurora cluster) for persistent data storage, including all provenance data for AI model responses.
*   **Cache:** A **Redis** in-memory data store (provisioned as AWS ElastiCache) for caching frequently accessed data and improving response times.
*   **Containerization:** The entire application is containerized using **Docker**, ensuring consistency across development, testing, and production environments.
*   **Orchestration:** The production environment is orchestrated using **AWS ECS with Fargate**, providing a serverless, scalable, and resilient platform for running the application containers.

### Advanced AI Capabilities (Roadmap):

The platform is designed to evolve with the following advanced AI capabilities, as outlined in the strategic roadmap:

*   **Mixture of Experts (MoE):** To efficiently serve a diverse range of specialized AI models.
*   **Retrieval-Augmented Generation (RAG):** To ground AI responses in factual, up-to-date information and reduce hallucinations.
*   **Multimodality:** To extend the platform's capabilities beyond text to include images, audio, and other data formats.

## Infrastructure

The entire infrastructure for the AI Prime platform is managed as code using **Terraform**, ensuring a repeatable, version-controlled, and automated provisioning process.

### Key Infrastructure Components (AWS):

*   **VPC:** A custom Virtual Private Cloud (VPC) with public and private subnets across multiple availability zones for a secure and isolated network environment.
*   **ECS with Fargate:** A serverless container orchestration platform for running the application containers without the need to manage servers.
*   **RDS Aurora (PostgreSQL):** A fully managed, high-availability relational database for persistent data storage.
*   **ElastiCache (Redis):** A fully managed in-memory data store for caching.
*   **Application Load Balancer:** A highly available load balancer to distribute traffic across the application containers and provide a single entry point to the API.
*   **Secrets Manager:** For securely storing and managing sensitive information like database credentials.
*   **ECR (Elastic Container Registry):** A fully managed container registry for storing the application's Docker images.

### Managing the Infrastructure

To provision or update the infrastructure, you will need to have Terraform installed and configured with the appropriate AWS credentials.

**Note:** Before applying the Terraform configuration, you will need to create a `terraform.tfvars` file and provide values for the `acm_certificate_arn` and `image_tag` variables. You can use the `terraform.tfvars.example` file as a template.

1.  **Navigate to the Terraform directory:**
    ```bash
    cd infra/terraform
    ```

2.  **Initialize Terraform:**
    ```bash
    terraform init
    ```

3.  **Create a plan:**
    ```bash
    terraform plan
    ```

4.  **Apply the plan:**
    ```bash
    terraform apply
    ```

## Getting Started

To get started with developing the AI Prime platform, you will need to have Docker and Docker Compose installed.

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd ai-prime
    ```

3.  **Start the development environment:**
    ```bash
    docker-compose -f prod_docker-compose.yml up
    ```

This will start the API server, the database, and the Redis cache in a local Docker environment. The API will be available at `http://localhost:8000`.
