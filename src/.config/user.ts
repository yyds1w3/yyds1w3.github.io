import type { UserConfig } from '~/types'

export const userConfig: Partial<UserConfig> = {
  // 1. 网站基础信息
  site: {
    title: 'Qingw の Blog',    // 你的博客大标题
    subtitle: '格物致知',  // 副标题，可以写学校或格言
    author: 'Qingw',          // 你的名字
    description: 'ACM', // SEO 描述
    website: 'https://yyds1w3.xyz', // 你的实际域名（上线后改） 
    pageSize: 10, // 首页显示多少篇文章
    
    // 2. 社交链接
    socialLinks: [
      {
        name: 'github',
        href: 'https://github.com/yyds1w3',
      },
      {
        name: 'rss',
        href: '/atom.xml',
      },
    ],

    // 3. 导航栏 (保持默认即可，或者加一个 'Friends')
    navLinks: [
      { name: 'Posts', href: '/' },
      { name: 'Archive', href: '/archive' },
      { name: 'Categories', href: '/categories' },
      { name: 'About', href: '/about' },
      { name: 'Friend', href: '/friend'}
    ],
    
    // 底部文字
    footer: [
      '© %year <a target="_blank" href="%website">%author</a>',
      'Powered by <a target="_blank" href="https://astro.build/">Astro</a>',
    ],
  },

  // 4. 外观设置
  appearance: {
    theme: 'system', // 跟随系统自动切换深色/浅色
    locale: 'en-us', // 强制中文
    // 这里的颜色是主题默认的，你可以改 hex 值来换皮肤
    colorsLight: {
      primary: '#2e405b',
      background: '#ffffff',
    },
    colorsDark: {
      primary: '#FFFFFF',
      background: '#050404ff',
    },
  },

  // 5. 开启数学公式 (重要！)
  latex: {
    katex: true, // 把 false 改成 true，你的公式才能显示！
  },
}