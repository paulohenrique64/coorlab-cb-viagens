<template>
  <div class="text-center pa-4">
    <v-dialog
      v-model="dialog"
      width="auto"
      theme="light"
    >
      <v-card
        max-width="400"
        prepend-icon="mdi-alert-circle"
        :text="text"
        :title="title"
      >
        <template v-slot:actions>
          <v-btn
            class="ms-auto"
            :text="buttonText"
            @click="dialog = false"
          ></v-btn>
        </template>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        dialog: false,
      }
    },
    props: {
      text: String,
      title: String,
      buttonText: String,
    }
  }
</script>



