<template>
    <div v-if="selectedOrdinal">
        <b-table striped hover :items="congressMemberList" :fields="fields"></b-table>
    </div>
</template>

<script>
    export default {
        props: [
            'selectedOrdinal', 
            'searchType'    
        ],
        data: function() {
            return {
                fields: [
                    {
                        key: 'politicalParty',
                        label: "정당",
                        sortable: true
                    },
                    {
                        key: 'memberName',
                        label: "국회의원 이름",
                        sortable: true
                    }
                ],
                congressMemberList: [
                    {
                        isActive: false,
                        politicalParty: "더불어민주당",
                        memberName: '홍익표'                      
                    },
                    {
                        isActive: false,
                        politicalParty: "더불어민주당",
                        memberName: '표창원'                      
                    },
                    {
                        isActive: false,
                        politicalParty: "자유한국당",
                        memberName: '강석진'                      
                    },
                    {
                        isActive: false,
                        politicalParty: "자유한국당",
                        memberName: '김광림'                      
                    }
                ]                
            }
        },
        watch: {
            selectedOrdinal: function() {
                this.congressMemberList = []
            }
        }
    }      
</script>