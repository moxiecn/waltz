<!--declares a demo component, No. is DemoF3

-->
<template>
  <div id="DemoF3CompRoot">
    <fieldset>
      <legend align="left">DemoF3-root</legend>
      <span>
        <DemoF3CompBusiness></DemoF3CompBusiness>
        <DemoF3CompBusiness1></DemoF3CompBusiness1>
      </span>
    </fieldset>
  </div>
</template>

<script>
import { defineAsyncComponent, defineComponent } from 'vue'

export default defineComponent({
  name: 'DemoF3CompRoot',
  components: {
    DemoF3CompBusiness1: defineAsyncComponent(() => import('./DemoF3CompBusiness.vue')),
    DemoF3CompBusiness: defineAsyncComponent({
      loader: () => import('./DemoF3CompBusiness.vue'),
      delay: 20000,
      timeout: 3000
      // errorComponent: () => import("./ErrorComponent.vue"),
      // loadingComponent: () => import("./LoadingComponent.vue"),
    })
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
