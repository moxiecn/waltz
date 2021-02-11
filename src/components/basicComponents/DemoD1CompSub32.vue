<!--declares a demo component, No. is DemoD1-3_2
  Multiple v-model bindings
-->
<template>
  <div id="DemoD1CompSub32">
    <span>
      component sn:{{ sn }},
      <input v-bind:value="vserach5" v-on:input="$emit('update:vserach5', $event.target.value)" />
      {{ vserach5 }}
      <br />
      <input v-bind:value="vserach6" v-on:input="$emit('update:vserach6', $event.target.value)" />
      {{ vserach6 }}
      <br />
    </span>
  </div>
</template>

<script>
import { defineComponent } from 'vue'
export default defineComponent({
  name: 'DemoD1CompSub32',
  props: ['vserach5', 'vserach6', 'sn'],
  emits: ['update:vserach5', 'update:vserach6']
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
