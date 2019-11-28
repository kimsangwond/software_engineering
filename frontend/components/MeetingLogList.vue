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
                            :to="{path: 'ViewDialouge', query: { type : searchType, ordinal: selectedOrdinal, round: meetingLogs.round, time: meetingLog.time }}" 
                            v-for="meetingLog in meetingLogs.dialogue" 
                            :key="meetingLog.time">
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
    export default {
        props: [
            'selectedOrdinal', 
            'searchType'    
        ],
        data: function() {
            return {
                meetingLogsList: [
                    {
                        "round": 1,
                        "text": "제1회",
                        "dialogue": [
                            {
                                "time":  1,
                                "text": "제1차"
                            },
                            {
                                "time": 2,
                                "text": "제2차"
                            }
                        ]                        
                    },
                    {
                        "round": 2,
                        "text": "제2회",
                        "dialogue": [
                            {
                                "time": 1,
                                "text": "제1차"
                            }
                        ]
                    }
            ]                
            }
        },
        watch: {
            selectedOrdinal: function() {
                this.meetingLogsList = [
                        {
                            "round": 1,
                            "text": "제1회",
                            "dialogue": [
                                {
                                    "time":  1,
                                    "text": "제1차"
                                }
                            ]                        
                        },
                        {
                            "round": 2,
                            "text": "제2회",
                            "dialogue": [
                                {
                                    "time": 1,
                                    "text": "제1차"
                                },
                                {
                                    "time": 2,
                                    "text": "제2차"
                                }
                            ]
                        }
                    ]
                
            }
        }
    }      
</script>