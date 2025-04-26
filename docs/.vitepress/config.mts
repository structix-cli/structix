import { defineConfig } from "vitepress";
import { cliCommands } from "./cliCommands";

// https://vitepress.dev/reference/site-config
export default defineConfig({
    title: "Structix",
    description:
        "A CLI tool to scaffold modern backend architectures and integrate DevOps workflows effortlessly.",
    themeConfig: {
        // https://vitepress.dev/reference/default-theme-config
        nav: [
            { text: "Home", link: "/" },
            { text: "Getting Started", link: "/getting-started/introduction" },
            { text: "Docs", link: "/cli-commands" },
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
                                link: "/getting-started/introduction",
                            },
                            {
                                text: "Requirements",
                                link: "/getting-started/requirements",
                            },
                            {
                                text: "How to Install",
                                link: "/getting-started/how-to-install",
                            },
                        ],
                    },
                    {
                        text: "Architectures",
                        collapsed: false,
                        items: [
                            {
                                text: "Monolith Modular",
                                link: "/architectures/monolith-modular",
                            },
                            {
                                text: "Domain-Driven Design",
                                link: "/architectures/domain-driven-design",
                            },
                            {
                                text: "Hexagonal Architecture",
                                link: "/architectures/hexagonal-architecture",
                            },
                            {
                                text: "DDD with Hexagonal Architecture",
                                link: "/architectures/ddd-hexagonal",
                            },
                            {
                                text: "Microservices",
                                link: "/architectures/microservices",
                            },
                        ],
                    },
                    {
                        text: "CLI Commands",
                        collapsed: false,
                        items: cliCommands,
                    },
                ],
            },
        ],
        socialLinks: [
            { icon: "github", link: "https://github.com/brayandm/structix" },
        ],
    },
});
