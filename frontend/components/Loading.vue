<template>
  <div v-if="isLoading" class="text-center">
    <b-button size="lg" variant="primary" disabled class="overlay-loading">
      <b-spinner type="grow"></b-spinner>
      검색중입니다!
    </b-button>
  </div>
</template>

<script>
  export default {
    data() {
      return { isLoading: false }
    },
    methods: {
      start() { this.isLoading = true },
      finish() { this.isLoading = false }
    }
  }
</script>

<style>
  .overlay-loading{
    position: absolute;
    top: 50%;
    left: 50%;
    font-size: 30px;
    transform: translate(-50%, -50%);
    z-index: 10;
    color: white;
  }
</style>