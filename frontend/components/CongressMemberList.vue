<template>
	<div v-if="selectedOrdinal">
		<b-card :header="selectedOrdinal + '대 국회의원 명단'" v-if="congressMemberList">
			<b-table 
				ref="selectableTable"
				striped hover 
				:items="congressMemberList" 
				:fields="fields" 
				>
				<template v-slot:cell(searchButton)="row">
					<b-button 
						size="sm" 
						:to="{name: 'UnifiedSearch-name', params: {name: row.item.name}}" 
						class="mr-1">
						회의록 찾기
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
						key: 'searchButton',
						label: '발언 검색하기',
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
					this.congressMemberList = await axios.get(
						URL + '/congressMember',
						{params: {ordinal: this.selectedOrdinal}}
					).then((res) => {
						return res.data.member_info_list
					})
				}
			}
		},
		methods: {
			subscribeMember: function(item) {
				//vuex에 기능추가할 것   
			}
		}
	}      
</script>