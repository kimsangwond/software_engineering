<template>
    <div class="mt-5">
        <div class="col-md-6 offset-md-3 pb-4">
            <ordinal-list @interface="setSelectedOrdinal"></ordinal-list>
        </div>
        <div class="col-md-10 offset-md-1 mt-4" v-if="selectedOrdinal">
            <h2 class="pb-3">{{ selectedOrdinal }}대 국회의원 명단</h2>
            <congress-member-list :selectedOrdinal="selectedOrdinal" :searchType="searchType"></congress-member-list>
        </div>
    </div>
</template>

<script>
    import OrdinalList from '@/components/OrdinalList.vue'
    import CongressMemberList from '@/components/CongressMemberList.vue'

    export default {
        layout:  'HeaderLayout',
        components: {
            OrdinalList,
            CongressMemberList
        },
        data: function() {
            return {
                selectedOrdinal: '',
                searchType: "congress_member"
            }
        },
        methods:{
            setSelectedOrdinal(fromEventData) {
                this.selectedOrdinal = fromEventData
                //let selectedOrdinal = fromEventData
                //selectedOrdinal하고 url하고 결합하려는 것 필요하다.
                //return axios.get("여기서는 selectedOrdinal을 이용하여 리스트를 가져올 수 있도록 한다.")
                //.then((res) => {
                //    this.congressMemberList = res.data
                //})
            }
        }
    }
</script>
<style scoped>
</style>
