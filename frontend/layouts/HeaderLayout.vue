<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col-lg-12">
                <Header/>
            <div class="contents">
                <nuxt/>
            </div>
            </div>
        </div>
    </div>
</template>

<script>
    import Header from '@/components/Header'
    
    export default {
        components: {
            Header
        }
    }
</script>