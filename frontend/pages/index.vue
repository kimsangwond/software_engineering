<template>
  <div class="col-md-10 offset-md-1 mt-5">
    <b-jumbotron 
      bg-variant="white" 
      text-variant="success"
      border-variant="secondary"
      lead="안건, 발언 등으로 회의록의 모든 것을 검색합니다"
      >
      <template v-slot:header class="text-center">Fact-finder에 오신 것을 환영합니다.</template>
      <b-button 
        to="/AgendaSearchView"
        variant="outline-primary"
        class="offset-md-1"
        > 
        안건 검색하기 
      </b-button>
      <b-button 
        to="/DiscussionSearchView"
        variant="outline-primary"
        > 
        발언 검색하기 
      </b-button>
      <b-button 
        to="/CongressMemberSearchView"
        variant="outline-primary"
        > 
        발언 검색하기 
      </b-button>
    </b-jumbotron>
  </div>
</template>

<script>
  export default {
    layout: 'HeaderLayout',
  }
</script>