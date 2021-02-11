<!--declares a demo component, No. is DemoF3

-->
<template>
  <div id="DemoF3CompBusiness">
    <fieldset>
      <legend align="left">DemoF3-business</legend>
      <span>
        <div>aasdfa;{{ answer }}</div>
      </span>
    </fieldset>
  </div>
</template>

<script>
import axios from 'axios'

import { defineComponent } from 'vue'
export default defineComponent({
  name: 'DemoF3CompBusiness',
  data() {
    return {
      answer: 'are you ok?'
    }
  },
  mounted() {
    this.getAnswer()
  },
  methods: {
    getAnswer() {
      this.answer = 'Thinking...'
      axios
        .get('https://yesno.wtf/api')
        .then(response => {
          this.answer = response.data.answer
        })
        .catch(error => {
          this.answer = 'Error! Could not reach the API. ' + error
        })
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
