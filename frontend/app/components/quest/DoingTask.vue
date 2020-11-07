<template>
  <div class="card-body">
    <b-list-group>
      <b-button v-if="isCompleted" variant="primary" @click="toggleDoing"
        >実行済みにする</b-button
      >
      <b-button v-else variant="secondary" @click="toggleDoing"
        >未実行に移動</b-button
      >
      <b-list-group-item class="task flex-end">
        <DoingTaskListItem
          ref="doingTaskListItem"
          :is-subtask="false"
          :task="task"
          @doneTask="toggleSubtask"
        />
      </b-list-group-item>
      <DoingSubtaskList ref="doingSubtaskList" :task="task" />
    </b-list-group>
  </div>
</template>

<script>
import DoingTaskListItem from '~/components/quest/DoingTaskListItem';
import DoingSubtaskList from '~/components/quest/DoingSubtaskList';

export default {
  components: {
    DoingTaskListItem,
    DoingSubtaskList,
  },
  props: {
    task: {
      type: Object,
      required: true,
    },
  },
  computed: {
    isCompleted() {
      if (this.task.done) {
        for (const subtask of Object.values(this.task.subtasks)) {
          if (!subtask.done) {
            return false;
          }
        }
        return true;
      } else {
        return false;
      }
    },
  },

  methods: {
    toggleSubtask(done) {
      if ('doingSubtaskList' in this.$refs) {
        this.$refs.doingSubtaskList.toggleDone(done);
      }
    },
    toggleDoing() {
      this.$refs.doingTaskListItem.toggleDoing();
    },
    updateTask(task) {
      const questId = this.$route.params.quest;
      this.$api
        .$patch(`/api/quests/${questId}/tasks/${task.id}`, {
          name: task.name,
        })
        .then(() => {})
        .catch((err) => {
          console.log(err);
        });
    },

    addNewTask() {
      const questId = parseInt(this.$route.params.quest);
      this.$api
        .$post(`/api/quests/${questId}/tasks`, {
          name: 'Untitled',
          description: '',
        })
        .then((res) => {
          this.tasks.push(res);
          this.$store.commit('quest/incrementUndoneCnt', questId);
          // サーバー側で順序は保存していないので途中挿入はしないことにする
          // this.tasks.splice(index + 1, 0, res);
        })
        .catch((err) => console.log(err));
    },
    addNewSubtask(taskId) {
      const index = this.tasks.findIndex((task) => {
        return task.id === taskId;
      });
      const questId = this.$route.params.quest;
      this.$api
        .$post(`/api/quests/${questId}/tasks/${taskId}/subtasks`, {
          name: 'Untitled',
          description: '',
        })
        .then((res) => {
          this.tasks[index].subtasks.push(res);
        })
        .catch((err) => console.log(err));
    },
    deleteTask(taskId) {
      const index = this.tasks.findIndex((task) => {
        return task.id === taskId;
      });
      const questId = parseInt(this.$route.params.quest);
      this.$api
        .$delete(`/api/quests/${questId}/tasks/${taskId}`)
        .then(() => {
          this.tasks.splice(index, 1);
          this.$store.commit('quest/decrementUndoneCnt', questId);
        })
        .catch((err) => console.log(err));
    },
  },
};
</script>

<style scoped>
.task {
  border: none;
  border-top: solid 1px gray;
}
</style>
