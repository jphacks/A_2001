<template>
  <div>
    <b-list-group>
      <div v-for="task in tasks" :key="task.id">
        <b-list-group-item class="d-flex align-items-center" button>
          <i class="fa fa-circle-o fa-lg"></i>
          <input
            v-model="task.name"
            class="task-name"
            placeholder="タスクを入力"
            @blur="updateTask(task)"
          />
          <b-badge variant="primary" pill class="ml-auto">{{
            task.subtasks.length
          }}</b-badge>
        </b-list-group-item>
        <SubtaskList :task="task" />
      </div>
    </b-list-group>
  </div>
</template>

<script>
import SubtaskList from '~/components/quest/SubtaskList';

export default {
  components: {
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

<style scoped>
*:focus {
  outline: none;
}

.task-name {
  width: 100%;
  border: none;
  background: none;
  margin-left: 1em;
  font-weight: bold;
}
</style>
