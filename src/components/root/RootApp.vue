<template>
  <img alt="Vue logo" src="../../assets/logo.png" />
  <fieldset>
    <legend align="left">DemoA Essentials</legend>
    <DemoA1Counter counter="abc"></DemoA1Counter>
    <DemoA2CounterTime :counter="0" :interval="2000" intervalUnit="ms"></DemoA2CounterTime>
    <DemoA3BindAttribute></DemoA3BindAttribute>
    <DemoA31VModel></DemoA31VModel>
    <DemoA4VOn></DemoA4VOn>
    <DemoA4VOnAdv></DemoA4VOnAdv>
    <DemoA51VIf></DemoA51VIf>
    <DemoA52VIfAdv></DemoA52VIfAdv>
    <DemoA61VFor></DemoA61VFor>
    <DemoA62VForAdv></DemoA62VForAdv>
    <DemoA7DynamicParams></DemoA7DynamicParams>
    <DemoA8Loadsh></DemoA8Loadsh>
    <DemoA8Loadsh></DemoA8Loadsh>
    <DemoA9ComputedProperties></DemoA9ComputedProperties>
    <DemoA9Watcher></DemoA9Watcher>
  </fieldset>
  <DemoB1ClassStyle></DemoB1ClassStyle>
  <fieldset>
    <legend align="left">DemoC Form elements</legend>
    <DemoC1FormElements></DemoC1FormElements>
  </fieldset>
  <DemoD1Comp></DemoD1Comp>
  <DemoE1Comp></DemoE1Comp>
  <DemoF1Comp></DemoF1Comp>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import DemoA1Counter from '../basicComponents/DemoA1Counter.vue'
import DemoA2CounterTime from '../basicComponents/DemoA2CounterTimer.vue'
import DemoA31VModel from '../basicComponents/DemoA3-1VModel.vue'
import DemoA3BindAttribute from '../basicComponents/DemoA3VBind.vue'
import DemoA4VOn from '../basicComponents/DemoA4VOn.vue'
import DemoA4VOnAdv from '../basicComponents/DemoA4VOnAdv.vue'
import DemoA51VIf from '../basicComponents/DemoA5_1VIf.vue'
import DemoA52VIfAdv from '../basicComponents/DemoA5_2VIfAdv.vue'
import DemoA61VFor from '../basicComponents/DemoA6_1VFor.vue'
import DemoA62VForAdv from '../basicComponents/DemoA6_2VForAdv.vue'
import DemoA7DynamicParams from '../basicComponents/DemoA7DynamicParam.vue'
import DemoA8Loadsh from '../basicComponents/DemoA8_Loadsh.vue'
import DemoA9ComputedProperties from '../basicComponents/DemoA9ComputedProperties.vue'
import DemoA9Watcher from '../basicComponents/DemoA9Watcher.vue'
import DemoB1ClassStyle from '../basicComponents/DemoB1ClassStyle.vue'
import DemoC1FormElements from '../basicComponents/DemoC1FormElements.vue'
import DemoD1Comp from '../basicComponents/DemoD1Comp.vue'
import DemoE1Comp from '../basicComponents/DemoE1Comp.vue'
import DemoF1Comp from '../basicComponents/DemoF1Comp.vue'

export default defineComponent({
  name: 'RootApp',
  components: {
    DemoA1Counter,
    DemoA2CounterTime,
    DemoA31VModel,
    DemoA3BindAttribute,
    DemoA4VOn,
    DemoA4VOnAdv,
    DemoA51VIf,
    DemoA52VIfAdv,
    DemoA61VFor,
    DemoA62VForAdv,
    DemoA7DynamicParams,
    DemoA8Loadsh,
    DemoA9ComputedProperties,
    DemoA9Watcher,
    DemoB1ClassStyle,
    DemoC1FormElements,
    DemoD1Comp,
    DemoE1Comp,
    DemoF1Comp
  }
})

/*
  in package.json
  // "prettier": {
  //   "stylelintIntegration": true,
  //   "eslintIntegration": true,
  //   "singleQuote": true,
  //   "semi": false,
  //   "insertPragma": false,
  //   "trailingComma": "none",
  //   "arrowParens": "avoid"
  // },
*/
</script>

<style>
#rootApp {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
