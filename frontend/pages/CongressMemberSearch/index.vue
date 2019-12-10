<template>
  <div>
    <div class="col-md-8 offset-md-2 mt-5">
      <b-card>
        <search-bar 
          @interface="onSearchTarget" 
          :searchTarget="searchTarget"
          :searchType="selectedRadio"
          >
        </search-bar>
        <div class="offset-md-8">
          <b-form-group>
            <b-form-radio-group
              v-model="selectedRadio"
              :options="options"
              name="radio-inline"
            ></b-form-radio-group>
          </b-form-group>
        </div>
      </b-card>
    </div>
    <div class="col-md-10 offset-md-1 mt-5">
      <search-result-list 
        @interface="viewDialogue" 
        :searchType="selectedRadio"
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
        options: [
          { text: '안건에 대해 검색하기', value: 'agenda' },
          { text: '발언에 대해 검색하기', value: 'discussion' },
        ],
        selectedRadio: 'agenda',
      }
    },
    methods: {
      onSearchTarget: async function(input) {
        this.$nuxt.$loading.start()
        this.searchTarget = input
        let urlTailPart = ''
        if (this.selectedRadio == 'agenda') {
          urlTailPart = '/searchAgenda'
        } else {
          urlTailPart = '/searchDiscussion'
        }
        this.searchResults = await axios.get(
          URL + urlTailPart,
          {
            params: {
              keyword: input,
              is_name: true
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
            args: `${dialogueInfo.meetingType}-${dialogueInfo.round}-${dialogueInfo.time}-${this.searchTarget}-${'CongressMember'}`
          }
        })
      }
    }  
  } 
</script>