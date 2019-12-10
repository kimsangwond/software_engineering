<template>
  <div class="plenary-session-by-series mt-5">
    <div class="col-md-6 offset-md-3 pb-4">
      <ordinal-list @interface="setSelectedOrdinal" :selectedOrdinal="selectedOrdinal"></ordinal-list>
    </div>
    <div class="col-md-10 offset-md-1 mt-4" v-if="selectedOrdinal">
      <meeting-log-list-by-series 
        :selectedOrdinal="selectedOrdinal" 
        :searchType="searchType"
        >
      </meeting-log-list-by-series>
    </div>
  </div>
</template>

<script>
  import OrdinalList from '@/components/OrdinalList.vue'
  import MeetingLogListBySeries from '@/components/MeetingLogListBySeries.vue'
  import { URL } from "@/assets/config.js"

  export default {
    layout:  'HeaderLayout',
    components: {
      MeetingLogListBySeries,
      OrdinalList,
    },
    data: function() {
      return {
        selectedOrdinal: null,
        searchType: "plenary_session"
      }
    },
    methods:{
      setSelectedOrdinal(fromEventData) {
        this.selectedOrdinal = fromEventData
      }
    }
  }
</script>