<!--declares a demo component,
  this is a todo component. here, some slots are defined.
-->
<template>
  <div id="DemoE1CompSub1Todo">
    <span>
      <div class="container">
        <header>
          <slot name="header"></slot>
        </header>
        <main>
          <slot></slot>
          <!-- in here, <slot> isn't named so,its name default is 'default' -->
        </main>
        <footer>
          <slot name="footer"></slot>
        </footer>
      </div>
    </span>
  </div>
</template>

<script>
import { defineComponent } from 'vue'
export default defineComponent({
  name: 'DemoE1CompSub1Todo'
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
