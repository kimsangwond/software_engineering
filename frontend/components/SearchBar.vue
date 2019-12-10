<template>
  <div>
    <b-form @submit="onSubmit">
      <b-input-group>
        <b-form-input
          v-model="searchKeywords"
          type="text"
          :placeholder="'검색하실 ' + searchTypeName + '을 입력해주세요'"
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
</template>

<script>
  import { searchTypeMap } from "@/assets/config.js"

  export default {
    props: [ 'searchTarget', 'searchType' ],
    data: function() {
      return {
        searchKeywords: this.searchTarget,
        searchTypeName: searchTypeMap.get(this.searchType),     
      }
    },
    watch: {
      searchType: {
        immediate: true, 
        handler (newValue, oldValue) {
          this.searchTypeName = searchTypeMap.get(newValue)
        }
      },
    },
    methods: {
      onSubmit: function(event) {
        event.preventDefault()
      },
      onSearch: function() {
        this.$emit('interface', this.searchKeywords)
      }
    }  
  }
</script>