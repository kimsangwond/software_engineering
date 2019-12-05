<template>
    <unified-search-result :meetingLogs="meetingLogs"></unified-search-result>
</template>
<script>
    import axios from 'axios'
    import UnifiedSearchResult from "@/components/UnifiedSearchResult.vue"
    import { URL } from "@/assets/config.js"

    export default {
        layout: 'HeaderLayout',
        components: { UnifiedSearchResult },
        asyncData: async function({ params }) {
            let result = await axios.get(
                URL + "/searchByName",
                {params: {name: params.name}}
            ).then((res) => (res.data.result))
            return {
                meetingLogs: result
            }
        },
    }
</script>