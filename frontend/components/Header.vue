<template>
    <div>
        <b-navbar toggleable="xl" type="dark" variant="primary">
            <b-navbar-brand to="/">Fact Finder</b-navbar-brand>
            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
            <b-collapse id="nav-collapse" is-nav>
                <b-navbar-nav>
                    <b-nav-item-dropdown text="본회의 검색" right>
                        <b-dropdown-item to="/PlenarySessionBySeriesView">회차별 검색</b-dropdown-item>
                        <b-dropdown-item to="/CongressMemberListView">국회의원별 검색</b-dropdown-item>
                    </b-nav-item-dropdown>
                </b-navbar-nav>
                <b-navbar-nav class="ml-auto">
                    <b-nav-item-dropdown right v-if="userId">
                        <template v-slot:button-content>
                            <em>{{ userNickName }}</em>
                        </template>
                        <b-dropdown-item href="/SubscriberListView">구독중인 목록</b-dropdown-item>
                        <b-dropdown-item href="/ProfileView">프로필</b-dropdown-item>
                        <b-dropdown-item @click="logout">로그아웃</b-dropdown-item>
                    </b-nav-item-dropdown>
                    <b-nav-item v-else to="/LoginView">로그인</b-nav-item>
                </b-navbar-nav>
            </b-collapse>
        </b-navbar>
    </div>
</template>
<script>
    import { mapGetters } from 'vuex'

    export default {
        computed: {
            userId: function() {
                return this.$store.state.id
            },
            userNickName: function() {
                return this.$store.state.nickName
            }
        },
        mounted: function() {
            this.userId = this.id,
            this.userNickName = this.nickName
        },
        methods: {
            logout() {
                this.$store.dispatch('logout').
                then(() => this.redirect("/"))
            },
            redirect(url) {
                this.$router.push(url)
            }
        }   
    }
</script>