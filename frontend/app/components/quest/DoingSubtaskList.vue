<template>
  <div :id="`subtask_${task.id}`" class="subtask-container">
    <div>
      <b-list-group-item
        v-for="subtask in task.subtasks"
        :key="subtask.id"
        class="subtask"
      >
        <DoingTaskListItem
          :ref="`DoingTaskListItem${subtask.id}`"
          :task="subtask"
          :is-subtask="true"
          :parent-task-id="task.id"
        />
      </b-list-group-item>
    </div>
  </div>
</template>

<script>
import DoingTaskListItem from '~/components/quest/DoingTaskListItem';

export default {
  components: {
    DoingTaskListItem,
  },
  props: {
    task: {
      type: Object,
      required: true,
    },
  },
  methods: {
    toggleDone(done) {
      for (const subtask of this.task.subtasks) {
        if (`DoingTaskListItem${subtask.id}` in this.$refs) {
          this.$refs[`DoingTaskListItem${subtask.id}`][0].toggleDone(done);
        }
      }
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
  border: none;
  border-top: solid 1px gray;
}

.subtask-container {
  display: flex;
  justify-content: flex-end;
  width: 100%;
}

.subtask-container > div {
  width: 95%;
}

.subtask {
  width: 100%;
}
</style>
