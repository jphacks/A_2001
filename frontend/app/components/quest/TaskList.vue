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
  data() {
    return {
      tasks: [],
    };
  },
};
</script>
