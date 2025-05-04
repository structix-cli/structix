# Overview

Modern Kubernetes environments require robust visibility into the state and performance of workloads, nodes, and the cluster itself. To achieve this, various observability tools can be integrated directly into the cluster.

These tools enable the collection, storage, visualization, and alerting of key metrics and events across the system, making it easier for teams to operate applications reliably and at scale.

## Why Observability Matters

-   **Tracking**: Continuously monitor resource usage such as CPU, memory, and I/O per pod or node
-   **Visualization**: Use dashboards to analyze data trends over time and support decision-making
-   **Alerting**: Trigger notifications when anomalies or threshold breaches are detected
-   **Debugging**: Gain insights to troubleshoot issues quickly and effectively
-   **Capacity Planning**: Understand patterns to plan for scaling and resource allocation

Kubernetes natively exposes a wide range of system and application metrics. When paired with the right observability stack, this unlocks a powerful foundation for proactive operations and system health monitoring.

The following documents will introduce key tools used to achieve this: metric collection, visualization, and alerting.
