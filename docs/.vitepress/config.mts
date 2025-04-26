import { defineConfig } from "vitepress";
import { sidebar } from "./sidebar";

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
        sidebar,
        socialLinks: [
            { icon: "github", link: "https://github.com/brayandm/structix" },
        ],
    },
});
