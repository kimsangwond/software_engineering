<template>
  <div class="col-md-10 offset-md-1 mt-5">
   <b-carousel
      v-model="slide"
      :interval="5000"
      controls
      indicators
      img-width="1024"
      img-height="768"
      @sliding-start="onSlideStart"
      @sliding-end="onSlideEnd"
    >
      <b-carousel-slide 
        caption="Fact finder에 오신 것을 환영합니다." 
        caption-tag="h2"
        text="안건, 발언, 국회의원 이름등으로 국회에 기록된 모든 것을 검색할 수 있습니다"
        >
        <template v-slot:img>
          <img
            class="d-block image-fluid w-100"
            width="1024"
            height="768"
            src="@/assets/Assembly_outside_picture.jpg"
          >
        </template>
      </b-carousel-slide>
      <b-carousel-slide 
        caption="발의한 안건의 내용이 궁금하다면!"
        caption-tag="h2"
        >
        <template v-slot:img>
          <img
            class="d-block image-fluid w-100"
            width="1024"
            height="768"
            src="@/assets/Assembly_sculpture1.jpg"
          >
        </template>
        <b-button 
          to="/AgendaSearchView"
          class="btn-outline-primary bg-white text-primary"
          >
          안건 검색하러 가기
        </b-button>
      </b-carousel-slide>
      <b-carousel-slide 
        caption="어떤 발언을 했는지 궁금하다면!"
        caption-tag="h2"
        >
        <template v-slot:img>
          <img
            class="d-block image-fluid w-100"
            width="1024"
            height="768"
            src="@/assets/Assembly_sculpture2.jpg"
          >
        </template>
        <b-button 
          to="/DiscussionSearchView"
          class="btn-outline-primary bg-white text-primary"
          >
          발언 검색하러 가기
        </b-button>
      </b-carousel-slide>
      <b-carousel-slide 
        caption="국회의원의 의정활동이 궁금하다면!"
        caption-tag="h2"
        >
        <template v-slot:img>
          <img
            class="d-block image-fluid w-100"
            width="1024"
            height="768"
            src="@/assets/Assembly_inside_picture.jpg"
          >
        </template>
        <b-button 
          to="/CongressMemberSearch"
          class="btn-outline-primary bg-white text-primary"
          >
          국회의원 이름으로 검색하러 가기
        </b-button>
      </b-carousel-slide>
    </b-carousel>
  </div>
</template>

<script>
  export default {
    layout: 'HeaderLayout',
    data: function() {
      return {
        slide: 0,
      }
    },
    methods: {
      onSlideStart(slide) {
        this.sliding = true
      },
      onSlideEnd(slide) {
        this.sliding = false
      }
    }
  }
</script>