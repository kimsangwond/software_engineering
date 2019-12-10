<template>
    <b-card title="회원가입" class="col-sm-10 offset-sm-1 mt-5">
        <div class="sign-up-form">
            <b-form @submit="onSubmit">
                <b-form-group
                    label="이메일 주소"
                    label-for="email-address-input"
                >
                <b-form-input
                    id="email-address-input"
                    v-model="form.id"
                    placeholder="이메일을 입력하세요."
                    type="email"
                    required
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
                <b-button block variant="secondary" @click="signUp">회원가입</b-button>
            </b-form>
        </div>
    </b-card>
</template>
<script>
    import axios from 'axios'

    export default {
        layout: 'HeaderLayout',
        data: function() {
            return {
                form: {
                    id: '',
                    pw: '',
                    pw2: '',
                    nickName: '',
                },
                errorMsg: '',                        
            }
        },
        methods: {
            onSubmit: function(event) {
                event.preventDefault()
            },
            signUp: function() {
                //ajax요청      
            }
        }   
    }
</script>