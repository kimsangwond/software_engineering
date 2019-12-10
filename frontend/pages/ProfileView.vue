<template>
  <b-card title="회원정보 변경" class="col-sm-10 offset-sm-1 mt-5">
    <form @submit="onSubmit">
      <div class="form-group row">
        <label for="input-id" class="col-sm-2 col-form-label"><b>아이디</b></label>
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
        <label for="input-nickname" class="col-sm-2 col-form-label"><b>닉네임</b></label>
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
        <label for="input-pw" class="col-sm-2 col-form-label"><b>비밀번호</b></label>
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
        <label for="input-pw-confirm" class="col-sm-2 col-form-label"><b>비밀번호 확인</b></label>
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
      <b-alert
        :show="isDifferentPassword"
        dismissible
        variant="warning"
      >
        패스워드가 일치하지 않아요!
      </b-alert>
      <div class="form-group row">
        <div class="col-sm-10">
          <button type="submit" class="btn btn-secondary" @click="changeInfo">변경</button>
        </div>
      </div>
      <b-modal v-model="isChangeSuccess">
        {{ changeMessage }} 
      </b-modal>
    </form>
  </b-card>
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
          isChangeSuccess: null,
          isDifferentPassword: false,
          changeMessage: ''
        }
      },
      methods: {
        onSubmit: function(event) {
          event.preventDefault()
        },
        changeInfo: async function() {
          if (isPasswordSame(this.form) == true) {
            try {
              this.$store.dispatch('changeInfo', {
                nickName: this.form.nickName,
                pw: this.form.pw
              }).then(() => {
                this.isChangeSuccess = true
                this.changeMessage = "변경에 성공하였습니다."      
              })
            } catch (err) {
              this.isChangeSuccess = false
              this.changeMessage = "변경에 실패하였습니다."
            }
          } else {
            this.isDifferentPassword = true
          }  
        }
      }
    }
</script>