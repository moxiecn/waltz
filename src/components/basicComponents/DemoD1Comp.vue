<!--declares a demo component, No. is DemoD1

-->
<template>
  <fieldset>
    <legend align="left">DemoD1: Components</legend>
    <fieldset>
      <legend align="left">D1-1: Passing Data to Child Components with Props</legend>
      <span>
        this is some of the child components:
        <DemoD1CompSub title="this title comes from parent its compoment. this is 1." />
        <DemoD1CompSub title="this title comes from parent its compoment. this is 2." />
        <DemoD1CompSub title="this title comes from parent its compoment. this is 3." />
      </span>
      <br />
      <span>
        this is some of the child components by v-for:
        <DemoD1CompSub1 v-for="(title, index) in titles" :key="index" v-bind:title="title.title" v-bind:id="title.id" />
      </span>
      <br />
    </fieldset>
    <fieldset>
      <legend align="left">DemoD1-2: usage of the $emit()</legend>
      <span>
        <div>
          child components by v-for({{ titleFontSize }}):
          <DemoD1CompSub2
            v-for="(t, index) in titles"
            :key="index"
            v-bind:title="t.title"
            v-bind:index1="t.index"
            :titleFontSize="t.fsize"
            v-on:eventEnlarge="doEnlarge1"
            @eventReduce="doReduce1"
          />
        </div>
      </span>
      <br />
      <fieldset>
        <legend align="left">D1-2_1: advanced usage of $emit()</legend>
        <span>
          <div>
            child components by v-for({{ titleFontSize }}):
            <DemoD1CompSub2_1
              v-for="(t, index) in titles"
              :key="index"
              v-bind:title="t.title"
              v-bind:index1="t.index"
              :titleFontSize="t.fsize"
              v-on:eventEnlarge="doEnlarge1"
              @eventReduce="doReduce1"
            />
          </div>
        </span>
        <br />
      </fieldset>
    </fieldset>

    <fieldset>
      <legend align="left">DemoD1-3: v-model feature on a custom component)</legend>
      <span>
        <DemoD1CompSub3 v-model="searchText1" sn="1" />
        <br />
        <DemoD1CompSub3 v-model="searchText2" sn="2" />
      </span>
      <br />
      <fieldset>
        <legend align="left">D1-31 advanced: modify attribute name</legend>
        <span>
          <DemoD1CompSub31 v-model:vtitle="searchText3" sn="3" />
          <br />
          <DemoD1CompSub31 v-model:vtitle="searchText4" sn="4" />
        </span>
        <br />
      </fieldset>
      <fieldset>
        <legend align="left">D1-32 advanced: multiple v-model binding on one component</legend>
        <span>
          <DemoD1CompSub32 v-model:vserach5="searchText5" v-model:vserach6="searchText6" sn="56" />
        </span>
        <br />
      </fieldset>
      <fieldset>
        <legend align="left">D1-33 advanced: v-model custom modifiers</legend>
        <span>
          <DemoD1CompSub33 v-model.capitalize1="searchText7" v-model:foo.lowercasefoo="searchText8"></DemoD1CompSub33>
          P:{{ searchText7 }},{{ searchText8 }}
        </span>
        <br />
      </fieldset>
    </fieldset>

    <fieldset>
      <legend align="left">DemoD1-4: slot feature on a component)</legend>
      <span>
        this is a empty slot.
        <DemoD1CompSub4 />
      </span>
      <br />
    </fieldset>

    <fieldset>
      <legend align="left">DemoD1-5: dynamic components</legend>
      <span>
        <!-- 组件会在 `currentTabComponent` 改变时改变 -->
        <!-- keep-alive标签：失活的组件将会被缓存！
          https://vue3js.cn/docs/zh/guide/component-dynamic-async.html#在动态组件上使用-keep-alive
          -->
        <keep-alive>
          <component v-bind:is="currentTabComponent"></component>
        </keep-alive>
        <button @click="currentComponent3">DemoD1CompSub3</button>
        <button @click="currentComponent2">DemoD1CompSub2</button>
      </span>
      <br />
    </fieldset>

    <fieldset>
      <legend align="left">DemoD1-6: some rules or conventions about components</legend>
      <span align="left">
        about the component itself:
        <ul>
          <li>
            component name must be followed W3C rules, all lowercase and contains hyphen symbol if has multiple words.
          </li>
          <li>registed in global, these can be used directly in any templetes.</li>
          <li>recommend local registration to avoid useless components.</li>
          <li>
            "import" and "export" is recommended to build the compoments system. Each component should be placed in
            "components" directory to facilitate the management of components.
          </li>
        </ul>
        <br />about props:
        <ul>
          <li>
            The definitions of "props" can be ['field1','field2'], this is simplest style, can also contain the
            defintions of type,validation. for more,
            <a href="https://vue3js.cn/docs/zh/guide/component-props.html#prop-类型">for more, refer to here</a>
          </li>
          <li>
            props can be passed a static or dynamic value, a string, a number, a boolean, a array, any entire object or
            a part of that object.
          </li>
          <li>
            All props is on-way binding beween parent component and child one, and can only pass data from parent to
            child, otherwise it can't.
          </li>
          <li>
            props are verfied before a component instance is created. so the properties of the instance( such as
            data,compouted,etc) are not available in the "default" or "validator" functions.
          </li>
        </ul>
        <fieldset>
          <legend align="left">a demo about props</legend>
          <DemoD1CompSub6 init-value="initValue" prop-d="true" />
          <br />
        </fieldset>
      </span>
      <br />
    </fieldset>
    <fieldset>
      <legend align="left">DemoD1-7: about "non-prop" attribute</legend>
      <span align="left">
        <DemoD1CompSub7 data-status="activated" @myevent="submitChange" />
        <br />
        <a href="https://vue3js.cn/docs/zh/guide/component-attrs.html#attribute-继承">attributes inheritance</a>
        <br />
        <a href="https://vue3js.cn/docs/zh/guide/component-attrs.html#禁用-attribute-继承"
          >disabling attributes inheritance</a
        >
        <br />
        <a href="https://vue3js.cn/docs/zh/guide/component-attrs.html#多个根节点上的-attribute-继承"
          >attributes inheritance on multiple root nodes</a
        >
      </span>
      <br />
    </fieldset>
  </fieldset>
</template>

<script>
import DemoD1CompSub from './DemoD1CompSub'
import DemoD1CompSub1 from './DemoD1CompSub1'
import DemoD1CompSub2 from './DemoD1CompSub2'
import DemoD1CompSub21 from './DemoD1CompSub2_1.vue'
import DemoD1CompSub3 from './DemoD1CompSub3'
import DemoD1CompSub31 from './DemoD1CompSub31'
import DemoD1CompSub32 from './DemoD1CompSub32'
import DemoD1CompSub33 from './DemoD1CompSub33'
import DemoD1CompSub4 from './DemoD1CompSub4'
import DemoD1CompSub6 from './DemoD1CompSub6'
import DemoD1CompSub7 from './DemoD1CompSub7'

import { defineComponent } from 'vue'
export default defineComponent({
  name: 'DemoD1Comp',
  components: {
    DemoD1CompSub: DemoD1CompSub,
    DemoD1CompSub1: DemoD1CompSub1,
    DemoD1CompSub2: DemoD1CompSub2,
    DemoD1CompSub21: DemoD1CompSub21,
    DemoD1CompSub3: DemoD1CompSub3,
    DemoD1CompSub31: DemoD1CompSub31,
    DemoD1CompSub32: DemoD1CompSub32,
    DemoD1CompSub33: DemoD1CompSub33,
    DemoD1CompSub4: DemoD1CompSub4,
    DemoD1CompSub6: DemoD1CompSub6,
    DemoD1CompSub7: DemoD1CompSub7
  },
  data() {
    return {
      titles: [
        { index: 1, fsize: 1, title: 'My journey with Vue' },
        { index: 2, fsize: 1, title: 'Blogging with Vue' },
        { index: 3, fsize: 1, title: 'Why Vue is so fun' }
      ],
      titleFontSize: 1,
      searchText1: '',
      searchText2: '',
      searchText3: '',
      searchText4: '',
      searchText5: '',
      searchText6: '',
      searchText7: '',
      searchText8: '',
      currentComponent: ''
    }
  },
  methods: {
    doEnlarge1: function(inx) {
      this.titles.find(function(el) {
        return el.index == inx
      }).fsize += 0.1
    },
    doReduce1: function(inx, in1) {
      console.log(in1)
      this.titles.find(function(el) {
        return el.index == inx
      }).fsize -= 0.1
    },
    currentComponent2: function() {
      this.currentComponent = 'DemoD1CompSub2'
    },
    currentComponent3: function() {
      this.currentComponent = 'DemoD1CompSub3'
    }
  },
  computed: {
    currentTabComponent() {
      return this.currentComponent
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
  list-style-type: square;
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
