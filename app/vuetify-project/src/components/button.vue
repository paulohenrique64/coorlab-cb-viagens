<template>
    <v-btn variant="tonal">
        {{ buttonName }}
    </v-btn>
</template>

<script>
    export default {
        data() {
            return {
               
            }
        },
        props: {       
            buttonName: String
        }
    }
</script>


