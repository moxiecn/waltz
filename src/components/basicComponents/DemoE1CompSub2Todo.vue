<!--declares a demo component,
  this is a child component.
  is about scoped slots.
-->
<template>
  <div id="DemoE1CompSub2Todo">
    <span>
      <ul>
        <li v-for="(item, index) in items" :key="index">
          <slot name="scoped-slots1" :item1="item"></slot>
        </li>
      </ul>
    </span>
  </div>
</template>

<script>
import { defineComponent } from 'vue'
export default defineComponent({
  name: 'DemoE1CompSub2Todo',
  data() {
    return {
      items: ['Feed a cat', 'Buy milk']
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
