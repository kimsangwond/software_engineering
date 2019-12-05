<template>
  <div>
    <div class="col-md-8 offset-md-2">
      <b-form @submit="onSubmit">
        <b-input-group class="mt-5">
          <b-form-input
            v-model="searchTarget"
            type="text"
            placeholder="무엇이든 검색해보세요"
            required
          >
          </b-form-input>
          <b-input-group-append>
            <b-button 
              type="submit" 
              variant="primary" 
              @click="onSearch"
              >
              검색
            </b-button>
          </b-input-group-append>
        </b-input-group>
      </b-form>
    </div>
  </div>
</template>
<script>
  import axios from 'axios'

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
      onSearch: function() {
        this.$router.push({
          name: 'UnifiedSearch-keywords',
          params: {keywords: this.searchTarget}}
        )
      }
    } 
  }
</script>