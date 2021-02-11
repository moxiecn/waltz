<!--declares a demo component, No. is DemoA4.
    this component will demo a usage of "v-on" dictate.
-->
<template>
  <fieldset>
    <legend align="left">A4 v-on</legend>
    <span v-bind:title="message">
      <p>{{ message }}</p>
      <!--specifies event click of the <button> tag  by v-on instruction to "reverseMessage" custom function-->
      <button v-on:click="reverseMessage">reverse a Message</button>
    </span>
  </fieldset>
</template>

<script>
import { defineComponent } from 'vue'
export default defineComponent({
  name: 'DemoA4VOn',
  data() {
    return {
      message: 'Hello Vue.js!'
    }
  },
  methods: {
    reverseMessage() {
      this.message = this.message // reverses every character of this.message and assign it back to this.message.
        .split('')
        .reverse()
        .join('')
    }
  }
})
</script>
//
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a,
span {
  color: red;
}
</style>
