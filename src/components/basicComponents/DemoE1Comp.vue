<!--declares a demo component, No. is DemoE1
  this chapter is about "slot" and its content distributions.
  main point is following:
    1. <slot> is an outlet for content distribution.
    插槽一共就三大类
1.匿名插槽(也叫默认插槽): 没有命名,有且只有一个
2.具名插槽: 相对匿名插槽组件slot标签带name命名的
3.作用域插槽: 子组件内数据可以被父页面拿到(解决了数据只能从父页面传递给子组件)

在用上v-slot之后 只需要考虑好
1.是否需要命名(匿名插槽,具名插槽)
2.父页面是否需要取存在子页面的数据(作用域插槽)

-->
<template>
  <fieldset>
    <legend align="left">DemoE1 slot and content distributions</legend>
    <fieldset>
      <legend align="left">DemoE1-1 named slots</legend>
      <span>
        <DemoE1CompSub1Fill></DemoE1CompSub1Fill>
      </span>
    </fieldset>
    <fieldset>
      <legend align="left">DemoE1-2 scoped slots</legend>
      <span>
        <DemoE1CompSub2Fill></DemoE1CompSub2Fill>
      </span>
    </fieldset>
  </fieldset>
</template>

<script>
import DemoE1CompSub1Fill from './DemoE1CompSub1Fill'
import DemoE1CompSub2Fill from './DemoE1CompSub2Fill'

import { defineComponent } from 'vue'
export default defineComponent({
  name: 'DemoE1Comp',
  components: {
    DemoE1CompSub1Fill: DemoE1CompSub1Fill,
    DemoE1CompSub2Fill: DemoE1CompSub2Fill
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
