import { defaultTheme } from '@vuepress/theme-default'
import { viteBundler } from '@vuepress/bundler-vite'
import { markdownMathPlugin } from '@vuepress/plugin-markdown-math'
import { slimsearchPlugin } from '@vuepress/plugin-slimsearch'
import markdownItFootnote from 'markdown-it-footnote'
import { groups } from './curriculum.js'

export default {
  lang: 'en-US',
  title: 'General Relativity',
  description: 'A documentation site about General Relativity',
  base: '/',

  bundler: viteBundler(),

  theme: defaultTheme({
    navbar: [
      { text: 'Home', link: '/' },
      ...groups.map(group => ({
        text: group.name,
        children: group.items.map(item => ({ text: item.title, link: item.link })),
      })),
    ],
    // Keep the ten main chapters together for previous/next navigation.
    sidebar: [
      ...groups.slice(0, 3).flatMap(group => group.items.map(item => ({
        text: `${item.number}. ${item.title}`, link: item.link,
      }))),
      {
        text: 'Supporting Chapters',
        children: groups[3].items.map(item => ({ text: item.title, link: item.link })),
      },
    ],
  }),

  plugins: [
    // Match Phyz and render mathematics without asynchronous MathJax font loading.
    markdownMathPlugin({ type: 'katex', output: 'html' }),
    slimsearchPlugin({
      indexContent: true,
      suggestion: false,
    }),
  ],

  extendsMarkdown(md) {
    md.use(markdownItFootnote)
  },
}
