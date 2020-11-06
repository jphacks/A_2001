<template>
  <div class="d-flex align-items-center">
    <b-form-checkbox
      v-model="task.done"
      :class="{ 'task-name': !isSubtask }"
      @change="toggleDone(task.done)"
      >{{ task.name }}</b-form-checkbox
    >
    <!-- <i
      class="fa fa-lg text-success"
      :class="task.done ? 'fa-check-circle-o' : 'fa-circle-o'"
      @click="toggleDone"
    />
    <p class="mb-0 ml-1" :class="{ 'task-name': !isSubtask }">
      {{ task.name }}
    </p> -->
    <!-- チェックボックスを元に戻すかもしれない -->
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
  },
  data() {
    return {
      focused: false,
      deleted: false,
      selected: 'stop',
      options: [{ text: 'checked', value: 'checked' }],
    };
  },

  methods: {
    // boolean
    toggleDone(done) {
      const questId = parseInt(this.$route.params.quest);
      const url = this.isSubtask
        ? `/api/quests/${questId}/tasks/${this.parentTaskId}/subtasks/${this.task.id}/done`
        : `/api/quests/${questId}/tasks/${this.task.id}/done`;
      if (done) {
        this.$api
          .$delete(url)
          .then(() => {
            if (!this.isSubtask) {
              this.$store.commit('quest/incrementUndoneCnt', questId);
            }
            this.task.done = false;
          })
          .catch(() => alert('done error'));
      } else {
        this.$api
          .$put(url)
          .then(() => {
            if (!this.isSubtask) {
              this.$store.commit('quest/decrementUndoneCnt', questId);
            }
            this.task.done = true;
          })
          .catch(() => alert('done error'));
      }
      if (!this.isSubtask) {
        this.$emit('doneTask', done);
      }
    },
    done() {
      const questId = parseInt(this.$route.params.quest);
      const url = this.isSubtask
        ? `/api/quests/${questId}/tasks/${this.parentTaskId}/subtasks/${this.task.id}/done`
        : `/api/quests/${questId}/tasks/${this.task.id}/done`;
      this.$api
        .$put(url)
        .then(() => {
          if (!this.isSubtask) {
            this.$store.commit('quest/incrementUndoneCnt', questId);
          }
          this.task.done = false;
        })
        .catch(() => alert('done error'));
    },
    toggleDoing() {
      // TODO: this.task.start情報をthis.taskに持たせるべきか考える
      this.$api
        .$put(
          `/api/quests/${this.$route.params.quest}/tasks/${this.task.id}/time`
        )
        .then(() => {
          if (this.task.start === null) {
            this.task.start = new Date().toUTCString();
          } else {
            this.task.start = null;
          }
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
};
</script>

<style scoped>
.task-name {
  font-weight: bold;
}
</style>
