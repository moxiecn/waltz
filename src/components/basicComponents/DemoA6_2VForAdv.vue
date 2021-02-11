<!--declares a demo component, No. is DemoA6_2.
    this component will demo a usage of "v-For" dictate.
-->
<template>
  <fieldset>
    <legend align="left">A6_2 v-for advance</legend>
    <ul id="array-rendering">
      <li v-for="(item, index) in items" :key="index">{{ item.message }}</li>
    </ul>
    <ul id="array-with-index">
      <li v-for="(item, index) of items" :key="index">{{ parentMessage }} - {{ index }} - {{ item.message }}</li>
    </ul>
  </fieldset>
  <fieldset>
    <legend align="left">A6_3 use object inside v-for</legend>
    <ul id="v-for-object" class="demo">
      <li v-for="(value, name, index) in myObject" :key="index">{{ index }}. {{ name }}: {{ value }}</li>
    </ul>
  </fieldset>
  <fieldset>
    <legend align="left">A6_4 about sort and filter of v-for</legend>
    <h5>based on computed property:</h5>
    <li v-for="(n, index) in evenNumbers" :key="index">{{ n }}</li>
    ,
    <span v-for="(n, index) in oddNumbers" :key="index">{{ n }}</span>
    <h5>based on method:</h5>
    <template v-for="(numbers, index) in sets" :key="index">
      <button v-for="(n, index) in even(numbers)" :key="index">{{ n }}</button>,
    </template>
    <template v-for="(numbers, index) in sets" :key="index">
      <!-- <li v-for="(n,index) in odd(numbers)" :key="index">{{ n }}</li> -->
      <input v-for="(n, index) in odd(numbers)" :key="index" :value="n" style="width:15px;" />,
    </template>
    <h5>v-for nested v-if, use &#60;template&#62;:</h5>
    <template v-for="(todo, index) in numbers" :key="index">
      <li v-if="isEven(todo)">{{ todo }}</li>
    </template>
    <template v-for="(todo, index) in numbers" :key="index">
      <li v-if="todo % 2 !== 0">{{ todo }}</li>
    </template>
  </fieldset>
  <fieldset>
    <legend align="left">A6_5 custom component &#60;DemoA6_3VForTodo&#62;</legend>
    <form v-on:submit.prevent="addNewTodo">
      <label for="new-todo">Add a todo</label>
      <input v-model="newTodoText" id="new-todo" placeholder="E.g. Feed the cat" />
      <button>Add</button>
    </form>
    <ul>
      <DemoA63VForTodo
        v-for="(todo, index) in todos"
        :key="todo.id"
        :title="todo.title"
        v-bind:titleId="todo.id"
        @remove="todos.splice(index, 1)"
      ></DemoA63VForTodo>
    </ul>
  </fieldset>
</template>

<script>
import DemoA63VForTodo from './DemoA6_3VForTodo'

import { defineComponent } from 'vue'
export default defineComponent({
  name: 'DemoA62VForAdv',
  data() {
    return {
      parentMessage: 'Parent',
      items: [{ message: 'Foo' }, { message: 'Bar' }],
      myObject: {
        title: 'How to do lists in Vue',
        author: 'Jane Doe',
        publishedAt: '2016-04-10'
      },
      sets: [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10]
      ],
      numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9],
      // for todo demo
      newTodoText: '',
      todos: [
        {
          id: 1,
          title: 'Do the dishes'
        },
        {
          id: 2,
          title: 'Take out the trash'
        },
        {
          id: 3,
          title: 'Mow the lawn'
        }
      ],
      nextTodoId: 4
    }
  },
  computed: {
    evenNumbers() {
      return this.numbers.filter(number => number % 2 === 0)
    },
    oddNumbers() {
      return this.numbers.filter(number => number % 2 !== 0)
    }
  },
  methods: {
    isEven(number) {
      return number % 2 === 0
    },
    even(numbers) {
      return numbers.filter(number => number % 2 === 0)
    },
    odd(numbers) {
      return numbers.filter(number => number % 2 !== 0)
    },
    // for todo demo
    addNewTodo() {
      this.todos.push({
        id: this.nextTodoId++,
        title: this.newTodoText
      })
      this.newTodoText = ''
    }
  },
  components: {
    DemoA63VForTodo
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
