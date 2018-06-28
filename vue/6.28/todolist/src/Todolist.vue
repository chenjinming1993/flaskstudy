<template>
  <div>
    <div id="app">
    <input v-model="inputValue" />
    <button @click="handleSubmit">提交</button>
    </div>
    <ul>
      <todo-item
        v-for="(item,index) of list"
        :key="index" :content="item"
        :index="index"
        @delete="handleDelete"></todo-item>
    </ul>
  </div>
</template>

<script>
import Todoitem from './components/Todoitem'

export default {
  components:{
    'todo-item':Todoitem
  },
  data() {
    return{
        inputValue:'',
      list:[]
    }
  },
  methods:{
      handleSubmit(){
          this.list.push(this.inputValue)
          this.inputValue=''
      },
    handleDelete(index){
      this.list.splice(index,1)
    }
  }
}
</script>

<style>

</style>
