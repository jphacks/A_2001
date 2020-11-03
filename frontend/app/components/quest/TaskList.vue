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
    </b-list-group>
  </div>
</template>

<script>
import TaskListItem from '~/components/quest/TaskListItem';
import SubtaskList from '~/components/quest/SubtaskList';

export default {
  props: {
    tasks: {
      type: Array,
      required: true,
    },
  },
  components: {
    TaskListItem,
    SubtaskList,
  },
  methods: {
    updateTask(task) {
      const quest = this.$route.params.quest;
      this.$api.$patch(`/api/quests/${quest}/tasks/${task.id}`, {
        name: task.name,
      });
    },
    addNewTask(taskId) {
      console.log(taskId);
      const index = this.tasks.findIndex((task) => {
        return task.id === taskId;
      });
      const newTask = {
        id: '0100',
        name: 'Untitled',
        done: false,
        subtasks: [],
      };
      this.tasks.splice(index + 1, 0, newTask);
    },
    addNewSubtask(taskId) {
      const index = this.tasks.findIndex((task) => {
        return task.id === taskId;
      });
      // TODO: サブタスク登録APIへ
      const newSubtask = {
        id: '0100',
        name: 'Untitled',
        done: false,
      };
      this.tasks[index].subtasks.push(newSubtask);
    },
    deleteTask(taskId) {
      const index = this.tasks.findIndex((task) => {
        return task.id === taskId;
      });
      this.tasks.splice(index, 1);
    },
  },
};
</script>
