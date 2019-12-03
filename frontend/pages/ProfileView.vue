<template>
  <form class="col-sm-10 offset-sm-1 mt-5" @submit="onSubmit">
    <div class="form-group row">
      <label for="input-id" class="col-sm-2 col-form-label">아이디</label>
      <div class="col-sm-10">
        <input 
          type="text" 
          readonly class="form-control-plaintext" 
          id="input-id" 
          :value="id"
          >
      </div>
    </div>
    <div class="form-group row">
      <label for="input-nickname" class="col-sm-2 col-form-label">닉네임</label>
      <div class="col-sm-10">
        <input 
          type="text" 
          class="form-control" 
          id="input-nickname" 
          v-model="form.nickName"
          >
      </div>
    </div>
    <div class="form-group row">
      <label for="input-pw" class="col-sm-2 col-form-label">비밀번호</label>
      <div class="col-sm-10">
        <input 
          type="password" 
          class="form-control" 
          id="input-pw" 
          placeholder="비밀번호"
          v-model="form.pw"
        >
      </div>
    </div>
    <div class="form-group row">
      <label for="input-pw-confirm" class="col-sm-2 col-form-label">비밀번호 확인</label>
      <div class="col-sm-10">
        <input 
          type="password" 
          class="form-control" 
          id="input-pw-confirm" 
          placeholder="비밀번호 확인"
          v-model="form.pw2"
          >
      </div>
    </div>
    <p v-if="errorMessage" class="error">
      {{ errorMessage }} 
    </p>
    <div class="form-group row">
      <div class="col-sm-10">
        <button type="submit" class="btn btn-secondary" @click="changeInfo">변경</button>
      </div>
    </div>
  </form>
</template>
<script>
    import isPasswordSame from '@/assets/ConfirmPassword.js'

    export default {
      layout: 'HeaderLayout',
      data() {
        return {
          id: 'admin',
          nickName: '운영자',
          form: {
            id: this.id,
            nickName: '',
            pw: '',
            pw2: ''
          },
          errorMessage: ''
        }
      },
      methods: {
        onSubmit: function(event) {
          event.preventDefault()
        },
        redirect: function(url) {
          this.$router.push(url)
        },
        changeInfo: function() {
          if (isPasswordSame(this.form)) {
            this.errorMessage = ''
            console.log(this.form) // ajax to change 
            this.redirect("/")
          } else {
            this.errorMessage = "비밀번호가 일치하지 않습니다."
          }  
        }
      }
    }
</script>