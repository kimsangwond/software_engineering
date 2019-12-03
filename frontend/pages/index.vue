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
            <b-button type="submit" variant="primary" @click="search">Button</b-button>
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
      async search() {
        axios.get("/searchMeetingLogs",{
          params: {
            keywords: this.searchTarget
          }
        }).then((res) => {
            this.$router.push('UnifiedSearchView',
              params={
                meetingLog: res.data
            })    
        })
      } 
    }
  }
</script>