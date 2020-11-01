<template>
  <div :id="`subtask_${task.id}`">
    <b-list-group-item
      v-for="subtask in task.subtasks"
      :key="subtask.id"
      class="subtask d-flex align-items-center"
      button
    >
      <i class="fa fa-circle-o fa-lg"></i>
      <input
        v-model="subtask.name"
        class="subtask-name"
        placeholder="サブタスクを入力"
        @blur="updateSubtask(subtask)"
      />
    </b-list-group-item>
  </div>
</template>

<script>
export default {
  props: ['task'],
  methods: {
    updateSubtask(subtask) {
      console.log('TODO: サブタスク編集APIへ', subtask);
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

.subtask-name {
  width: 100%;
  border: none;
  background: none;
  margin-left: 1em;
}
</style>
