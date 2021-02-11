<!--declares a demo component, No. is DemoF1
  this chapter is about "provide" and "inject".
  for more details,
  https://vue3js.cn/docs/zh/guide/component-provide-inject.html#处理响应性

-->
<template>
  <div id="DemoF1CompSub1Child1">
    <fieldset>
      <legend align="left">DemoF1-child</legend>
      <span>
        <div>this is child, but there isn't user property here.</div>
        <DemoF1CompSub1GrandSon1></DemoF1CompSub1GrandSon1>
      </span>
    </fieldset>
  </div>
</template>

<script>
import DemoF1CompSub1GrandSon1 from './DemoF1CompSub1GrandSon1'
import { defineComponent } from 'vue'
export default defineComponent({
  name: 'DemoF1CompSub1Child1',
  components: {
    DemoF1CompSub1GrandSon1: DemoF1CompSub1GrandSon1
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
