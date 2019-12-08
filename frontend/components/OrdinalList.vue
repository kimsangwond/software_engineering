<template>
	<div>
		<b-form-select v-model="choice" @change="setOrdinal">
			<template v-slot:first>
				<option :value="null" disabled> 몇 대 국회인지 선택해주세요.</option>
			</template>
			<option v-for="info in options" :key="info.id" :value="info.id">
				{{ info.text }}
			</option>
		</b-form-select>
	</div>
</template>

<script>
	let temporaryArray = () => {
		let temp = []
		for(let i=1; i<21; i++) {
			temp.push(
				{
					"id": i,
					"text": `제${i}대`
				}
			)
		}
		return temp
	}

	export default {
		props: [ 'selectedOrdinal' ],
		data: function() {
			return {
				choice: this.selectedOrdinal,
				options: temporaryArray()
			}
		},
		watch: {
			selectedOrdinal: function() {
				this.choice = this.selectedOrdinal
			}
		},
		methods:{
			setOrdinal: function() {
				this.$emit('interface', this.choice)
			}
		} 
	}
</script>