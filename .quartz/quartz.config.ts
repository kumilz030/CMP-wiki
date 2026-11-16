import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

// CMP-wiki 網站設定；內容由 build.sh 從 wiki/ 和 index.md 複製進來。顏色與字體見 DESIGN.md
const config: QuartzConfig = {
  configuration: {
    pageTitle: "CMP-wiki",
    pageTitleSuffix: " · CMP-wiki",
    enableSPA: true,
    enablePopovers: true,
    analytics: null,
    locale: "zh-TW",
    baseUrl: "kumilz030.github.io/CMP-wiki",
    ignorePatterns: [".obsidian", "**/*.base", "**/.gitkeep"],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Noto Sans TC",
        body: "Noto Sans TC",
        code: "JetBrains Mono",
      },
      colors: {
        lightMode: {
          light: "#fbfaf7",
          lightgray: "#e6e4df",
          gray: "#8f8a82",
          darkgray: "#3f3d39",
          dark: "#1f1e1c",
          secondary: "#2f5d8a",
          tertiary: "#c0793a",
          highlight: "rgba(47, 93, 138, 0.10)",
          textHighlight: "#f5d76e88",
        },
        darkMode: {
          light: "#15171a",
          lightgray: "#2c3036",
          gray: "#7a808a",
          darkgray: "#d6d8dc",
          dark: "#eceef1",
          secondary: "#8db4dc",
          tertiary: "#e0a36b",
          highlight: "rgba(141, 180, 220, 0.12)",
          textHighlight: "#8a6d1088",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: false,
        enableRSS: false,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
    ],
  },
}

export default config
