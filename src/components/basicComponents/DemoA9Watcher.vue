<!--declares a demo component, No. is DemoA9-1.
    this theme is about watchers.
    1. a watcher is used to watch a property and respond.
    2.

-->
<template>
  <div id="DemoA9Watcher">
    <fieldset>
      <legend align="left">A9-2: watcher example</legend>
      <p>
        Ask a yes/no question:
        <input v-model="question" />1 <input v-model="question2" />2 <input v-model="question3" />3
        <input v-model="question4" />4
      </p>
      <p>{{ answer }}</p>
    </fieldset>
  </div>
</template>

<script>
import axios from 'axios'
import { defineComponent } from 'vue'
export default defineComponent({
  name: 'DemoA9Watcher',
  watch: {
    // whenever question changes, this function will run
    question(newQuestion) {
      // watchdog is a function style1
      if (newQuestion.indexOf('?') > -1) {
        this.getAnswer(newQuestion)
      }
    },
    question2: 'getAnswer2', // watchdog is a function style2
    question3: function(newQuestio) {
      // watchdog is a function style3
      this.getAnswer3(newQuestio)
    },
    question4: [
      // is defined a array including two callback function in property question4 watcher.
      'getAnswer4',
      function getAnswer41() {
        this.getAnswer4()
      }
    ]
  },
  data() {
    return {
      question: '',
      question2: '',
      question3: '',
      question4: '',
      answer: 'Questions usually contain a question mark. ;-)'
    }
  },
  methods: {
    getAnswer4: function() {
      alert('question 4 is called by question4')
      this.getAnswer()
    },
    getAnswer3: function(newQuestio) {
      alert('question 3 is called by question3')
      this.getAnswer(newQuestio)
    },
    getAnswer2: function() {
      alert('question 2 is called by question2')
      this.getAnswer()
    },
    getAnswer(v) {
      alert(v)
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
