<!--declares a demo component, No. is DemoF1
  this chapter is about "provide" and "inject".
  for more details,
  https://vue3js.cn/docs/zh/guide/component-provide-inject.html#处理响应性

-->
<template>
  <div id="DemoF1Comp">
    <fieldset>
      <legend align="left">DemoF1 provide/inject</legend>
      <fieldset>
        <legend align="left">DemoF1-1 simplest</legend>
        <span>
          <DemoF1CompSub1Root> </DemoF1CompSub1Root>
        </span>
      </fieldset>
      <fieldset>
        <legend align="left">DemoF1-2 uses provide(){}</legend>
        <span>
          <DemoF2CompSub1Root> </DemoF2CompSub1Root>
        </span>
      </fieldset>
      <fieldset>
        <legend align="left">DemoF1-3 Async Components</legend>
        <span>
          <DemoF3CompRoot> </DemoF3CompRoot>
        </span>
      </fieldset>
      <fieldset>
        <legend align="left">DemoF1-4 templates refs</legend>
        <span>
          <DemoF4CompRef> </DemoF4CompRef>
        </span>
      </fieldset>
    </fieldset>
  </div>
</template>

<script>
import DemoF1CompSub1Root from './DemoF1CompSub1Root'
import DemoF2CompSub1Root from './DemoF2CompSub1Root'
import DemoF3CompRoot from './DemoF3CompRoot'
import DemoF4CompRef from './DemoF4CompRef'

import { defineComponent } from 'vue'
export default defineComponent({
  name: 'DemoF1Comp',
  components: {
    DemoF1CompSub1Root: DemoF1CompSub1Root,
    DemoF2CompSub1Root: DemoF2CompSub1Root,
    DemoF3CompRoot: DemoF3CompRoot,
    DemoF4CompRef: DemoF4CompRef
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
