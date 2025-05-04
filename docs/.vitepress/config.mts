import { defineConfig } from "vitepress";
import { cliCommands } from "./cliCommands";
import { resources } from "./resources";

// https://vitepress.dev/reference/site-config
export default defineConfig({
    appearance: "dark",
    base: "/structix/",
    title: "Structix",
    description:
        "A CLI tool to scaffold modern backend architectures and integrate DevOps workflows effortlessly.",
    themeConfig: {
        logo: {
            light: "/logo-light.png",
            dark: "/logo-dark.png",
        },
        // https://vitepress.dev/reference/default-theme-config
        search: {
            provider: "local",
            options: {
                miniSearch: {
                    options: {
                        tokenize: (text: string) => text.split(/\s+/),
                    },
                    searchOptions: {
                        fuzzy: 0.2,
                        prefix: true,
                        boost: {
                            title: 4,
                            text: 2,
                            headings: 3,
                        },
                    },
                },
            },
        },
        nav: [
            { text: "Home", link: "/" },
            {
                text: "Docs",
                link: "/docs/getting-started/introduction",
                activeMatch: "^/docs/",
            },
        ],
        sidebar: [
            {
                text: "Documentation",
                items: [
                    {
                        text: "Getting Started",
                        collapsed: false,
                        items: [
                            {
                                text: "Introduction",
                                link: "/docs/getting-started/introduction",
                            },
                            {
                                text: "Requirements",
                                link: "/docs/getting-started/requirements",
                            },
                            {
                                text: "How to Install",
                                link: "/docs/getting-started/how-to-install",
                            },
                        ],
                    },
                    {
                        text: "Architectures",
                        collapsed: false,
                        items: [
                            {
                                text: "Overview",
                                link: "/docs/architectures/overview",
                            },
                            {
                                text: "Monolith Modular",
                                link: "/docs/architectures/monolith-modular",
                            },
                            {
                                text: "Domain-Driven Design",
                                link: "/docs/architectures/domain-driven-design",
                            },
                            {
                                text: "Hexagonal Architecture",
                                link: "/docs/architectures/hexagonal-architecture",
                            },
                            {
                                text: "DDD with Hexagonal Architecture",
                                link: "/docs/architectures/ddd-hexagonal",
                            },
                            {
                                text: "Microservices",
                                link: "/docs/architectures/microservices",
                            },
                        ],
                    },

                    {
                        text: "Tools",
                        collapsed: false,
                        items: [
                            {
                                text: "Overview",
                                link: "/docs/tools/overview",
                            },
                            {
                                text: "Prometheus",
                                link: "/docs/tools/prometheus",
                            },
                            {
                                text: "Grafana",
                                link: "/docs/tools/grafana",
                            },
                            {
                                text: "AlertManager",
                                link: "/docs/tools/alertmanager",
                            },
                            {
                                text: "Jaeger",
                                link: "/docs/tools/jaeger",
                            },
                        ],
                    },
                    {
                        text: "CLI Commands",
                        collapsed: false,
                        items: [
                            {
                                text: "Overview",
                                link: "/docs/cli-commands/overview",
                            },
                            ...cliCommands,
                        ],
                    },
                    {
                        text: "Resources",
                        collapsed: false,
                        items: [
                            {
                                text: "Overview",
                                link: "/docs/resources/overview",
                            },
                            ...resources,
                        ],
                    },
                ],
            },
        ],
        socialLinks: [
            {
                icon: "github",
                link: "https://github.com/structix-cli/structix",
            },
        ],
    },
});
