<template>
    <div role="tablist">
        <b-card
            v-for="paragraph in meetingLog"
            :key="paragraph.order"
            no-body class="mb-1">
            <b-card-header header-tag="header" class="p-1" role="tab">
                <b-button block v-b-toggle="paragraph.order" variant="info">
                    <div v-html="concatAgenda(paragraph.agenda)"></div>
                </b-button>
            </b-card-header>
            <b-collapse :id="paragraph.order" role="tabpanel">
                <b-card-body>
                    <div v-html="concatDiscussion(paragraph.discussion)"></div>
                </b-card-body>
            </b-collapse>
        </b-card>
    </div>
</template>
<script>
    import axios from 'axios'
    import { URL } from '@/assets/config.js'

    export default {
        layout: 'HeaderLayout',
        asyncData: async function({ params }) {
            let [type, round, time] = params.typeRoundTime.split("-")
            let result = await axios.get(
                URL + "/dialogueInTime",
                {params: {
                    meeting_type: type,
                    round: round, 
                    time: time
                    }
                 }
            ).then((res) => {
                return res.data
            })
            return {
                meetingLog: result.dialogue
            }
        },
        methods: {
            concatDiscussion: function(discussionArr) {
                let newArr = discussionArr.filter((sentence) => {
                    console.log(sentence)
                    console.log('-------------')
                    return sentence.replace(/(?:\r\n|\r|\n)/g, '<br />')
                })
                return newArr.join('<br/>')
            },
            concatAgenda: function(agendaArr) {
                return agendaArr.join('')
            }
        }
    }
</script>