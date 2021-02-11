<!--declares a demo component, No. is DemoF1
  this chapter is about "provide" and "inject".
  for more details,
  https://vue3js.cn/docs/zh/guide/component-provide-inject.html#处理响应性

-->
<template>
  <div id="DemoF1CompSub1Root">
    <fieldset>
      <legend align="left">DemoF1-root provide/inject</legend>
      <span>
        <div>
          the length of todos array is {{ todos.length }}.
          <br />
          user is (), because it provided.
          <!-- 模板的其余部分 -->
        </div>
        <DemoF1CompSub1Child1></DemoF1CompSub1Child1>
      </span>
    </fieldset>
  </div>
</template>

<script>
import DemoF1CompSub1Child1 from './DemoF1CompSub1Child1'
import { defineComponent } from 'vue'
export default defineComponent({
  name: 'DemoF1CompSub1Root',
  data() {
    return {
      todos: ['Feed a cat', 'Buy tickets']
    }
  },
  provide: {
    user: 'John Doe',
    todos: ''
  },
  components: {
    DemoF1CompSub1Child1: DemoF1CompSub1Child1
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
