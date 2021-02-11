<!--declares a demo component, No. is DemoD1-3
  what the demo shows is a custom component how to support v-model bidirectional features.
  in this example, v-mode on this custom component uses "modelValue" property as "props", and "update:modelValue" as update event on "modelValue".
-->
<template>
  <div id="DemoD1CompSub3">
    <span>
      component sn:{{ sn }},
      <input v-bind:value="modelValue" v-on:input="$emit('update:modelValue', $event.target.value)" />
      {{ modelValue }}
      <br />
    </span>
  </div>
</template>

<script>
import { defineComponent } from 'vue'
export default defineComponent({
  name: 'DemoD1CompSub3',
  props: ['modelValue', 'sn']
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
