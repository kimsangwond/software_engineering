<template>
  <div v-if="meetingLogsList" role="tablist">
    <b-card :header="selectedOrdinal + '대 국회 ' + meetingType + ' 목록'">
      <b-card v-for="meetingLogs in meetingLogsList" 
        :key="meetingLogs.round" 
        no-body class="mb-1">
        <b-card-header header-tag="header" class="p-1" role="tab">
          <b-button block v-b-toggle="meetingLogs.round + '-round'" variant="secondary">
            {{ meetingLogs.text }}
          </b-button>
        </b-card-header>
        <b-collapse :id="meetingLogs.round + '-round'" role="tabpanel">
          <b-card-body>
            <b-list-group>
              <b-list-group-item 
                v-for="meetingLog in meetingLogs.dialogue" 
                :key="meetingLog.time"
                @click="onSearch(meetingLogs.round, meetingLog.time)"
                button
                class="text-center"
                >
                {{ meetingLog.text }}
              </b-list-group-item>
            </b-list-group>
          </b-card-body>
        </b-collapse>
      </b-card>
    </b-card>
  </div>
  <div v-else>
    <b-card>
      {{ selectedOrdinal }}대 국회 회의록이 없습니다.
    </b-card>
  </div>
</template>

<script>
  import axios from 'axios'
  import { meetingTypeMap, URL } from '@/assets/config.js'

  export default {
    props: [
      'selectedOrdinal', 
      'searchType'    
    ],
    data: function() {
      return {
        meetingType: meetingTypeMap.get(this.searchType),
        meetingLogsList: [],
      }
    },
    watch: {
      selectedOrdinal: {
        immediate: true,
        handler: async function(newOrdinal) {
          this.$nuxt.$loading.start()
          this.meetingLogsList = await axios.get(
            URL + '/meetingInfo', 
            {params: {ordinal: this.selectedOrdinal}}
          ).then((res) => {
            return res.data
          })
          this.$nuxt.$loading.finish()
        }
      }
    },
    methods: {
      onSearch: function(round, time) {
        this.$router.push({
          name: 'ViewDialogue-args',
          params: {
            args: `${this.searchType}-${round}-${time}-${null}-${'dialogueInTime'}`
          }
        })                    
      },
    }
  }
</script>