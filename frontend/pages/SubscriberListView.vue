<template>
    <div>
      <b-card-group deck>
        <b-card 
          v-for="congressMember in subcribedCongressMemberList" 
          :key="congressMember.name" 
          :header="congressMember.name"
          bg-variant="light" 
          class="text-center"
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
    data: function() {
      return {
        subcribedCongressMemberList: [
          {
            name:'정영진'
          },
          {
            name:'문희상'
          }
        ]
      }
    }
  }
</script>
