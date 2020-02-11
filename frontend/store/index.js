export const state = () => ({
	id: '',
	nickName: '',
	subscriberList: []
})

export const getters = {
	id: (state) => state.id,
	nickName: (state) => state.nickName,
	subscriberList: (state) => state.subscriberList,
}

export const mutations = {
	loginState: function(state, req) { 
		state.id = req.id,
		state.nickName = req.nickName,
		state.subscriberList = req.subscriberList
	},
	logoutState: function(state) {
		state.id = null,
		state.nickName = null
		state.subscriberList = []
	},
	cancleSubscribeCongressMember: function(state, name) {
		state.subscriberList = state.subscriberList.filter((subscriber) =>{
			return subscriber.name != name
		});
	},
	changeInfo: function(state, req) {
		if (req.nickName) {
			state.nickName = req.nickName
		}
		if (req.pw) {
			state.pw = req.pw
		}
	},
	startSubscribeCongressMember: function(state, req) {
		state.subscriberList.push({ 
			name: req.name,
			party: req.party
		})
	}
}

export const actions = {
	login({ commit }, req ) {
		Object.defineProperties(req, {
			nickName: {
				value: '황인준',
				writable: true,
			},
			subscriberList: {
				value: [
					{
						name: '이해찬',
						party: '더불어민주당'
					},
					{
						name: '나경원',
						party: '자유한국당'
					}
				],
				writable: true,
			}
		})
		if (!req.id) {
			throw new Error("로그인에 실패했습니다.")
		}
		commit('loginState', req)
	},
	logout({ commit }) {
		commit('logoutState')
	},
	cancleSubscribe({ commit }, name) {
		commit('cancleSubscribeCongressMember', name)
	},
	changeInfo({ commit }, req) {
		commit('changeInfo', req)
	},
	startSubscribe( { commit }, req) {
		commit('startSubscribeCongressMember', req)
	}
}