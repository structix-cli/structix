from typing import Literal

ArchitectureType = Literal["Monolith", "Microservices"]
StackType = Literal["NestJS"]
ClusterProviderType = Literal[
    "minikube",
    "kubeconfig",
]
