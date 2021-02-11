<!--declares a demo component, No. is DemoD2_1
  this demo is about some validation of emitted event.
-->
<template>
  <div id="DemoD1CompSub2_1">
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
  name: 'DemoD1CompSub21',
  props: ['title', 'index1', 'titleFontSize'],
  emits: {
    eventEnlarge: function(index) {
      // in here, verify the method specfied in $emit in "methods".
      // only through the validatoin here , the event specified by $emit in "doenlarge" method can be continued.
      // otherwise, the event defined by $emit will not be executed.
      alert(index)
      if (index) {
        if (index >= 1) {
          alert('index passed validation.')
          return true
        } else {
          alert('index failed validation. index<1.')
          return false
        }
      } else {
        alert('index failed validation. index is null or undefined.')
        return false
      }
    },
    eventRecude: null
  },

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
