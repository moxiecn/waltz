<!--declares a demo component, No. DemoE1-1
  this example is about usage of v-slot.
  this custom component is called by DemoE1Comp component to be used to show final pages.
  this is a child component.
-->
<template>
  <div id="DemoE1CompSub1Fill">
    <span>
      <DemoE1CompSub1Todo>
        <template v-slot:header>
          <DemoE1CompSub1Header></DemoE1CompSub1Header>
        </template>
        <template v-slot:default>
          <DemoE1CompSub1Content></DemoE1CompSub1Content>
        </template>
        <template v-slot:footer>
          <DemoE1CompSub1Footer></DemoE1CompSub1Footer>
        </template>
      </DemoE1CompSub1Todo>
    </span>
  </div>
</template>

<script>
import DemoE1CompSub1Todo from './DemoE1CompSub1Todo'
import DemoE1CompSub1Header from './DemoE1CompSub1Header'
import DemoE1CompSub1Footer from './DemoE1CompSub1Footer'
import DemoE1CompSub1Content from './DemoE1CompSub1Content'

import { defineComponent } from 'vue'
export default defineComponent({
  name: 'DemoE1CompSub1Fill',
  components: {
    DemoE1CompSub1Todo: DemoE1CompSub1Todo,
    DemoE1CompSub1Header: DemoE1CompSub1Header,
    DemoE1CompSub1Footer: DemoE1CompSub1Footer,
    DemoE1CompSub1Content: DemoE1CompSub1Content
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
