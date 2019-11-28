<template>
  <div class="col-md-8 offset-md-2">
    <b-form @submit="onSubmit">
      <b-input-group class="mt-5">
        <b-form-input
          v-model="searchTarget"
          type="search"
          placeholder="무엇이든 검색해보세요"
          required
        >
        </b-form-input>
        <b-input-group-append>
          <b-button type="submit" variant="primary" @click="search">Button</b-button>
        </b-input-group-append>
      </b-input-group>
    </b-form>
  </div>
</template>
<script>
  export default {
    layout: 'HeaderLayout',
    data: function() {
      return {
        searchTarget: '',
      }
    },
    methods: {
      onSubmit: function(event) {
        event.preventDefault()
      },
      redirect: function(url) {
        this.$router.push(url)
      },
      search() {
        //query문 날리기 
        this.redirect("/UnifiedSearchView")  
      } 
    }
  }
</script>