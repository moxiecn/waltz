<!--declares the first demo component, No. is DemoA1.
    this component shows the value of a Counter in browser.
-->
<template>
  <div id="demoA1Counter">
    <fieldset title="[in,tә:pәu'leiʃәn] n. 篡改, 添写, 插补【计】内推法; 内插法">
      <legend align="left">A1 interpolation</legend>
      Counter: {{ counter }}
    </fieldset>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
export default defineComponent({
  // defines name for this component. this name will be used by the parent component that uses this component.
  // in other words, in RootApp.vue, use the name like this <DemoA1Counter></DemoA1Counter>
  name: 'DemoA1Counter',
  data() {
    return {
      data1: 'adsf',
      da: 'df'
    }
  },
  props: {
    // defines custom property "counter" of the "DemoA1Counter" component .
    counter: String
  },
  mounted() {
    // alert(this.da)
  }
})
</script>

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

a {
  color: #42b983;
}
</style>
