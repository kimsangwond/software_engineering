import axios from 'axios'

export const state = () => ({
    id: null,
    nickName: null,
    subscriberList: []
})

export const getters = {
    getNickName: function(state) {
        return state.nickName
    },
    getSubscriberList: function(state) {
        return state.subscriberList
    },
    getInfo: function(state) {
        return {
            id: state.id,
            nickName: state.nickName,
            subscriberList: state.subscriberList        
        }
    }
}

export const mutations = {
    login: function(state, id, nickName, subscriberList) {
        state.id = id,
        state.nickName = nickName,
        state.subscriberList = subscriberList
    },
    logout: function() {
        state.id = null,
        state.nickName = null
        state.subscriberList = []
    },
}

export const actions = {
    async login({ commit }, {id, pw}) {
        let { res } = await axios.post('/login', {id, pw})
        if (!res.id) {
            throw new Error("로그인에 실패했습니다.")
        }
        commit('login', res.id, res.nickName, res.subscriberList)
    },
    async logout({ commit }) {
        await axios.post('/logout').then(() => commit('logout'))
    }
}