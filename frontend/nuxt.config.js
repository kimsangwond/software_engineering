module.exports = {
  modules: [
    'bootstrap-vue/nuxt'
  ],
  plugins: [
    "@/plugins/fontawesome.js",
    "@/plugins/bootstrap.js"
  ],
  css: [
    "@/node_modules/bootstrap/dist/css/bootstrap.min.css"
  ],
  build: {
    /*
    ** Run ESLint on save
    */
    extend (config, { isDev, isClient }) {
      if (isDev && isClient) {
        config.module.rules.push({
          enforce: 'pre',
          test: /\.(js|vue)$/,
          loader: 'eslint-loader',
          exclude: /(node_modules)/
        })
      }
    },
    vendor: ["axios"]
  }
}

