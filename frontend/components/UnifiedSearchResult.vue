<template>
    <div class="mt-5">
        <b-card header="검색결과">
            <b-list-group>
                <b-list-group-item 
                    v-for="meetingLog in meetingLogs" 
                    :key="meetingLog.round + '_' + meetingLog.time" 
                    @click="getMeetingLog(meetingLog.meeting_type, meetingLog.round, meetingLog.time)"
                    class="flex-column align-items-start"
                    >
                    <div class="d-flex w-100 justify-content-between">
                        <h5 class="mb-1">{{ meetingLog.source.discussion[0] }}</h5>
                    </div>
                    <p class="mb-1">
                        {{ meetingLog.source.agenda[0] }}
                    </p>
                </b-list-group-item>
            </b-list-group>
        </b-card>
    </div>
</template>
<script>
    export default {
        props: ['meetingLogs'],
        methods: {
            getMeetingLog: function(meetingType, round, time) {
                this.$router.push({
                    name: 'ViewDialogue-typeRoundTime',
                    params: {typeRoundTime: `${meetingType}-${round}-${time}`}
                })
            }
        }
    }
</script>