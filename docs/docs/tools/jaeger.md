# Jaeger

## What is Jaeger?

Jaeger is an open-source distributed tracing system used for monitoring and troubleshooting transactions in complex microservice architectures. It helps track the flow of requests across multiple services.

## What is Jaeger used for?

-   Tracing requests as they travel through different services
-   Identifying performance bottlenecks and latency issues
-   Understanding service dependencies and execution flows
-   Analyzing root causes of failures in distributed systems
-   Improving observability in microservice-based applications

## How is Jaeger integrated?

Jaeger works seamlessly with **OpenTelemetry**, which is used as the standard client for instrumentation. Applications instrumented with OpenTelemetry SDKs or agents export trace data that is collected and visualized by Jaeger. This setup enables consistent and vendor-neutral tracing across the entire stack.
