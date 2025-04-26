---
# https://vitepress.dev/reference/default-theme-home-page
layout: home

hero:
    name: "Structix"
    text: "A CLI tool to scaffold modern backend architectures and integrate DevOps workflows effortlessly."
    tagline: "Speed up your backend and DevOps projects with clean, production-ready templates."
    actions:
        - theme: brand
          text: Get Started
          link: /getting-started/introduction
        - theme: alt
          text: CLI Commands
          link: /cli-commands/overview

features:
    - title: Architecture Templates
      details: Quickly scaffold monoliths, microservices, and DDD-based projects following Hexagonal and CQRS patterns.
    - title: DevOps Integration
      details: Generate Kubernetes, Helm, and Terraform setups automatically to streamline your infrastructure deployments.
    - title: Observability Built-in
      details: Add Prometheus and Grafana integrations out of the box to monitor and visualize your services effortlessly.
    - title: Database Flexibility
      details: Scaffold projects with support for PostgreSQL and MongoDB databases, ready for production environments.
    - title: Event-Driven Ready
      details: Integrate Kafka seamlessly into your architectures to enable event-driven communication between services.
    - title: Local & Cloud Environments
      details: Easily manage Minikube clusters for local development or create full Kubernetes clusters for production.
---
