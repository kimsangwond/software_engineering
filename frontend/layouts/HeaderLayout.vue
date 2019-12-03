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

<style>
    body {
        background: url('../assets/background-image.jpeg') no-repeat center center fixed;
        -webkit-background-size: cover;
        -moz-background-size: cover;
        background-size: cover;
        -o-background-size: cover;
    }
</style>