<!--declares a demo component, No. is DemoD1-3_3
  a advanced usage about v-mode modifiers on a custom component.
  in this example, we design 2 types of modifiers. one is the prop based on default nameing rules,
    such as modelValue and modelModifier, and the other is custom naming prop and modifier, it is
    named "foo" and "fooModifiers".
  both modifiers repsond to "input" event of "<input>" tag.
  for more, please should refer to:<template>
    https://vue3js.cn/docs/zh/guide/component-custom-events.html#处理-v-model-修饰符
-->
<template>
  <div id="DemoD1CompSub33">
    <span>
      capitalize the 1st letter:
      <input type="text" :value="modelValue" @input="emitValue" />
      C:{{ modelValue }}
      <input type="text" :value="foo" @input="emitValueFoo" />
      C:{{ foo }}
      <br />
    </span>
  </div>
</template>

<script>
import { defineComponent } from 'vue'
export default defineComponent({
  name: 'DemoD1CompSub33',
  props: {
    modelValue: String, // default named
    modelModifiers: {
      // modelModifiers is default named
      // eslint-disable-next-line @typescript-eslint/no-empty-function
      default: () => {}
    },
    foo: String, // this is a custom prop,
    // so its modifier will must conform to the naming rules of arg+"Modifiers".
    // so it is named "fooModifiers".
    fooModifiers: {
      default: () => {}
    }
  },
  emits: ['update:vtitle', 'update:foo'],
  methods: {
    emitValue(e) {
      let value = e.target.value
      if (this.modelModifiers.capitalize1) {
        // in here, modifier name "capitalize1" is can be defined at will.
        // write the logic for capitcalizing the first letter.
        value = value.charAt(0).toUpperCase() + value.slice(1)
      }
      this.$emit('update:modelValue', value)
    },
    emitValueFoo(e) {
      let value = e.target.value
      if (this.fooModifiers.lowercasefoo) {
        value = value.charAt(0).toLowerCase() + value.slice(1)
      }
      this.$emit('update:foo', value)
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
