<!--declares a demo component, No. is DemoD1-6
  what the demo shows is about "props".
-->
<template>
  <div id="DemoD1CompSub6">
    <span>
      the value passed in from parent component is :
      <input v-bind:value="initValue" />
      {{ initValue }}, <br />internal computed property : <input v-bind:value="internalCP" />, <br />internal data value
      :
      <input v-bind:value="internalValue" />
      {{ internalValue }}, <button @click="doChange">use internalValue to change</button><br />
      {{ probD }}
    </span>
  </div>
</template>

<script>
import { defineComponent } from 'vue'
export default defineComponent({
  name: 'DemoD1CompSub6',
  props: {
    initValue: String, // specifies a props "initValue", it used to receive datas from parent component.
    // but it is not recommended to change value of this property directly inside this component.
    // so declare a data "internalValue" to use "initValue" property indirectly.This practice is offically recommended.

    // 基础的类型检查 (`null` 和 `undefined` 会通过任何类型验证)
    propA: Number,
    // 多个可能的类型
    propB: [String, Number],
    // 必填的字符串
    propC: {
      type: String,
      required: true
    },
    // 带有默认值的数字
    propD: {
      type: Number,
      default: 100
    },
    // 带有默认值的对象
    propE: {
      type: Object,
      // 对象或数组默认值必须从一个工厂函数获取
      default: function() {
        return { message: 'hello' }
      }
    },
    // 自定义验证函数
    propF: {
      validator: function(value) {
        // 这个值必须匹配下列字符串中的一个
        return ['success', 'warning', 'danger'].indexOf(value) !== -1
      }
    },
    // 具有默认值的函数
    propG: {
      type: Function,
      // 与对象或数组默认值不同，这不是一个工厂函数 —— 这是一个用作默认值的函数
      default: function() {
        return 'Default function'
      }
    }
  },
  data: function() {
    return {
      internalValue: this.initValue
    }
  },
  computed: {
    internalCP: function() {
      return this.initValue.toUpperCase()
    }
  },
  methods: {
    doChange: function() {
      this.internalValue = this.initValue + ' is changed.'
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
