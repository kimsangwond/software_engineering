<template>
  <div class="container-fluid">
    <div class="row-fluid">
      <Header/>
      <div class="contents">
        <nuxt/>
      </div>
    </div>
  </div>
</template>

<script>
  import Header from '@/components/Header'
  
  export default {
    components: {
      Header
    },
    head() {
      return {
        title: 'Fact Finder'
      }
    }
  }
</script>

<style>
  body {
    background: url('../assets/background-image.jpeg') no-repeat center center fixed;
    -webkit-background-size: cover;
    -moz-background-size: cover;
    background-size: cover;
    -o-background-size: cover;
  }
  .container-fluid {
    padding-right:0;
    padding-left:0;
    margin-right:auto;
    margin-left:auto
  }
</style>