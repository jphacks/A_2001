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
  components: {
    TaskListItem,
    SubtaskList,
  },
  data() {
    return {
      tasks: [],
    };
  },
  mounted() {
    // TODO: APIからGET
    this.tasks = [
      {
        id: '0001',
        name: 'hogehoge',
        done: false,
        subtasks: [
          { id: '0010', name: 'subtask hoge', done: false },
          { id: '0011', name: '', done: false },
        ],
      },
      {
        id: '0002',
        name: 'fuga',
        done: true,
        subtasks: [
          { id: '0020', name: 'subtask hoge', done: false },
          { id: '0021', name: 'subtask002', done: false },
        ],
      },
      { id: '0003', name: 'asljfalksdfj', done: false, subtasks: [] },
      { id: '0004', name: 'hpighlrkjlkwjeafs', done: false, subtasks: [] },
    ];
  },
  methods: {
    updateTask(task) {
      console.log('TODO: タスク編集APIへ', task);
    },
  },
};
</script>
