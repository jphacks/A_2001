export default {
  // Global page headers (https://go.nuxtjs.dev/config-head)
  head: {
    title: 'SHIBAFU',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      {
        hid: 'description',
        name: 'description',
        content:
          "SHIBAFU(Status Heatmap and Illustration of Brah brah Activities For User's motivation)は、経験値システムやヒートマップを導入した、ブラウザ上で動作するタスク管理アプリです。設定したタスクをこなすことで経験値がたまり、ゲーム的な体験を提供し、モチベーションアップに繋げることができます。",
      },
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
  },

  server: {
    port: 3000,
    host: '0.0.0.0',
  },

  router: {
    linkActiveClass: 'active open',
  },

  // Global CSS (https://go.nuxtjs.dev/config-css)
  css: [
    /* Import Font Awesome Icons Set */
    '~/node_modules/flag-icon-css/css/flag-icon.min.css',
    /* Import Font Awesome Icons Set */
    '~/node_modules/font-awesome/css/font-awesome.min.css',
    /* Import Simple Line Icons Set */
    '~/node_modules/simple-line-icons/css/simple-line-icons.css',
    /* Import Bootstrap Vue Styles */
    '~/node_modules/bootstrap-vue/dist/bootstrap-vue.css',
    /* Import Core SCSS */
    { src: '~/assets/scss/style.scss', lang: 'scss' },
  ],

  // Plugins to run before rendering page (https://go.nuxtjs.dev/config-plugins)
  plugins: [
    { src: '~/plugins/localStorage.js', ssr: false },
    { src: '~/plugins/firebase.js' },
    '~/plugins/axios',
  ],

  // Auto import components (https://go.nuxtjs.dev/config-components)
  components: true,

  // Modules for dev and build (recommended) (https://go.nuxtjs.dev/config-modules)
  buildModules: [
    // https://go.nuxtjs.dev/typescript
    '@nuxt/typescript-build',
  ],

  // Modules (https://go.nuxtjs.dev/config-modules)
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    // https://go.nuxtjs.dev/pwa
    '@nuxtjs/pwa',
    'bootstrap-vue/nuxt',
  ],

  styleResources: {
    scss: './assets/scss/style.scss',
  },

  // Axios module configuration (https://go.nuxtjs.dev/config-axios)
  axios: {},

  // Build Configuration (https://go.nuxtjs.dev/config-build)
  build: {},
};
