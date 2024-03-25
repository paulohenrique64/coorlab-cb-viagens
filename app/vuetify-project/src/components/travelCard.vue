<template>
    <div class="parent">
        <div class="container">
            <div class="image">
                <img v-if="economic" src="../assets/price.png" alt="">
                <img v-else src="../assets/timer.png" alt="">
            </div>
            <div class="travel-data">
                <div class="travel-details">
                    <p class="travel-name">{{ data.name }}</p>
                    <p v-if="economic">Poltrona: {{ data.seat }} (Convencional)</p>
                    <p v-else>Leito: {{ data.seat }} (Completo)</p>
                    <p>Tempo estimado: {{ data.duration }}</p>
                </div>
            </div>
        </div>
        <div class="travel-price-container">
            <div class="travel-price">
                <p class="price-tag">Preço</p>
                <p v-if="economic">{{ data.price_econ }}</p>
                <p v-else>{{ data.price_confort }}</p>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
            }
        },
        props: {
            data: Object,
            economic: Boolean
        }
    }
</script>

<style scoped>
    .parent {
        display: flex;
        flex-direction: row;
        margin: 2% 0% 1%;
        color: black;
    }

    .container {
        margin: 0;
        display: flex;
        flex-direction: row;
        width: 70%;
        height: 15vh;
        background-color: #caf1f8;
        border-radius: 10px;
    }

    .image {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 30%;
        background-color: #91e0ef;
        border-radius: 10px 0 0 10px;
    }

    img {
        height: auto;
        width: 10vh;
    }

    .travel-data {
        display: flex;
        flex-direction: row;
        margin: 5% 5% 5%;
    }

    .travel-price-container {
        margin-left: 2%;
        width: 30%;
        height: 15vh;
        background-color: #caf1f8;
        border-radius: 10px;
    }

    .travel-price {
        margin: 15% 20% 10%;
    }

    .travel-price > .price-tag, .travel-name {
        font-weight: 600;
    }

    .travel-price-container:hover {
        background-color: #91e0ef;
        cursor: pointer;
    }
</style>