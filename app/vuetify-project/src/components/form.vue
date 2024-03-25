<template>
    <div class="container">
        <div class="form">
            <div class="form-header">
                <BanknotesIcon class="h-6 w-6 text-blue-500" />
                <p>Calcule o valor da viagem</p>
            </div>
            <div class="box">
                <label for="">Destino</label>
                <combo-box ref="childBoxComponentRef" :data="cityList" label="Selecione o destino" @selected="(value) => this.selectedCity = value"/>
            </div>
            <div class="date">
                <label for="">Data</label>
                <VueDatePicker :min-date="new Date()" v-model="date" placeholder="Selecione uma data" :enable-time-picker="false"
                input-class-name="dp-custom-input"/>
            </div>
            <div class="button">
                <Button buttonName="Buscar" @click="submitForm" theme="light"></Button>
            </div>
        </div>
        <Dialog ref="childComponentRef" text="Insira os valores para iniciar a cotação" buttonText="Fechar" theme="purple"></Dialog>
    </div>  
</template>

<script>
    import comboBox from './comboBox.vue';
    import VueDatePicker from '@vuepic/vue-datepicker';
    import Button from './button.vue'
    import dialog from './dialog.vue'
    import { BanknotesIcon } from '@heroicons/vue/24/outline'
    
    import '@vuepic/vue-datepicker/dist/main.css'

    export default {
        data() {
            return {
                selectedCity: null,
                citiesData: null,
                cityList: [],
                date: null,
            }
        },
        created() {
            this.getCities();         
        },  
        components: {
            comboBox,
            VueDatePicker,
            Button,
            dialog,
            BanknotesIcon
        },
        methods: {
            submitForm(e) {
                e.preventDefault();

                if (!this.selectedCity || !this.date) 
                    return this.$refs.childComponentRef.dialog = !this.$refs.childComponentRef.dialog;
                
                let selectedCities = []

                this.citiesData.forEach(cityData => {
                    if (cityData.city === this.selectedCity) {
                        selectedCities.push(cityData);
                    }
                })

                this.findTravels(selectedCities);
            },
            getCities() {
                fetch('http://127.0.0.1:3000/transport')
                .then(response => {
                    response.json()
                        .then(responseJson => {
                            this.citiesData = responseJson;
                            responseJson.forEach(cityData => {
                                this.cityList.push(cityData.city);
                            })
                        })
                })
                .catch(error => {
                    console.log(error);
                })
            },
            findTravels(selectedCities) {
                const fastTravel = this.findFastTravel(selectedCities);
                const economicTravel = this.findEconomicTravel(selectedCities);

                this.$emit('data', {
                    fastTravel,
                    economicTravel
                })
            },
            findFastTravel(selectedCities) {
                // find fastest and more confort travel
                let bestTravel = undefined;
                
                if (selectedCities[0]) 
                    bestTravel = selectedCities[0];

                selectedCities.forEach(cityData => {
                    if (parseInt(cityData.duration.split('h').at(0)) < parseInt(bestTravel.duration.split('h').at(0))) {
                        bestTravel = cityData;
                    } else if (parseInt(cityData.duration.split('h').at(0)) === parseInt(bestTravel.duration.split('h').at(0))){
                        if (parseFloat(cityData.price_confort.split('R$ ').at(1)) > parseFloat(bestTravel.price_confort.split('R$ ').at(1))) 
                            bestTravel = cityData;
                    }
                })

                return bestTravel;
            },
            findEconomicTravel(selectedCities) {
                // find best economic travel
                let economicTravel = undefined;
                
                if (selectedCities[0]) 
                    economicTravel = selectedCities[0];

                selectedCities.forEach(cityData => {
                    if (parseFloat(cityData.price_econ.split('R$ ').at(1)) < parseFloat(economicTravel.price_econ.split('R$ ').at(1))) 
                        economicTravel = cityData;
                })

                return economicTravel;
            },
            clearForm() {
                this.date = null;
                this.$refs.childBoxComponentRef.clearValue();
            }
        }
    }
</script>

<style lang="scss">
    .dp-custom-input {
        --dp-input-padding: 10px 30px 6px 12px; 
    }

    .dp-custom-input:hover {
        background-color: #e7e7e7;
    }
</style>

<style scoped>
    body{
        display: flex;
        align-items: center;
    }

    .container {
        display: flex;
        justify-content: center;
    }

    .form {
        display: flex;
        flex-direction: column;
        width: 80%;
        height: 100%;
        margin-top: 10%;
    }

    .form > p {
        font-size: 130%;
    }

    .box {
        margin-top: 3vh;
    }

    .combo-box {
        width: 100%;
    }

    .date {
        margin: 0;
    } 

    Button {
        margin-top: 6vh;
        width: 100%;
    }

    .form-header {
        display: flex;
        flex-direction: row;
    }

    .form-header > p {
        font-size: 120%;
        display: flex;
        flex-direction: row;
    }

    .text-blue-500 {
        margin: 0;
        margin-right: 4%;
        width: 12%;
        height: auto;
    }
</style>





