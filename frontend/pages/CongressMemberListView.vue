<template>
	<div class="mt-5">
		<div class="col-md-6 offset-md-3 pb-4">
			<ordinal-list @interface="setSelectedOrdinal" :selectedOrdinal="selectedOrdinal"></ordinal-list>
		</div>
		<div class="col-md-10 offset-md-1 mt-4" v-if="selectedOrdinal">
			<congress-member-list :selectedOrdinal="selectedOrdinal" :searchType="searchType"></congress-member-list>
		</div>
	</div>
</template>

<script>
	import OrdinalList from '@/components/OrdinalList.vue'
	import CongressMemberList from '@/components/CongressMemberList.vue'

	export default {
		layout:  'HeaderLayout',
		components: {
			OrdinalList,
			CongressMemberList
		},
		data: function() {
			return {
				selectedOrdinal: null,
				searchType: "congress_member"
			}
		},
		methods:{
			setSelectedOrdinal(fromEventData) {
				this.selectedOrdinal = fromEventData
			},
			onSearch() {
				axios.get("/searchByName", {
					params: {
						name: CongressMemberName
					} 
				})
			}
		}
	}
</script>
