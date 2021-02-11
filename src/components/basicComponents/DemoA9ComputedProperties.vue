<!--declares a demo component, No. is DemoA9.
    this theme is about computed properties and watchers.
    1. Both computed property and method can achieve the same function. but the difference is that computed property is based on cache mechanism.<template>
        when data has not changed and refreshing the template, there is no need to recaclulate on computed property, howerver, the method is called ever time the page is rendered.
        When dataset is large and the caculation logic is complex, method mode will be catastrophic([,kætә'strɒfik]a. 悲惨的, 灾难的).
    2.

-->
<template>
  <fieldset>
    <legend align="left">A9-1: a simple demo about computed properties</legend>
    <p>Has published books:</p>
    <!--specifies a computed property name, it is defined "computed" attribute in vm isntance. its defination refer to computed field.-->
    <span>computed property:{{ publishedBooksMessage0 }}</span>
    &nbsp;&nbsp;&nbsp;
    <span>method:{{ publishedBooksMessage1() }}</span>
    &nbsp;&nbsp;&nbsp;
    <span>computed property setter:{{ publishedBooksMessage2 }}</span>
    &nbsp;&nbsp;&nbsp;
    <button v-on:click="toswitch">switch status</button>&nbsp;&nbsp;
    <button v-on:click="tosetter">setter</button>
    <p />
    <span>{{ author.books }}</span>
  </fieldset>
</template>

<script>
import { defineComponent } from 'vue'
export default defineComponent({
  name: 'DemoA9ComputedProperties',
  data() {
    return {
      author: {
        name: 'John Doe',
        books: ['Vue 2 - Advanced Guide', 'Vue 3 - Basic Guide', 'Vue 4 - The Mystery']
      }
    }
  },
  computed: {
    // 计算属性的 getter
    publishedBooksMessage0: function() {
      // `this` points to the vm instance
      return this.author.books.length > 0 ? 'Yes' : 'No'
    },
    publishedBooksMessage2: {
      get() {
        return this.author.books.length > 0 ? 'Yes setter' : 'No setter'
      },
      set(val) {
        this.author.books = val
      }
    }
  },
  methods: {
    publishedBooksMessage1: function() {
      return this.author.books.length > 0 ? 'Yes' : 'No'
    },
    tosetter: function() {
      this.publishedBooksMessage2 = ['Vue 12 ', 'Vue 23 ', 'Vue 34 ']
    },
    toswitch: function() {
      this.author.books =
        this.author.books.length > 0 ? [] : ['Vue 2 - Advanced Guide', 'Vue 3 - Basic Guide', 'Vue 4 - The Mystery']
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
