import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"

// components shared across all pages
export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [Component.MobileOnly(Component.Explorer({
    mapFn: (node) => {
      // dont change name of root node
      if (node.depth > 0) {
        // set emoji for file/folder
        if (node.file) {
          node.displayName = "📄 " + node.displayName
        } else {
          node.displayName = "📁 " + node.displayName
        }
      }
    },
  }))],
  afterBody: [],
  footer: Component.Footer({
    links: {
      Me: "https://zephyr-zdz.space",
      Thanks: "https://runjp.com",
    },
  }),
}

// components for pages that display a single page (e.g. a single note)
export const defaultContentPageLayout: PageLayout = {
  beforeBody: [
    Component.Breadcrumbs(),
    Component.ArticleTitle(),
    Component.ContentMeta(),
    Component.TagList(),
  ],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Search(),
    Component.Darkmode(),
    Component.DesktopOnly(Component.Explorer({
      mapFn: (node) => {
        // dont change name of root node
        if (node.depth > 0) {
          // set emoji for file/folder
          if (node.file) {
            node.displayName = "📄 " + node.displayName
          } else {
            node.displayName = "📁 " + node.displayName
          }
        }
      },
    })),
  ],
  right: [
    Component.Graph(),
    Component.DesktopOnly(Component.TableOfContents()),
    Component.Backlinks(),
  ],
}

// components for pages that display lists of pages  (e.g. tags or folders)
export const defaultListPageLayout: PageLayout = {
  beforeBody: [Component.Breadcrumbs(), Component.ArticleTitle(), Component.ContentMeta()],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Search(),
    Component.Darkmode(),
    Component.DesktopOnly(Component.Explorer({
      mapFn: (node) => {
        // dont change name of root node
        if (node.depth > 0) {
          // set emoji for file/folder
          if (node.file) {
            node.displayName = "📄 " + node.displayName
          } else {
            node.displayName = "📁 " + node.displayName
          }
        }
      },
    })),
  ],
  right: [],
}
