<template>
    <div class="select-oridnal">
        <select class="form-control" v-model="selectedOrdinal" @change="setOrdinal">
            <option disabled value="">몇 대 국회인지 선택해주세요</option>
            <option v-for="info in options" :key="info.id" :value="info.id">
                {{ info.text }}
            </option>
        </select>
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
        data: function() {
            return {
                selectedOrdinal: '',
                options: temporaryArray()
            }
        },
        methods:{
            setOrdinal: function() {
                this.$emit('interface', this.selectedOrdinal)
            }
        } 
    }
</script>