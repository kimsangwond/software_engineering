<template>
  <div class="col-md-6 offset-md-3">
    <b-form @submit="onSubmit">
      <b-form-group
        label="이메일 주소:"
        label-for="email-address-input"
      >
        <b-form-input
          id="email-address-input"
          v-model="form.id"
          type="email"
          required
          placeholder="이메일을 입력하세요."
        ></b-form-input>
      </b-form-group>
      <b-form-group label="비밀번호" label-for="password-input">
        <b-form-input
          id="password-input"
          v-model="form.pw"
          type="password"
          required
          placeholder="비밀번호를 입력하세요."
        ></b-form-input>
      </b-form-group>
      <p v-if="errorMsg" class="error">
        {{ errorMsg }}
      </p>
      <div class="mt-3">
        <b-button type="submit" variant="primary" @click="login">로그인</b-button>
      </div>
      <div class="mt-3">
        <b-button variant="light" @click="signUp">회원가입</b-button>
      </div>
    </b-form>
  </div>
</template>

<script>
  export default {
    layout: 'HeaderLayout',
    data: function() {
      return {
        form: {
          id: '',
          pw: '',
        },
        errorMsg: '',
      }
    },
    methods: {
      onSubmit: function(event) {
        event.preventDefault()
      },
      async login() {
        try {
          await this.$store.dispatch('session/login', {
            id: this.form.email,
            pw: this.form.password
          }).then(() => this.redirect("/"))
        } catch (e) {
          this.errorMsg = e.message
        } 
      },
      redirect(url) {
        this.$router.push(url)
      },
      signUp() {
        this.redirect("/SignUpView")
      }
    }
  }
</script>
