<template>
    <div class="combo-box">
        <v-combobox
        :label="showLabel ? label : ''"
        :items="data"
        @update:search="updateValue"
        bg-color="white"
        theme="light"
        v-model="value"
        clearable
        density="compact">
        </v-combobox>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                value: null,
                showLabel: true
            }
        },
        props: {
            data: Array,
            label: String
        },
        methods: {
            updateValue(value) {
                if (value === '')
                    this.showLabel = true;
                else 
                    this.showLabel = false;
                
                this.$emit('selected', value)
            },
            clearValue() {
                this.value = null
            }
        },
    }
</script>


