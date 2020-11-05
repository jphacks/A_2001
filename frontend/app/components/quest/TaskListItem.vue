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
      :ref="`task${task.id}`"
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
      v-show="!isSubtask && (this.task.start !== null || focused)"
      class="fa mr-2 icon"
      :class="
        this.task.start !== null ? 'fa-hourglass-start' : 'fa-hourglass-end'
      "
      @click="toggleDoing"
    ></i>
    <!-- <b-badge v-if="!isSubtask" variant="primary" pill>{{
      task.subtasks.length
    }}</b-badge> -->
    <i
      v-if="!isSubtask"
      class="fa fa-plus-square-o ml-2 fa-lg icon"
      @click="addNewTask"
    />
    <i class="fa fa-minus-square-o ml-2 fa-lg icon" @click="deleteTask" />
  </div>
</template>

<script>
export default {
  props: {
    task: {
      type: Object,
      required: true,
    },
    isSubtask: {
      type: Boolean,
      required: true,
    },
  },
  data() {
    return {
      focused: false,
      // timerId: null,
      // totalTime: 0,
      deleted: false,
    };
  },
  mounted() {
    this.$nextTick(() => {
      this.$refs[`task${this.task.id}`].focus();
    });
  },
  //   if (this.task.start !== null) {
  //     this.totalTime = Math.round(
  //       (new Date().getTime() - new Date(this.task.start + '+0900').getTime()) /
  //         1000
  //     );
  //     this.timerId = setInterval(() => this.updateTime(), 1000);
  //   }
  // beforeDestroy() {
  //   clearInterval(this.timerId);
  // },
  methods: {
    // updateTime() {
    //   this.totalTime++;
    // },
    updateTask() {
      // 削除されたときにも@blurが発生するのでそのときは取り除く
      if (!this.deleted) this.$emit('updateTask', this.task);
    },
    addNewTask(e) {
      // ボタンで追加するとき
      if (e.target.tagName === 'I') {
        this.$emit('addNewSubtask', this.task.id);
        return;
      }

      // キーボードで追加するとき
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
    deleteTask(e) {
      // ボタンで削除するとき
      if (e.target.tagName === 'I') {
        this.$emit('deleteTask', this.task.id);
        return;
      }

      // 長押ししたときに1度だけifの中に入る
      if (this.task.name.length === 0 && !this.deleted) {
        // 0文字の状態でDELETEを押すと削除
        this.$emit('deleteTask', this.task.id);
        this.deleted = true;
      }
    },

    toggleDone() {
      const questId = parseInt(this.$route.params.quest);
      if (this.task.done === true) {
        this.$api
          .$delete(`/api/quests/${questId}/tasks/${this.task.id}/done`)
          .then(() => {
            if (!this.isSubtask)
              this.$store.commit('quest/decrementUndoneCnt', questId);
            this.task.done = false;
          })
          .catch(() => alert('done error'));
      } else {
        this.$api
          .$put(`/api/quests/${questId}/tasks/${this.task.id}/done`)
          .then(() => {
            if (!this.isSubtask)
              this.$store.commit('quest/incrementUndoneCnt', questId);
            this.task.done = true;
          })
          .catch(() => alert('done error'));
      }
    },
    toggleDoing() {
      // TODO: this.task.start情報をthis.taskに持たせるべきか考える
      this.$api
        .$put(
          `/api/quests/${this.$route.params.quest}/tasks/${this.task.id}/time`
        )
        .then(() => {
          // this.this.task.start = !this.this.task.start;
          if (this.task.start === null) {
            this.task.start = new Date().toUTCString();
          } else {
            this.task.start = null;
          }
          this.updateTask();
          // タイマー機能は一旦保留
          // if (this.timerId === null) {
          //   // 開始時の処理
          //   this.timerId = setInterval(() => this.updateTime(), 1000);
          // } else {
          //   // 終了時の処理
          //   clearInterval(this.timerId);
          //   this.timerId = null;
          // }
        })
        .catch((err) => {
          console.error(err);
        });
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
