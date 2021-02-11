<!--declares a demo component, No. is DemoC1-1.

-->
<template>
  <fieldset>
    <legend align="left">C1-1: bidirectional data binding V-MODE basic form elements</legend>
    <span>
      text:
      <input v-model="message" placeholder="edit me" />
      Message is: {{ message }}
    </span>
    <br />
    <span>
      textarea:
      <textarea v-model="message" placeholder="add multiple lines"></textarea>
      <p style="white-space: pre-line;">{{ message }}</p>
    </span>
    <br />
    <span>
      Checkbox:
      <input type="checkbox" id="jack" value="Jack" v-model="checkedNames" />
      <label for="jack">Jack</label>
      <input type="checkbox" id="john" value="John" v-model="checkedNames" />
      <label for="john">John</label>
      <input type="checkbox" id="mike" value="Mike" v-model="checkedNames" />
      <label for="mike">Mike</label>,
      <span>Checked names: {{ checkedNames }}</span>
    </span>
    <br />
    <span>
      Radio:
      <input type="radio" id="one" value="One" v-model="picked" />
      <label for="one">One</label>
      <input type="radio" id="two" value="Two" v-model="picked" />
      <label for="two">Two</label>,
      <span>Picked: {{ picked }}</span>
    </span>
    <br />
    <span>
      select(single):
      <select v-model="selected">
        <option disabled value>Please select one</option>
        <option>A</option>
        <option>B</option>
        <option>C</option> </select
      >,
      <span>Selected: {{ selected }}</span>
    </span>
    <br />
    <span>
      select(multiple):
      <select v-model="selected" multiple>
        <option>A</option>
        <option>B</option>
        <option>C</option> </select
      >,
      <span>Selected: {{ selected }}</span>
    </span>
    <br />
    <span>
      select(v-for):
      <select v-model="selected">
        <option v-for="(option, index) in options" :value="option.value" :key="index">{{ option.text }}</option>
      </select>
      <span>Selected: {{ selected }}</span>
    </span>
  </fieldset>
  <fieldset>
    <legend align="left">C1-2: bidirectional data binding V-MODE value binding</legend>
    <span>
      single select:
      <!-- 当选中时，`picked` 为字符串 "a" -->
      <input type="radio" v-model="picked" value="a" />
      <!-- 当选中时，picked 为 data.a变量的值"dd"-->
      <input type="radio" v-model="picked" v-bind:value="a" />
      {{ picked }}
      <!-- `toggle` 为 true 或 false -->
      <input type="checkbox" v-model="toggle" />
      {{ toggle }}
      <!-- 当选中第一个选项时，`selected` 为字符串 "abc" -->
      <select v-model="selected">
        <option value="abc">ABC</option>
        <option value="def">DEF</option>
      </select>
      {{ selected }}
    </span>
    <br />
    <span>
      MULTIPLE select:
      <input type="checkbox" v-model="toggle" true-value="yesno" false-value="noyes" />
      {{ toggle }}
    </span>
    <br />
    <span>
      Select option INLINE object:
      <select v-model="selected">
        <!-- 内联对象字面量 -->
        <!-- 当被选中时
            typeof vm.selected＝'object'
          vm.selected.number＝123-->
        <option :value="{ number: 123 }">123</option>
        <option :value="{ number: 456 }">456</option>
      </select>
      {{ selected }}
    </span>
  </fieldset>
  <fieldset>
    <legend align="left">C1-3: form elelemts modifiers</legend>
    <span>
      .lazy:
      <!-- synced after "change" instead of "input" -->
      <input v-model.lazy="msg" />
      <br />.lazy: no lazy
      <!-- synced after "input" immediately -->
      <input v-model="msg" />
      {{ msg }}
      <br />.number:
      <input
        v-model.number="msg"
        title="If you want user input to be automatically typecast as a number, you can add the number modifier to your v-model managed inputs:"
      />
      <br />.number: no number
      <input v-model="msg" />
      {{ msg }},{{ typeof msg }} <br />.trim:
      <input v-model.trim="msg" />
      {{ msg }}
    </span>
    <br />
  </fieldset>
</template>

<script>
import { defineComponent } from 'vue'
export default defineComponent({
  name: 'DemoC1FormElements',
  data() {
    return {
      msg: 'test text',
      a: 'dd',
      message: '',
      checkedNames: [],
      picked: '',
      selected: '',
      toggle: Boolean,
      options: [
        { text: 'One', value: 'A' },
        { text: 'Two', value: 'B' },
        { text: 'Three', value: 'C' }
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
