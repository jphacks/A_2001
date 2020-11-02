<template>
  <div class="d-flex align-items-center">
    <i class="fa fa-circle-o fa-lg"></i>
    <input
      v-model="task.name"
      class="focusable"
      :class="isSubtask ? 'subtask-name' : 'task-name'"
      placeholder="タスクを入力"
      @blur="updateTask(task)"
      @keydown.enter="addNewTask"
      @keydown.prevent.down="moveNext"
      @keydown.prevent.up="movePrev"
      @keydown.delete="deleteTask"
    />
    <b-badge v-if="!isSubtask" variant="primary" pill class="ml-auto">{{
      task.subtasks.length
    }}</b-badge>
  </div>
</template>

<script>
export default {
  props: ['task', 'isSubtask'],
  methods: {
    updateTask() {
      this.$emit('updateTask', this.task);
    },
    addNewTask(e) {
      if (e.keyCode !== 13) return; // 日本語入力確定を除外

      if (this.isSubtask) {
        this.$emit('addNewSubtask', this.task.id);
      } else if (e.shiftKey) {
        this.$emit('addNewSubtask', this.task.id);
      } else {
        this.$emit('addNewTask', this.task.id);
      }
    },
    moveNext(event) {
      const elements = document.getElementsByClassName('focusable');
      const index = [].findIndex.call(elements, (e) => e === event.target);
      if (index + 1 < elements.length) elements[index + 1].focus();
    },
    movePrev(event) {
      const elements = document.getElementsByClassName('focusable');
      const index = [].findIndex.call(elements, (e) => e === event.target);
      if (index - 1 >= 0) elements[index - 1].focus();
    },
    deleteTask() {
      if (this.task.name.length === 0) {
        // 0文字の状態でDELETEを押すと削除
        this.$emit('deleteTask', this.task.id);
      }
    },
  },
};
</script>

<style scoped>
*:focus {
  outline: none;
}

.task-name,
.subtask-name {
  width: 100%;
  border: none;
  background: none;
  margin-left: 1em;
}

.task-name {
  font-weight: bold;
}
</style>
