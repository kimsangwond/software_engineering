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
        console.log(state.subscriberList)
    },
    logoutState: function() {
        state.id = null,
        state.nickName = null
        state.subscriberList = []
    },
}

export const actions = {
    login({ commit }, {id, pw}) {
        //let { res } = await axios.post('/login', {id, pw})
        let res = {
            id: 'admin@admin.com',
            nickName: '운영자',
            subscriberList: [
                {
                    name: '문희상'
                },
                {
                    name: '홍준표'
                }
            ]
        }
        if (!res.id) {
            throw new Error("로그인에 실패했습니다.")
        }
        commit('loginState', res)
    },
    logout({ commit }) {
        //await axios.post('/logout').then(() => commit('logout'))
        () => commit('logoutState')
    }
}