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
                    { text: "CLI Commands", link: "/cli-commands" },
                ],
            },
        ],

        socialLinks: [
            { icon: "github", link: "https://github.com/brayandm/structix" },
        ],
    },
});
