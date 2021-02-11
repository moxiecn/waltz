<!--declares a demo component, No. is DemoA4.
    this component will demo a usage of "v-on" dictate.
-->
<template>
  <fieldset>
    <legend align="left">A4-2 v-on deluxe</legend>
    <span>
      <!-- `greet` 在下面定义的方法名 -->
      <button @click="greet">Greet:Method event handlers</button>
      <!-- 1:in inline, 2:$event is the original DOM event, 3:multiple event handlers, in order-->
      <button @click="say1('what', $event), say2('how', $event)">Greet:Method in INLINE Handlers</button>
    </span>
  </fieldset>
  <fieldset>
    <legend align="left">A4-3 v-on Modifiers</legend>
    <span>
      <input
        v-on:click.stop="doClickStop($event)"
        @click.prevent="doClickPrevent($event)"
        @click.capture="doClickCapture($event)"
        @click.self="doClickSelf($event)"
        @click.once="doClickOnce($event)"
        @click.passive="doClickPassive($event)"
        @keyup.enter="doKeyEnter($event)"
        @keyup.tab="doKeyTab($event)"
        @keyup.delete="doKeyDelete($event)"
        @keyup.esc="doKeyEsc($event)"
        @keyup.space="doKeySpace($event)"
        @keyup.up="doKeyUp"
        @keyup.down="doKeyDown($event)"
        @keyup.left="doKeyLeft($event)"
        @keyup.right="doKeyRight($event)"
        @keyup.ctrl.alt.c="doKeyCtrlAltC($event)"
      />
    </span>
  </fieldset>
</template>

<script>
import { defineComponent } from 'vue'
export default defineComponent({
  name: 'DemoA4VOnAdv',
  data() {
    return {
      name: 'Vue.js'
    }
  },
  methods: {
    doClickStop: function(event) {
      alert('Event modifier: click.stop. ' + event.target)
    },
    doClickPrevent: function(event) {
      alert('Event modifier: click.prevent. ' + event.target)
    },
    doClickCapture: function(event) {
      alert('Event modifier: click.capture. ' + event.target)
    },
    doClickSelf: function(event) {
      alert('Event modifier: click.self. ' + event.target)
    },
    doClickOnce: function(event) {
      alert('Event modifier: click.once. ' + event.target)
    },
    doClickPassive: function(event) {
      alert('Event modifier: click.passive. ' + event.target)
    },
    doKeyEnter: function(event) {
      alert('Event modifier: keyup.enter. ' + event.target)
    },
    doKeyTab: function(event) {
      alert('Event modifier: keyup.tab. ' + event.target)
    },
    doKeyDelete: function(event) {
      alert('Event modifier: keyup.delete. ' + event.target)
    },
    doKeyEsc: function(event) {
      alert('Event modifier: keyup.esc. ' + event.target)
    },
    doKeySpace: function(event) {
      alert('Event modifier: keyup.space. ' + event.target)
    },
    doKeyUp() {
      alert('Event modifier: keyup.up. ')
    },
    doKeyDown: function(event) {
      alert('Event modifier: keyup.down. ' + event.target)
    },
    doKeyLeft: function(event) {
      alert('Event modifier: keyup.left. ' + event.target)
    },
    doKeyRight: function(event) {
      alert('Event modifier: keyup.right. ' + event.target)
    },
    doKeyCtrlAltC: function(event) {
      alert('Event modifier: keyup.ctrl.alt.c. ' + event.target)
    },
    greet(event) {
      // `event` 是原生 DOM event
      if (event) {
        alert('Hello ' + this.name + '! by ' + event.target.tagName)
      } else {
        // `this` 内部 `methods` 指向当前活动实例
        alert('Hello ' + this.name + '!')
      }
    },
    say1(message, e) {
      if (e) {
        e.preventDefault()
      }
      alert('you said ' + message + ' on 1 by ' + e)
    },
    say2(message, e) {
      alert('you said ' + message + ' on 2 by ' + e)
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
