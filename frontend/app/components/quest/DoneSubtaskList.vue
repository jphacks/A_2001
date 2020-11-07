<template>
  <div :id="`subtask_${task.id}`" class="subtask-container">
    <div>
      <b-list-group-item
        v-for="subtask in task.subtasks"
        :key="subtask.id"
        class="subtask"
      >
        <DoneTaskListItem :task="subtask" :is-subtask="true" />
      </b-list-group-item>
    </div>
  </div>
</template>

<script>
import DoneTaskListItem from '~/components/quest/DoneTaskListItem';

export default {
  components: {
    DoneTaskListItem,
  },
  props: {
    task: {
      type: Object,
      required: true,
    },
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
        .then(() => {
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
