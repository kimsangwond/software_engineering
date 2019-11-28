<template>
    <div class="sign-up-form">
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
            <b-form-group label="비밀번호 확인" label-for="password-input-match">
                <b-form-input
                    id="password-input-match"
                    v-model="form.pw2"
                    type="password"
                    required
                    placeholder="비밀번호 확인을 위해 다시 입력해주세요"
                ></b-form-input>
            </b-form-group>
            <b-form-group label="닉네임" label-for="nickname-input">
                <b-form-input
                    id="nickname-input"
                    v-model="form.nickName"
                    type="text"
                    required
                    placeholder="사용하실 닉네임을 입력해주세요"
                ></b-form-input>
            </b-form-group>
            <p v-if="errorMsg" class="error">
                {{ errorMsg }}
            </p>
            <b-button variant="light" @click="signUp">회원가입</b-button>
        </b-form>
    </div>
</template>
<script>
    export default {
        data: function() {
            return {
                form: {
                    id: '',
                    pw: '',
                    pw2: '',
                    nickName: '',
                }                        
            }
        },
        methods: {
            onSubmit: function(event) {
                event.preventDefault()
            }
        }   
    }
</script>