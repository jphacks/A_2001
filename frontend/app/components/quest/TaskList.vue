<template>
  <div>
    <b-list-group>
      <div v-for="task in tasks" :key="task.id">
        <b-list-group-item>
          <TaskListItem
            :is-subtask="false"
            :task="task"
            @addNewTask="addNewTask"
            @addNewSubtask="addNewSubtask"
            @updateTask="updateTask"
            @deleteTask="deleteTask"
          />
        </b-list-group-item>
        <SubtaskList :task="task" />
      </div>
      <b-button @click="addNewTask" variant="primary">+</b-button>
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
  },
  methods: {
    updateTask(task) {
      const quest = this.$route.params.quest;
      this.$api.$patch(`/api/quests/${quest}/tasks/${task.id}`, {
        name: task.name,
      });
    },
    // addNewTask(taskId) {
    // const index = this.tasks.findIndex((task) => {
    //   return task.id === taskId;
    // });
    addNewTask() {
      const quest = this.$route.params.quest;
      this.$api
        .$post(`/api/quests/${quest}/tasks`, {
          name: 'Untitled',
          description: '',
        })
        .then((res) => {
          this.tasks.push(res);
          // サーバー側で順序は保存していないので途中挿入はしないことにする
          // this.tasks.splice(index + 1, 0, res);
        })
        .catch((err) => console.log(err));
    },
    addNewSubtask(taskId) {
      const index = this.tasks.findIndex((task) => {
        return task.id === taskId;
      });
      const quest = this.$route.params.quest;
      this.$api
        .$post(`/api/quests/${quest}/tasks/${taskId}/subtasks`, {
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
      const quest = this.$route.params.quest;
      this.$api
        .$delete(`/api/quests/${quest}/tasks/${taskId}`)
        .then(() => {
          this.tasks.splice(index, 1);
        })
        .catch((err) => console.log(err));
    },
  },
};
</script>
