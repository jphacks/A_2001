<template>
  <div>
    <b-list-group>
      <div v-for="task in tasks" :key="task.id">
        <template v-if="task.start === null && displayDoneTask == task.done">
          <b-list-group-item class="task flex-end">
            <TaskListItem
              :is-subtask="false"
              :task="task"
              :is-doing="isDoing"
              @addNewTask="addNewTask"
              @addNewSubtask="addNewSubtask"
              @updateTask="updateTask"
              @deleteTask="deleteTask"
            />
          </b-list-group-item>
          <SubtaskList :task="task" :display-done-task="displayDoneTask" />
        </template>
      </div>
      <b-button v-if="!displayDoneTask" variant="primary" @click="addNewTask"
        >タスクを追加</b-button
      >
    </b-list-group>
  </div>
</template>

<script>
import TaskListItem from '~/components/quest/TaskListItem';
import SubtaskList from '~/components/quest/SubtaskList';

export default {
  components: {
    TaskListItem,
    SubtaskList,
  },
  props: {
    tasks: {
      type: Array,
      required: true,
    },
    displayDoneTask: {
      type: Boolean,
      default: false,
    },
  },
  computed: {
    isDoing() {
      for (const task of Object.values(this.tasks)) {
        if (task.start) {
          return true;
        }
      }
      return false;
    },
  },
  methods: {
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
