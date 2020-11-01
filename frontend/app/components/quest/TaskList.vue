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
            @keydown.enter="(e) => addNewTask(e, task.id)"
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
  data() {
    return {
      tasks: [],
    };
  },
  components: {
    SubtaskList,
  },
  methods: {
    updateTask(task) {
      console.log('TODO: タスク編集APIへ', task);
    },
    // taskIdの下に新しいtask or subtaskを追加する
    addNewTask(e, taskId) {
      if (e.keyCode !== 13) return; // 日本語入力確定を除外

      const index = this.tasks.findIndex((task) => {
        return task.id === taskId;
      });

      if (e.shiftKey) {
        // サブタスクを追加
        // TODO: サブタスク登録APIへ
        const newSubtask = {
          id: '0100',
          name: 'Untitled',
          done: false,
        };
        this.tasks[index].subtasks.push(newSubtask);
      } else {
        // タスクを追加
        // TODO: タスク登録APIへ
        const newTask = {
          id: '0100',
          name: 'Untitled',
          done: false,
          subtasks: [],
        };
        this.tasks.splice(index + 1, 0, newTask);
      }
    },
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
