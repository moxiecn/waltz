<!--declares a demo component, No. is DemoA8.
    Why Lodash?
    Lodash makes JavaScript easier by taking the hassle out of working with arrays, numbers, objects, strings, etc.
    Lodash’s modular methods are great for:
      Iterating arrays, objects, & strings
      Manipulating & testing values
      Creating composite functions
-->
<template>
  <fieldset>
    <legend align="left">A8 debounce base on LOADSH</legend>
    <button v-on:click="myDebounce">test loadsh-myDebounce</button>
    <button v-on:click="_myDebounce">test loadsh-_myDebounce</button>
  </fieldset>
</template>

<script>
import { debounce } from 'loadsh'
import { defineComponent } from 'vue'
const _ = require('loadsh')
export default defineComponent({
  name: 'DemoA8Loadsh',
  data: function() {
    return {
      test: String
    }
  },
  created() {
    // 不用Lodash而自定义的防抖函数，延迟2000毫秒
    this.dbf01 = debounce(this.myDoit, 2000, false)
    // 用 Lodash 的防抖函数
    this.dbf02 = _.debounce(this.myDoitLoadsh, 2000, false)
  },
  unmounted() {
    // 移除组件时，取消定时器
    this.dbf01.cancel()
    this.dbf02.cancel()
    // this.debouncedClick.cancel();
  },
  methods: {
    myDoit: function() {
      // working function actually executed on my custom.
      alert('this my normal function myDoit. 2000ms have passed')
    },
    myDoitLoadsh: function() {
      // working function actually executed base on loadsh.
      alert('this my loadsh debounce function myDoitLoadsh.  2000ms have passed')
    },
    myDebounce: function() {
      // bind to <button> tag, call dbf01 variable of this component by built in created hook funcion.
      this.dbf01()
    },
    _myDebounce: function() {
      // bind to <button> tag,
      this.dbf02()
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
