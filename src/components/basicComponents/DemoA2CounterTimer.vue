<!--declares a demo component, No. is DemoA2.
    this component will add 1 at a specified time interval.
-->
<template>
  <div id="DemoA2CounterTime">
    <fieldset>
      <legend align="left">A2 templates syntax</legend>
      <fieldset class="subfieldset">
        <legend align="center">{{}},props,data(),mounted()</legend>
        <span>Time Counter: {{ counter }}, add 1 times every {{ interval }}{{ intervalUnit }}.</span>
        <p />
        <span v-once>Time Counter: {{ counter }} v-once, so it'll not changed.</span>
        <p />
      </fieldset>
      <fieldset class="subfieldset">
        <legend>v-html</legend>
        <span v-html="rawHtml"></span>
        <p />
        <span>{{ rawHtml }}</span>
        <p />
      </fieldset>
      <fieldset class="subfieldset">
        <legend>javascript expression</legend>
        <span>{{ vok ? 'YES' : 'NO' }} </span>
        <p />
        <span v-bind:id="counter - 1">this id is {{ counter - 1 }}</span>
        <p />
      </fieldset>
    </fieldset>
  </div>
</template>

<script>
import { defineComponent } from 'vue'
export default defineComponent({
  name: 'DemoA2CounterTime',
  props: {
    interval: {
      type: [Number],
      required: false,
      default: function() {
        console.log('DemoA2 component "interval" atrribute default value is set to 500.')
        return 500
      },
      validator: function(value) {
        console.log('DemoA2 component "interval" atrribute default value is ' + value + '. ')
        return value >= 200
      }
    },
    intervalUnit: String,
    rawHtml: {
      default:
        '<div id="example1" class="demo">' +
        'Using mustaches: {{ rawHtml }}' +
        'Using v-html directive: <span v-html="rawHtml"></span>' +
        '</div>'
    },
    vok: { default: true }
  },
  data() {
    return {
      counter: 0
      // interval: Number,
      // intervalUnit: String
    }
  },
  mounted() {
    setInterval(() => {
      this.counter++
    }, this.interval)
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
.subfieldset {
}
</style>
