<!--declares a demo component, No. is DemoA6_1.
    this component will demo a usage of "v-For" dictate.
-->
<template>
  <fieldset>
    <legend align="left">A6_1 v-for</legend>
    <span>
      <ol>
        <li v-for="todo in todos" v-bind:key="todo.id">{{ todo.id }}--{{ todo.text }}.</li>
      </ol>
    </span>
  </fieldset>
</template>

<script>
import { defineComponent } from 'vue'
export default defineComponent({
  name: 'DemoA61VFor',
  data() {
    return {
      todos: [
        { id: 'a', text: 'Learn JavaScript' },
        { id: 'b', text: 'Learn Vue' },
        { id: 'c', text: "Build something awesome['ɒ:sәm]a.引起敬畏的, 可怕的" },
        {
          id: 'd',
          text: 'Whatever else humans are supposed to eat also. [supposed to应该]人类也应该吃其它的(whatever else)'
        }
      ]
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
