<!--declares a demo component, No. is DemoAb-1.

-->
<template>
  <fieldset>
    <legend align="left">B1-1: binding HTML class</legend>
    <span class="static" :class="{ active: isActive, 'text-danger': hasError }"
      >操作元素的 class 列表和内联样式是数据绑定的一个常见需求。因为它们都是 attribute，</span
    >
    <p />
    <span :class="classObj"
      >所以我们可以用 v-bind 处理它们：只需要通过表达式计算出字符串结果即可。不过，字符串拼接麻烦且易错。</span
    >
    <p />
    <span :class="classObjCp"
      >因此，在将 v-bind 用于 class 和 style 时，Vue.js
      做了专门的增强。表达式结果的类型除了字符串之外，还可以是对象或数组。</span
    >
  </fieldset>
  <fieldset>
    <legend align="left">B1-2: binding inline style</legend>
    <span :style="{ color: activeColor, fontSize: fontSize + 'px' }"
      >操作元素的 class 列表和内联样式是数据绑定的一个常见需求</span
    >
    <p />
    <span :style="styleObject">操作元素的 class 列表和内联样式是数据绑定的一个常见需求</span>
    <p />
  </fieldset>
</template>

<script>
import { defineComponent } from 'vue'
export default defineComponent({
  name: 'DemoB1ClassStyle',
  data() {
    return {
      /// ////// for class
      isActive: true,
      hasError: false,
      classObj: {
        active: true,
        'text-danger': false
      },
      /// ////// for style
      activeColor: 'red',
      fontSize: 30,
      styleObject: {
        color: 'red',
        fontSize: '13px'
      }
    }
  },
  computed: {
    classObjCp() {
      return {
        active: this.isActive && !this.error,
        'text-danger': this.error && this.error.type === 'fatal'
      }
    }
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
