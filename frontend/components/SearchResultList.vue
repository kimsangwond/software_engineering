<template>
  <div class="mt-5 col-md-10 offset-md-1">
    <b-card :header="searchTypeName + ' 검색결과'">
      <b-list-group>
        <b-list-group-item 
          v-for="result in results" 
          :key="result.round + '_' + result.time" 
          @click="getMeetingLog(result.meeting_type, result.round, result.time, result.highlight)"
          class="flex-column align-items-start text-dark"
          button
          variant="primary"
          >
          <div class="d-flex w-100 justify-content-between result-title">
            <h3 class="mb-1">
              제{{ result.round }}회 {{ result.time }}차 {{ convertMeetingType(result.meeting_type) }}
            </h3>
          </div>
          <p class="mb-1 result-contents" v-html="viewHighlight(result.highlight)"></p>
        </b-list-group-item>
      </b-list-group>
    </b-card>
  </div>
</template>

<script>
  import { searchTypeMap, meetingTypeMap } from "@/assets/config.js"

  export default {
    layout: 'HeaderLayout',
    props: [ 'searchType', 'searchResults'],
    data: function() {
      return {
        searchT: this.searchType,
        results: this.searchResults,
        searchTypeName: searchTypeMap.get(this.searchType),
      }
    },
    watch: {
      searchResults: {
        immediate: true,
        handler(newValue) {
          this.results = newValue
        }
      }
    },
    methods: {
      getMeetingLog: function(meetingType, round, time, highlight) {
        this.$emit('interface', {
          meetingType: meetingType,
          round: round,
          time: time,
          highlight: highlight
        })
      },
      convertMeetingType: function(meetingType) {
        return meetingTypeMap.get(meetingType)
      },
      viewHighlight: function(highlight) {
        return highlight[this.searchT]								
      }
    }
  }
</script>

<style>
  .result-contents {
    white-space: pre-line;
  }
</style>