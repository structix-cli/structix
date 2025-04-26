import { defineConfig } from "vitepress";

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
                        text: "CLI Commands",
                        collapsed: true,
                        items: [
                            { text: "Init", link: "/cli-commands/init" },
                            { text: "Config", link: "/cli-commands/config" },
                            {
                                text: "Add",
                                collapsed: true,
                                items: [
                                    {
                                        text: "Context",
                                        link: "/cli-commands/add/context",
                                    },
                                    {
                                        text: "Microservice",
                                        link: "/cli-commands/add/microservice",
                                    },
                                    {
                                        text: "Module",
                                        link: "/cli-commands/add/module",
                                    },
                                ],
                            },
                            {
                                text: "Ops",
                                collapsed: true,
                                items: [
                                    {
                                        text: "Init Cluster",
                                        link: "/cli-commands/ops/init/cluster",
                                    },
                                    {
                                        text: "Start Cluster",
                                        link: "/cli-commands/ops/start/cluster",
                                    },
                                    {
                                        text: "Stop Cluster",
                                        link: "/cli-commands/ops/stop/cluster",
                                    },
                                    {
                                        text: "Create Cluster",
                                        link: "/cli-commands/ops/create/cluster",
                                    },
                                    {
                                        text: "Destroy Cluster",
                                        link: "/cli-commands/ops/destroy/cluster",
                                    },
                                    {
                                        text: "Deploy",
                                        collapsed: true,
                                        items: [
                                            {
                                                text: "Deploy Microservice",
                                                link: "/cli-commands/ops/deploy/microservice",
                                            },
                                            {
                                                text: "Deploy Ingress",
                                                link: "/cli-commands/ops/deploy/ingress",
                                            },
                                            {
                                                text: "Deploy All",
                                                link: "/cli-commands/ops/deploy/all",
                                            },
                                        ],
                                    },
                                    {
                                        text: "Expose Cluster",
                                        link: "/cli-commands/ops/expose/cluster",
                                    },
                                    {
                                        text: "Add (Ops)",
                                        collapsed: true,
                                        items: [
                                            {
                                                text: "Add DB",
                                                link: "/cli-commands/ops/add/db",
                                            },
                                            {
                                                text: "Add Microservice",
                                                link: "/cli-commands/ops/add/microservice",
                                            },
                                            {
                                                text: "Add Ingress",
                                                link: "/cli-commands/ops/add/ingress",
                                            },
                                        ],
                                    },
                                    {
                                        text: "Remove",
                                        collapsed: true,
                                        items: [
                                            {
                                                text: "Remove Microservice",
                                                link: "/cli-commands/ops/remove/microservice",
                                            },
                                            {
                                                text: "Remove Cluster",
                                                link: "/cli-commands/ops/remove/cluster",
                                            },
                                        ],
                                    },
                                    {
                                        text: "Status",
                                        collapsed: true,
                                        items: [
                                            {
                                                text: "Status Helm",
                                                link: "/cli-commands/ops/status/helm",
                                            },
                                            {
                                                text: "Status Cluster",
                                                link: "/cli-commands/ops/status/cluster",
                                            },
                                        ],
                                    },
                                ],
                            },
                        ],
                    },
                ],
            },
        ],
        socialLinks: [
            { icon: "github", link: "https://github.com/brayandm/structix" },
        ],
    },
});
