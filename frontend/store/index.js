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
    loginState: function(state, res) { 
        state.id = res.id,
        state.nickName = res.nickName,
        state.subscriberList = res.subscriberList
    },
    logoutState: function(state) {
        state.id = null,
        state.nickName = null
        state.subscriberList = []
    },
    cancleSubscribeCongressMember: function(targetObject) {     
        let newSubscribeList = state.subscriberList.filter(function(subscriber) {
            return subscriber.name != targetObject.name
        });
        state.subscriberList = newSubscribeList
    }
}

export const actions = {
    login({ commit }, {id, pw}) {
        let res = {
            id: 'admin@admin.com',
            nickName: '운영자',
            subscriberList: [
                {
                    name: '이해찬',
                    party: '더불어민주당'
                },
                {
                    name: '홍준표',
                    party: '자유한국당'
                }
            ]
        }
        if (!res.id) {
            throw new Error("로그인에 실패했습니다.")
        }
        commit('loginState', res)
    },
    logout({ commit }) {
        commit('logoutState')
    },
    cancleSubscribe({ commit }, { name }) {
        let target = { name } ;
        commit('cancleSubscribeCongressMember', target)
    }
}