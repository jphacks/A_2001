<template>
  <div :id="`subtask_${task.id}`">
    <b-list-group-item
      v-for="subtask in task.subtasks"
      :key="subtask.id"
      class="subtask d-flex align-items-center"
      button
    >
      <TaskListItem
        :task="subtask"
        :is-subtask="true"
        @addNewSubtask="addNewSubtask"
        @updateTask="updateSubtask"
      />
    </b-list-group-item>
  </div>
</template>

<script>
import TaskListItem from '~/components/quest/TaskListItem';

export default {
  props: ['task'],
  components: {
    TaskListItem,
  },
  methods: {
    updateSubtask(subtask) {
      console.log('TODO: サブタスク編集APIへ', subtask);
    },
    // taskに新しいsubtaskを追加
    addNewSubtask() {
      // TODO: サブタスク登録APIへ
      const newSubtask = {
        id: '0100',
        name: 'Untitled',
        done: false,
      };
      this.task.subtasks.push(newSubtask);
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
