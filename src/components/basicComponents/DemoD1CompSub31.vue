<!--declares a demo component, No. is DemoD1-3_1
  a advanced usage about v-mode on a custom component.
  According to the property inheritance rule in SUB7, can modify name of "modelValue" by passing an argument to v-model.
  for example, in this case, we will replaces "modelValue" with "vtitle".
  for more ,https://blog.csdn.net/weixin_40642141/article/details/111769719
-->
<template>
  <div id="DemoD1CompSub31">
    <span>
      component sn:{{ sn }},
      <input v-bind:value="vtitle" v-on:input="$emit('update:vtitle', $event.target.value)" />
      {{ vtitle }}
      <br />
    </span>
  </div>
</template>

<script>
import { defineComponent } from 'vue'
export default defineComponent({
  name: 'DemoD1CompSub31',
  props: ['vtitle', 'sn'],
  emits: ['update:vtitle'],
  // setup(props, context){
  setup(props) {
    console.log('SUB31.props:')
    console.log(props)
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
