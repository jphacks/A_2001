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
  data() {
    return {
      tasks: [],
    };
  },
  components: {
    TaskListItem,
    SubtaskList,
  },
  methods: {
    updateTask(task) {
      console.log('TODO: タスク編集APIへ', task);
    },
    addNewTask(taskId) {
      console.log(taskId);
      const index = this.tasks.findIndex((task) => {
        return task.id === taskId;
      });

      const newTask = {
        id: '0100',
        name: 'Untitled',
        done: false,
        subtasks: [],
      };
      this.tasks.splice(index + 1, 0, newTask);
    },
    addNewSubtask(taskId) {
      const index = this.tasks.findIndex((task) => {
        return task.id === taskId;
      });

      // TODO: サブタスク登録APIへ
      const newSubtask = {
        id: '0100',
        name: 'Untitled',
        done: false,
      };
      this.tasks[index].subtasks.push(newSubtask);
    },
    deleteTask(taskId) {
      const index = this.tasks.findIndex((task) => {
        return task.id === taskId;
      });
      this.tasks.splice(index, 1);
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
