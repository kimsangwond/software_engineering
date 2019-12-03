<template>
    <div v-if="meetingLogsList" role="tablist">
        <b-card v-for="meetingLogs in meetingLogsList" 
            :key="meetingLogs.round" 
            no-body class="mb-1">
            <b-card-header header-tag="header" class="p-1" role="tab">
                <b-button block v-b-toggle="meetingLogs.round + '-round'" variant="info">
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
                            >
                            {{ meetingLog.text }}
                        </b-list-group-item>
                    </b-list-group>
                </b-card-body>
            </b-collapse>
        </b-card>
    </div>
    <div v-else>
        {{ selectedOrdinal }}대 국회 회의록이 없습니다.
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        props: [
            'selectedOrdinal', 
            'searchType'    
        ],
        watch: {
            async selectedOrdinal() {
                this.meetingLogsList = await axios.get('/getMeetingLogsList', {
                    params: {
                        ordinal: this.selectedOrdinal,
                    }
                })
            }
        },
        methods: {
            async onSearch(round, time) {
                axios.get('/searchMeetingLog', {
                    params: { 
                        type : this.searchType, 
                        ordinal: this.selectedOrdinal, 
                        round: round, 
                        time: time
                    }
                }).then((res) => {
                    this.$router.push('ViewDialogue',
                    params={
                        meetingLog: res.data
                    })                    
                }

                )
            },
        }
    }
</script>