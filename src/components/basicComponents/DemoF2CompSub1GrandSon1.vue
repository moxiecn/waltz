<!--declares a demo component, No. is DemoF1
  this chapter is about "provide" and "inject".
  for more details,
  https://vue3js.cn/docs/zh/guide/component-provide-inject.html#处理响应性

-->
<template>
  <div id="DemoF2CompSub1GrandSon1">
    <fieldset>
      <legend align="left">DemoF1-grandson</legend>
      <span>
        <div>
          this is grandson,the following is from root component:<br />
          user: {{ user }}<br />
          todos: {{ todos }}<br />
          todoLength:{{ todoLength }}
        </div>
      </span>
    </fieldset>
  </div>
</template>

<script>
import { defineComponent } from 'vue'
export default defineComponent({
  name: 'DemoF2CompSub1GrandSon1',
  inject: ['user', 'todos', 'todoLength'],
  created() {
    console.log(`Injected property: ${this.user}`) // > 注入 property: John Doe
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
