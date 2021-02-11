<!--declares a demo component, No. DemoE1-2
  this example is about usage of scoped slots.
  this is a root component which imported Todo comopnents. it can define some slot in todo
  components. yet here, can fill in slot contents to the todo components.
  in this example, we declare a scope for v-slot called "slotProps"(this name can named at will),
  so that in this child component we can access todos' data.
  in addtional, please refer to :
  https://vue3js.cn/docs/zh/guide/component-slots.html#独占默认插槽的缩写语法
  https://vue3js.cn/docs/zh/guide/component-slots.html#解构插槽-prop
  https://vue3js.cn/docs/zh/guide/component-slots.html#动态插槽名
  https://vue3js.cn/docs/zh/guide/component-slots.html#具名插槽的缩写
-->
<template>
  <div id="DemoE1CompSub2Fill">
    <span>
      <DemoE1CompSub2Todo>
        <template v-slot:scoped-slots1="slotProps">
          <i class="fas fa-check"></i>
          <span class="green">{{ slotProps.item1 + '.--' }}</span>
        </template>
      </DemoE1CompSub2Todo>
    </span>
  </div>
</template>

<script>
import DemoE1CompSub2Todo from './DemoE1CompSub2Todo'
import { defineComponent } from 'vue'
export default defineComponent({
  name: 'DemoE1CompSub2Fill',
  components: {
    DemoE1CompSub2Todo: DemoE1CompSub2Todo
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
