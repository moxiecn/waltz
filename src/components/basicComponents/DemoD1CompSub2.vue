<!--declares a demo component, No. is DemoD2
  this demo is about custom event of component, $emit(), this is a simplest demo.
-->
<template>
  <div id="DemoD1CompSub2">
    <span>
      <span v-bind:style="{ fontSize: titleFontSize + 'em' }">{{ index1 }}:{{ title }}</span>
      <button v-on:click="doenlarge(index1)">Enlarge</button>
      <button @click="doreduce(index1)">Reduce</button>
    </span>
  </div>
</template>

<script>
import { defineComponent } from 'vue'
export default defineComponent({
  name: 'DemoD1CompSub2',
  props: ['title', 'index1', 'titleFontSize'],
  emits: ['eventEnlarge', 'eventRecude'],
  methods: {
    doenlarge: function(index) {
      this.$emit('eventEnlarge', index) // the first parament "eventEnlarge" is a custom event inside parent component.
    },
    doreduce: function(index) {
      this.$emit('eventReduce', index, index + 100) // here there are 2 value to be emited. in parent component, the value of
      // "v-on:eventReduce" fill just in function name, such as "doReduce1", no need to fill in parameter name.
      // doReduce1 function will get "index,index100" 2 parameters automatically.
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
