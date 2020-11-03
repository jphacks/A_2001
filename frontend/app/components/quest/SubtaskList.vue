<template>
  <div :id="`subtask_${task.id}`">
    <b-list-group-item
      v-for="subtask in task.subtasks"
      :key="subtask.id"
      class="subtask"
      button
    >
      <TaskListItem
        :task="subtask"
        :is-subtask="true"
        @addNewSubtask="addNewSubtask"
        @updateTask="updateSubtask"
        @deleteTask="deleteSubtask"
      />
    </b-list-group-item>
  </div>
</template>

<script>
import TaskListItem from '~/components/quest/TaskListItem';

export default {
  props: {
    task: {
      type: Object,
      required: true,
    },
  },
  components: {
    TaskListItem,
  },
  methods: {
    updateSubtask(subtask) {
      const quest = this.$route.params.quest;
      this.$api.$patch(
        `/api/quests/${quest}/tasks/${this.task.id}/subtasks/${subtask.id}`,
        {
          name: subtask.name,
        }
      );
    },
    // taskに新しいsubtaskを追加
    addNewSubtask() {
      const quest = this.$route.params.quest;
      this.$api
        .$post(`/api/quests/${quest}/tasks/${this.task.id}/subtasks`, {
          name: 'Untitled',
          description: '',
        })
        .then((res) => {
          this.task.subtasks.push(res);
        })
        .catch((err) => console.log(err));
    },
    deleteSubtask(taskId) {
      const index = this.task.subtasks.findIndex((subtask) => {
        return subtask.id === taskId;
      });
      const quest = this.$route.params.quest;
      this.$api
        .$delete(
          `/api/quests/${quest}/tasks/${this.task.id}/subtasks/${taskId}`
        )
        .then((res) => {
          this.task.subtasks.splice(index, 1);
        })
        .catch((err) => console.log(err));
    },
  },
};
</script>

<style scoped>
*:focus {
  outline: none;
}

.subtask {
  text-indent: 1em;
}
</style>
