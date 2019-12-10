<template>
	<div role="tablist" class="col-sm-10 offset-sm-1 mt-5">
    <b-card :header="resultHeader">
      <b-card
        v-for="paragraph in meetingLog"
        :key="paragraph.order"
        no-body class="mb-1">
        <b-card-header header-tag="header" class="p-1" role="tab">
          <b-button block v-b-toggle="paragraph.order" variant="secondary">
            <div v-html="paragraph.agenda" class="agenda"></div>
          </b-button>
        </b-card-header>
        <b-collapse :id="paragraph.order" role="tabpanel">
          <b-card-body>
            <div class="row discussion" v-html="showDiscussion(paragraph.discussion)"></div>
          </b-card-body>
        </b-collapse>
      </b-card>
    </b-card>
	</div>
</template>

<script>
	import axios from 'axios'
	import { URL, meetingTypeMap } from '@/assets/config.js'

  export default {
    layout: 'HeaderLayout',
		asyncData: async function({ params }) {
      let [type, round, time, highlight, url] = params.args.split("-")
      let response = null
      if (url == 'dialogueInTime') { 
        response = await axios.get(
          URL + "/dialogueInTime",
          {
            params: {
              meeting_type: type,
              round: round,
              time: time,
            }
          }
        ).then((res) => (res.data))
      } else {
        response = await axios.get(
          URL + "/search" + url + "Detail",
          { params: 
            {
              meeting_type: type,
              round: round, 
              time: time,
              keyword: highlight
            }
          }
        ).then((res) => (res.data.result[0]))
      }
      let result = []
      for(let i=0; i < response.agenda.length; i++) {
        result.push({
          order: `${i}`,
          agenda: response.agenda[i],
          discussion: response.discussion[i]                        
        })
      }
			return {
        meetingLog: result,
        resultHeader: `제${round}회 ${time}차 국회 ${meetingTypeMap.get(type)}`
      }
    },
    methods: {
      showDiscussion: function(discussion) {
        let splittedDiscussionBySpeaking = discussion.split("\n\n")
        let speakingArr = []
        for(let i=0; i < splittedDiscussionBySpeaking.length; i++) {
          let entireSpeaking = []
          let splittedSpeaking = splittedDiscussionBySpeaking[i].split(" ")
          let speakerPart = "<div class=col-md-2>" + "<strong>" + splittedSpeaking.slice(0,3).join(' ') +
                            "</strong>" + "</div>"
          entireSpeaking.push(speakerPart)
          let speakingPart = "<div class=col-md-10>" + splittedSpeaking.slice(3).join(" ") + "</div>"
          entireSpeaking.push(speakingPart)
          entireSpeaking.push("\n")
          speakingArr.push(entireSpeaking.join(''))
        }
        return speakingArr.join('')
      }
    }
	}
</script>

<style>
  .agenda {
    white-space: pre-line;
  }
  .discussion {
    white-space: pre-line;
  }
</style>