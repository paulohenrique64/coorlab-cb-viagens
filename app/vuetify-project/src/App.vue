<template>
  <div class="all">
    <div class="lateral-menu">
      <div class="image">
        <img src="./assets/logo-cb-viagens.png" alt="">
      </div>
      <a class="menu-item" href="http://127.0.0.1:8080/"><CalculatorIcon class="h-6 w-6 text-blue-500" /><p>Calculadora de Viagem</p></a>
    </div>
    <div class="container-all-0">
      <div class="container-all"> 
        <div class="container-header">
          <TruckIcon class="h-6 w-6 text-blue-500" />
          <p>Calculadora de Viagem</p>
        </div>
        <div class="container">
          <div class="left-side">
            <div class="form">
              <Form ref="childComponentRef" @data="(result) => updateData(result)"></Form>
            </div>
          </div>  
          <div class="right-side">
            <p v-if="fastTravel || economicTravel">Estas são as melhores alternativas de viagem para a data selecionada</p>
            <TravelCard v-if="fastTravel" :data="fastTravel" :economic="false"/>
            <TravelCard v-if="economicTravel" :data="economicTravel" :economic="true"/>
            <div class="button" v-if="fastTravel || economicTravel">
              <Button buttonName="Limpar" @click="clearData" theme="light"></Button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>  
</template>

<script>
  import Form from './components/form.vue'
  import TravelCard  from './components/travelCard.vue'
  import { TruckIcon, CalculatorIcon } from '@heroicons/vue/24/outline'

  export default {
    data() {
      return {
        fastTravel: null,
        economicTravel: null
      }
    },
    components: {
      Form,
      TravelCard,
      TruckIcon,
      CalculatorIcon
    },
    methods: {
      updateData(result) {
        this.fastTravel = result.fastTravel;
        this.economicTravel = result.economicTravel;
      },
      clearData() {
        this.$refs.childComponentRef.clearForm();
        this.fastTravel = null,
        this.economicTravel = null
      }
    }
  }
</script>

<style>
  body {
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #e9f9fc;
    color: black;
    overflow-x: auto;
  }

  #app {
    width: 100%;
  }

  .all {
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
  }

  .lateral-menu {
    background-color: #2b4348;
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.8);
    min-width: 45vh;
    max-width: 45vh;
    height: 100vh;
    color: #fff;
  }

  .lateral-menu > .image {
    margin: 8% 8% 8%;
  }

  .lateral-menu > .image > img {
    height: auto;
    width: 30vh;
  }

  .lateral-menu > a > .text-blue-500 {
    margin: 0;
    margin-left: 7%;
    width: 10%;
    height: auto;
  }

  .menu-item {
    color: #fff;
    display: flex;
    align-items: center;
    height: 7vh;
    width: auto;
    text-decoration: none; 
  }

  .menu-item > p {
    font-weight: 600;
    font-size: 110%;
    margin-left: 4%;
  }

  .menu-item:hover {
    background-color: #1d2d30;
  }

  .container-all-0 {
    height: 100%;
    width: 100%;
    display: flex;
    justify-content: center;
    margin: 0;
  }

  .container-all {
    box-shadow: 0px 0px 40px 0px rgba(0, 0, 0, 0.3);
    border-radius: 8px;
    width: 80%;
  }

  .container-header {
    background-color: #2b4348;
    height: 9vh;
    width: auto;
    display: flex;
    align-items: center;
    border-radius: 8px 8px 0 0;
    color: #fff;
  }

  .container-header > p {
    font-weight: 600;
    font-size: 130%;
    margin-left: 2%;
  }

  .container-all > .container {
    display: flex;
    flex-direction: row;
    width: 100%;
    height: auto;
    background-color: #e9f9fc;
    border-radius: 10px;
  }

  .left-side {
    margin: 2% 1% 2% 2%;
    width: 45%;
    height: 65vh;
    background-color: #caf1f8;
    border-radius: 8px 0px 0px 8px;
  }

  .form {
    margin-left: 2vh;
  }

  .right-side {
    margin: 2% 2% 2%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100vh;
    height: 65vh;
    border-radius: 8px;
  }

  .right-side > p {
    margin-top: 5%;
    margin-left: 2%;
    font-size: 130%;
  }

  .right-side > .button {
    height: 100%;
    display: flex;
    justify-content: end;
    align-items: end;
    margin: 0 2% 2%;
  }

  .right-side > .button > .v-btn {
    background-color: rgb(255, 148, 129);
  }

  .text-blue-500 {
    margin-left: 2%;
    width: 3.5%;
    height: auto;
  }

  @media screen and (max-width: 1366px) and (max-height: 768px) {
    body {
      font-size: 11px; 
    }
  }
  
</style>




