<template>
  <div class="d-flex align-items-center">
    <i class="fa fa-lg fa-check-circle-o text-success icon-button" />
    <p class="mb-0 ml-1" :class="{ 'task-name': !isSubtask }">
      {{ task.name }}
    </p>
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
  data: () => {
    return {
      deleted: false,
      selected: 'stop',
      composing: false,
    };
  },
};
</script>

<style scoped>
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
