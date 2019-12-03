<template>
    <div class="mt-4 col-sm-10 offset-sm-1">
      <h2 class="mb-5">구독중인 국회의원 명단</h2>
      <b-card-group deck>
        <b-card 
          v-for="congressMember in subcribedCongressMemberList" 
          :key="congressMember.name" 
          :header="congressMember.name"
          bg-variant="light" 
          class="text-center"
          style="max-width: 20rem"
        >
            <b-card-text>
            {{ congressMember.name }}
            </b-card-text>
            <b-button href="#">Go somewhere</b-button>
        </b-card>
      </b-card-group>
    </div>
</template>

<script>
  export default {
    layout: 'HeaderLayout',
    computed: {
      subcribedCongressMemberList: function() {
        return this.$store.state.subcribedCongressMemberList
      }
    }
  }
</script>
