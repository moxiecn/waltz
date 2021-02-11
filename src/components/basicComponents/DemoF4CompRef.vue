<!--declares a demo component, No. is DemoF4
  this chapter is about reference of template elements.
  in other words,how to operate HTML DOM objects with VUE.
  ref + this.$refs
-->
<template>
  <div id="DemoF4CompRef">
    <fieldset>
      <legend align="left">DemoF4</legend>
      <span>
        <input ref="myRef" id="myRef" value="refValue." />
        <button @click="change">change</button>
      </span>
    </fieldset>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
export default defineComponent({
  name: 'DemoF4CompRef',
  methods: {
    change: function() {
      // this.$refs.myRef.value = 'ddddd'
      // under typescript,the type of $refs must be explicitly specified. this is designated as "any".
      ;(this.$refs.myRef as any).value = 'ddddd'
      alert('myRdf input element has already changed. ' + (document.getElementById('myRef') as any).value)
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
  padding: 0;
}
li {
  margin: 0 10px;
}
a,
span {
  color: red;
}
</style>
