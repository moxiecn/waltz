<!--declares a demo component, No. is DemoD1-5
  what the demo shows is about dynamic components.
-->
<template>
  <div id="DemoD1CompSub5">
    <span>
      <div class="demo-alert-box">
        <strong>Error!</strong>
        <slot></slot>
      </div>
    </span>
  </div>
</template>

<script>
import { defineComponent } from 'vue'
export default defineComponent({
  name: 'DemoD1CompSub5'
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
