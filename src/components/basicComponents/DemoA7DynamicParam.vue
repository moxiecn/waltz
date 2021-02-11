<!--declares a demo component, No. is DemoA7.
    this component will add 1 at a specified time interval.
-->
<template>
  <fieldset>
    <legend align="left">A7 Dynamic Parameters</legend>
    <fieldset class="subfieldset">
      <legend align="center">on v-bind</legend>
      <input v-bind:[htmlattrname]="onattrvalue" />
      <button v-on:click="doitAttr('value')">click for value</button>
      <button v-on:click="doitAttr('font-color')">click for title</button>
      {{ htmlattrname }}
    </fieldset>
    <fieldset class="subfieldset">
      <legend>on v-on</legend>
      <button v-on:[htmleventname]="doit">test {{ htmleventname }}</button>
      <button v-on:click="doitSwitch('click')">switch to click</button>
      <button v-on:click="doitSwitch('mouseout')">switch to mouseup</button>
      <button
        v-on:[htmleventname]="
          {
            doitc
          }
        "
      >
        test {{ htmleventname }}
      </button>
      <!-- <button v-on:[htmleventname]="{{doitc()}">test {{htmleventname}}</button> -->
    </fieldset>
  </fieldset>
</template>

<script>
import { defineComponent } from 'vue'
export default defineComponent({
  name: 'DemoA7DynamicParams',
  data: function() {
    return {
      onattrvalue: 'current',
      htmlattrname: '',
      htmleventname: '',
      doitc: 'doit'
    }
  },
  // computed: {
  //   doitc(){
  //     if (this.htmleventname=='click'){
  //       return 'doitClick('+'click is clicked.)';
  //     }
  //     return "";
  //   }
  // },
  methods: {
    doitSwitch: function(Switch) {
      this.htmleventname = Switch
      // alert(this.htmleventname + " event is activated." + "--" + Switch);
    },
    doit: function() {
      if (this.htmleventname == 'click') {
        //eslint-disable-line
        this.doitClick('click is set.')
      }
      if (this.htmleventname == 'mouseout') {
        this.doitMouseout('mouse up is set.')
      }
    },
    doitClick: function(v) {
      alert(this.htmleventname + ' event is activated.' + '--' + v)
    },
    doitMouseout: function(v) {
      alert(this.htmleventname + ' event is activated.' + '--' + v)
    },
    doitAttr(v) {
      if (v == 'value') {
        this.htmlattrname = 'value'
        this.onattrvalue = 'current attr is ' + this.htmlattrname
      }
      if (v == 'font-color') {
        this.htmlattrname = 'font-color'
        this.onattrvalue = 'red'
      }
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
.subfieldset {
}
</style>
