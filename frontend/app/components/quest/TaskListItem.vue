<template>
  <div
    class="d-flex align-items-center"
    @mouseover="focused = true"
    @mouseout="focused = false"
  >
    <i
      class="fa fa-lg"
      :class="task.done ? 'fa-check-circle-o' : 'fa-circle-o'"
      @click="toggleDone"
    />
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
    <i
      v-show="!isSubtask && (doing || focused)"
      class="fa mr-2 icon"
      :class="doing ? 'fa-hourglass-start' : 'fa-hourglass-end'"
      @click="toggleDoing"
    ></i>
    <b-badge v-if="!isSubtask" variant="primary" pill>{{
      task.subtasks.length
    }}</b-badge>
  </div>
</template>

<script>
export default {
  props: ['task', 'isSubtask'],
  data() {
    return {
      doing: false,
      focused: false,
      deleted: false,
    };
  },
  methods: {
    updateTask() {
      // 削除されたときにも@blurが発生するのでそのときは取り除く
      if (!this.deleted) this.$emit('updateTask', this.task);
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
      // 長押ししたときに1度だけifの中に入る
      if (this.task.name.length === 0 && !this.deleted) {
        // 0文字の状態でDELETEを押すと削除
        this.$emit('deleteTask', this.task.id);
        this.deleted = true;
      }
    },
    toggleDone() {
      this.task.done = !this.task.done;
    },
    toggleDoing() {
      // TODO: doing情報をthis.taskに持たせるべきか考える
      this.doing = !this.doing;
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
