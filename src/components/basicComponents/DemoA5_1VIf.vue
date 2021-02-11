<!--declares a demo component, No. is DemoA5_1.
    this component will demo a usage of "v-if,v-else,v-else-if" dictate.
-->
<template>
  <fieldset>
    <legend align="left">A5_1 v-if,v-else-if,v-else</legend>
    <span v-if="seen">Now you have seen me.</span>
    <span v-else-if="seen === false">Now you can not see me.</span>
    <span v-else>nothing.</span>
    <button v-on:click="seen = !seen">switch it</button>
    <button v-on:click="reserveIt">switch it by reserveIt</button>
    <transition name="fade">
      <span>{{ seen }}</span>
    </transition>
  </fieldset>
</template>

<script>
import { defineComponent } from 'vue'
export default defineComponent({
  name: 'DemoA51VIf',
  data() {
    return {
      seen: true
    }
  },
  methods: {
    reserveIt() {
      this.seen = this.seen !== true
    }
  }
})
</script>
//
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

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
