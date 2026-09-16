import { defaultTheme } from '@vuepress/theme-default'
import { viteBundler } from '@vuepress/bundler-vite'
import { markdownMathPlugin } from '@vuepress/plugin-markdown-math'
import { slimsearchPlugin } from '@vuepress/plugin-slimsearch'
import markdownItFootnote from 'markdown-it-footnote'

export default {
  lang: 'en-US',
  title: 'General Relativity',
  description: 'A documentation site about General Relativity',
  base: '/',

  bundler: viteBundler(),

  theme: defaultTheme({
    navbar: [
      { text: 'Home', link: '/' },
    ],
    sidebar: [],
  }),

  plugins: [
    markdownMathPlugin({ type: 'mathjax', output: 'svg' }),
    slimsearchPlugin({
      indexContent: true,
      suggestion: false,
    }),
  ],

  extendsMarkdown(md) {
    md.use(markdownItFootnote)
  },
}
