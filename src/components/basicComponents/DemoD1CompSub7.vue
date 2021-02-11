<!--declares a demo component, No. is DemoD1-7
  what the demo shows is about "non-prop" attributes.
  When the parent component calls this component, 2 properties are passed in, however,
    these 2 properties are not defined in this component through "props" or "$emit()".
  in this case, the rule of VUE is that the undefined attributes (called "non-prop attributes") passed in by parent components
    will be mounted automatically to the root node of this component(wether is a native or custom),
    which can be verfied by the message output by "console.log(this.$attrs)".
  for more please refer to:
  https://vue3js.cn/docs/zh/guide/component-attrs.html#attribute-继承
  https://vue3js.cn/docs/zh/guide/component-attrs.html#禁用-attribute-继承
  https://vue3js.cn/docs/zh/guide/component-attrs.html#多个根节点上的-attribute-继承
-->
<template>
  <div id="DemoD1CompSub7">
    <div class="date-picker">
      <input type="datetime" />
    </div>
  </div>
</template>

<script>
import { defineComponent } from 'vue'
export default defineComponent({
  name: 'DemoD1CompSub7',
  created() {
    console.log("DemoD1CompSub7's attributes:" + this.$attrs) // { onChange: () => {}  }
    console.log(this.$attrs) // { onChange: () => {}  }
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
