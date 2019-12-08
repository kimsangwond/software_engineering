<template>
	<div>
		<b-navbar toggleable="xl" type="dark" variant="primary">
			<b-navbar-brand to="/">Fact Finder</b-navbar-brand>
			<b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
			<b-collapse id="nav-collapse" is-nav>
				<b-navbar-nav>
					<b-nav-item
						to="/PlenarySessionBySeriesView"
						>
						본회의 회차별 검색
					</b-nav-item>
					<b-nav-item 
						to="/CongressMemberListView"
            			>
						역대 국회의원 리스트
					</b-nav-item>
          <b-nav-item-dropdown text="검색" right>
            <b-dropdown-item to="/AgendaSearchView">안건 검색</b-dropdown-item>
            <b-dropdown-item to="/DiscussionSearchView">발언 검색</b-dropdown-item>
            <b-dropdown-item to="/CongressMemberSearchView">국회의원으로 검색</b-dropdown-item>
          </b-nav-item-dropdown>
				</b-navbar-nav>
				<b-navbar-nav class="ml-auto">
					<b-nav-item-dropdown right v-if="userId">
						<template v-slot:button-content>
							<em>{{ userNickName }}</em>
						</template>
						<b-dropdown-item to="/SubscriberListView">구독중인 목록</b-dropdown-item>
						<b-dropdown-item to="/ProfileView">프로필</b-dropdown-item>
						<b-dropdown-item @click="logout">로그아웃</b-dropdown-item>
					</b-nav-item-dropdown>
					<b-nav-item v-else to="/LoginView">로그인</b-nav-item>
				</b-navbar-nav>
			</b-collapse>
		</b-navbar>
	</div>
</template>

<script>
	export default {
		computed: {
			userId: function() {
				return this.$store.getters.id
			},
			userNickName: function() {
				return this.$store.getters.nickName
			}
		},
		methods: {
			logout() {
				this.$store.dispatch('logout').
				then(() => {this.$router.push("/")})
			},
		}   
	}
</script>