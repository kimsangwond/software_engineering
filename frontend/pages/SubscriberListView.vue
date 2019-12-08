<template>
    <div class="mt-4 col-sm-10 offset-sm-1">
      <b-card header="구독중인 국회의원 명단">
        <b-card-group deck>
          <b-card 
            v-for="congressMember in subcribedCongressMemberList" 
            :key="congressMember.name" 
            :header="congressMember.party"
            bg-variant="light" 
            class="text-center"
            style="max-width: 20rem"
          >
              <b-card-text>
                {{ congressMember.name }}
              </b-card-text>
              <b-button 
                :to="{name: 'UnifiedSearch-twoParams', params: {keyword: congressMember.name}}" 
                class="mr-4" 
                variant="success"
                >
                회의록 검색
              </b-button>
              <b-button @click="cancleSubscribe(congressMember.name)" variant="danger">구독 취소</b-button>
          </b-card>
        </b-card-group>
      </b-card>
    </div>
</template>

<script>
  export default {
    layout: 'HeaderLayout',
    computed: {
      subcribedCongressMemberList: function() {
        return this.$store.state.subscriberList
      }
    },
    methods: {
      cancleSubscribe: function(name) {
        this.$store.dispatch('cancleSubscribe', name)
      },
    }
  }
</script>
