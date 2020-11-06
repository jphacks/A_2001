<template>
  <div
    class="d-flex align-items-center"
    @mouseover="focused = true"
    @mouseout="focused = false"
  >
    <template v-if="!task.done">
      <template v-if="!isSubtask">
        <i
          v-if="focused"
          class="fa fa-lg fa-thumb-tack icon-button"
          @click="toggleDoing"
        />
        <i
          v-else
          class="fa fa-lg fa-thumb-tack icon-button"
          :style="{ color: '#cccccc' }"
          @click="toggleDoing"
        />
      </template>

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
        v-if="!isSubtask"
        class="fa fa-plus-square-o ml-2 fa-lg icon text-muted icon-button"
        @click="addNewTask"
      />
      <i
        class="fa fa-minus-square-o ml-2 fa-lg icon text-muted icon-button"
        v-b-modal="!isSubtask ? `modal-task-delete${task.id}` : ''"
        @click="deleteTask(isSubtask)"
      />
      <b-modal :id="`modal-task-delete${task.id}`" @ok="deleteTask(true)">
        <p>タスクを削除しますか？</p>
      </b-modal>
    </template>
    <template v-else>
      <i class="fa fa-lg fa-check-circle-o text-success icon-button" />
      <p class="mb-0 ml-1" :class="{ 'task-name': !isSubtask }">
        {{ task.name }}
      </p>
    </template>
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
    parentTaskId: {
      type: Number,
      default: null,
    },
    isDoing: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      focused: false,
      deleted: false,
      selected: 'stop',
      options: [
        { text: 'stop', value: 'stop' },
        { text: 'start', value: 'start' },
      ],
    };
  },
  mounted() {
    this.$nextTick(() => {
      if (`task${this.task.id}` in this.$refs) {
        this.$refs[`task${this.task.id}`].focus();
      }
    });
  },
  methods: {
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
    deleteTask(isButton) {
      if (isButton) {
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
      const url = this.isSubtask
        ? `/api/quests/${questId}/tasks/${this.parentTaskId}/subtasks/${this.task.id}/done`
        : `/api/quests/${questId}/tasks/${this.task.id}/done`;

      if (this.task.done === true) {
        this.$api
          .$delete(url)
          .then(() => {
            if (!this.isSubtask)
              this.$store.commit('quest/incrementUndoneCnt', questId);
            this.task.done = false;
          })
          .catch(() => alert('done error'));
      } else {
        this.$api
          .$put(url)
          .then(() => {
            if (!this.isSubtask)
              this.$store.commit('quest/decrementUndoneCnt', questId);
            this.task.done = true;
          })
          .catch(() => alert('done error'));
      }
    },

    toggleDoing() {
      if (this.isDoing) {
        alert('実行中のタスクがあります');
        return;
      }
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

.icon-button::before {
  cursor: pointer;
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
