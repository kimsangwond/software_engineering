<template>
  <div>
    <div class="col-md-8 offset-md-2 mt-5">
      <b-card>
        <search-bar 
          @interface="onSearchTarget" 
          :searchTarget="searchTarget"
          :searchType="'discussion'"
          ></search-bar>
      </b-card>
    </div>
    <div class="col-md-10 offset-md-1 mt-5">
      <search-result-list 
        @interface="viewDialogue" 
        :searchType="'discussion'"
        :searchResults="searchResults"
        v-if="isSearch"
      ></search-result-list>
    </div>
  </div>
</template>

<script>
  import SearchBar from "@/components/SearchBar.vue"
  import SearchResultList from "@/components/SearchResultList.vue"
  import { URL } from "@/assets/config.js"
  import axios from 'axios'

  export default {
    layout: 'HeaderLayout',
    components: { 
      SearchBar,
      SearchResultList
    },
    data: function() {
      return {
        searchTarget: '',
        searchResults: [],
        isSearch: false,
      }
    },
    methods: {
      onSearchTarget: async function(input) {
        this.$nuxt.$loading.start()
        this.searchResults = await axios.get(
          URL + '/searchDiscussion',
          {
            params: {
              keyword: input,
              is_name: false
            }
          }
        ).then((res) => {
          return res.data.result
        })
        this.isSearch = true
        this.$nuxt.$loading.finish()
      },
      viewDialogue: function(dialogueInfo) {
        this.$router.push({
          name: 'ViewDialogue-args',
          params: {
            args: `${dialogueInfo.meetingType}-${dialogueInfo.round}-${dialogueInfo.time}-${dialogueInfo.highlight['discussion']}-${'Discussion'}`
          }
        })
      }
    }
  }
</script>