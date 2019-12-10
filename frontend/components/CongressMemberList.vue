<template>
    <div v-if="selectedOrdinal">
        <b-card :header="selectedOrdinal + '대 국회의원 명단'" v-if="congressMemberList">
            <b-table 
                ref="selectableTable"
                striped hover 
                :items="congressMemberList" 
                :fields="fields" 
                >
                <template v-slot:cell(searchByAgenda)="row">
                    <b-button 
                        size="sm" 
                  @click="searchByAgenda(row.item.name)"
                        class="mr-1">
                        {{ row.item.name }} 국회의원 발의 안건찾기
                    </b-button>
                </template>
                <template v-slot:cell(searchByDiscussion)="row">
                    <b-button 
                        size="sm" 
                  @click="searchByDiscussion(row.item.name)"
                        class="mr-1">
                        {{ row.item.name }} 국회의원 발언 찾기
                    </b-button>
                </template>
                <template v-slot:cell(subscribeButton)="row">
                    <b-button size="sm" @click="subscribeMember(row.item)" class="mr-1">
                        구독하기
                    </b-button>
                </template>
            </b-table>
        </b-card>
    </div>
</template>

<script>
    import axios from 'axios'
    import { URL } from "@/assets/config.js"

    export default {
        props: [
            'selectedOrdinal', 
            'searchType'    
        ],
        data: function() {
            return {
                fields: [
                    {
                        key: 'party',
                        label: "정당",
                        sortable: true
                    },
                    {
                        key: 'name',
                        label: "국회의원 이름",
                        sortable: true
                    },
                    {
                        key: 'searchByAgenda',
                        label: '안건 찾기',
                        sortable: false
          },
                    {
                        key: 'searchByDiscussion',
                        label: '발언 검색',
                        sortable: false
                    },
                    {
                        key: 'subscribeButton',
                        label: '구독',
                        sortable: false
                    }
                ],
                congressMemberList: []
            }
        },
        watch: {
            selectedOrdinal: {
                immediate: true,
                handler: async function(newOrdinal) {
                    this.$nuxt.$loading.start()
                    this.congressMemberList = await axios.get(
                        URL + '/congressMember',
                        {params: {ordinal: this.selectedOrdinal}}
                    ).then((res) => {
                        return res.data.member_info_list
                    })
                    this.$nuxt.$loading.finish()
                }
            }
        },
        methods: {
            subscribeMember: function(item) {
            this.$store.dispatch('startSubscribe', item)
        },
            searchByAgenda: function(name) {
        let args = `${name}-agenda`
        this.$router.push({
          name: 'CongressMemberSearch-nameChoice', 
          params: {nameChoice: args}
        })
        },
        searchByDiscussion: function(name) {
        let args = `${name}-discussion`
        this.$router.push({
          name: 'CongressMemberSearch-nameChoice', 
          params: {nameChoice: args}
        })
      }	
        }
    }      
</script>