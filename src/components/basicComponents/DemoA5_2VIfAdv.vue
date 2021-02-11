<!--declares a demo component, No. is DemoC1-1.

-->
<template>
  <fieldset>
    <legend align="left">A5_2(C1-1): v-if,v-else,v-else-if</legend>
    <span>template</span>
    <template v-if="ok">
      <h1>Title</h1>
      <p>Paragraph 1</p>
      <p>Paragraph 2</p>
    </template>
    <span>if else</span>
    <div v-if="Math.random() > 0.5">Now you see me</div>
    <div v-else>Now you don't</div>
    <p />
    <span>if elseif else</span>
    <div v-if="type === 'A'">A</div>
    <div v-else-if="type === 'B'">B</div>
    <div v-else-if="type === 'C'">C</div>
    <div v-else>Not A/B/C</div>
  </fieldset>
  <fieldset>
    <legend align="left">A5_2(C1-2): v-show</legend>
    <span>
      <h1 v-show="ok">Hello!</h1>
      <span v-show="ok">
        v-if is "real" conditional rendering because it ensures that event listeners and child components inside the
        conditional block are properly destroyed and re-created during toggles. v-if is also lazy: if the condition is
        false on initial render, it will not do anything - the conditional block won't be rendered until the condition
        becomes true for the first time. In comparison, v-show is much simpler - the element is always rendered
        regardless of initial condition, with CSS-based toggling. Generally speaking, v-if has higher toggle costs while
        v-show has higher initial render costs. So prefer v-show if you need to toggle something very often, and prefer
        v-if if the condition is unlikely to change at runtime.
      </span>
    </span>
  </fieldset>
</template>

<script>
import { defineComponent } from 'vue'
export default defineComponent({
  name: 'DemoA52VIfAdv',
  data() {
    return {
      ok: true
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
