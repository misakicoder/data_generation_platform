import Data_preprocess from "@/components/Playground/Data_preprocess.vue";
import router from "@/router/router";
import axios from "axios";
import { da } from "element-plus/es/locales.mjs";
import { ref } from "vue";

export interface ITask {
  task_id: string;
  task_type: string;
  task_algorithm: string;
  task_state: string;
  task_name: string;
}



export const task_list = ref<ITask[]>([]);

export const current_task = ref<ITask>({
  task_id: "",
  task_type: "",
  task_algorithm: "",
  task_state: "",
  task_name: "",
});

export const data_manage = ref({
  data_clean : false,
  data_mark : false,
  data_preprocess : false,
  data_generate : false,
});



export const algorithm_list = ref<Array<{[key: string]: any}>>([]);

export const get_algorithm_list = () => {
  axios
    .get("/api/algorithms/",{ params: { task_type: current_task.value.task_type } })
    .then((res) => {
      Object.assign(algorithm_list.value, res.data.algorithm_list);
    })
    .catch((err) => {
      console.error(err);
    });
};

export const get_data_manager = () => {
  axios
    .get("/api/data_manager/",{ params: { task_id: current_task.value.task_id } })
    .then((res) => {
      Object.assign(data_manage.value, res.data.data_manager);
    })
    .catch((err) => {
      console.error(err);
    });
}

export const update_current_task = () => {
  current_task.value.task_type = "pending";
  const update_current_task_interval = setInterval(() => {
    axios
      .get("/api/task/", { params: { task_id: current_task.value.task_id } })
      .then((res) => {
        Object.assign(current_task.value, res.data);

        if (current_task.value.task_type === "ready") {
          clearInterval(update_current_task_interval);
        }
      });
  }, 4000);
};

export const get_current_task = () => {
  if (current_task.value.task_id === "") {
    return;
  }
  axios
    .get("/api/task/", { params: { task_id: current_task.value.task_id } })
    .then(async (res) => {
      await Object.assign(current_task.value, res.data.task);
      await get_algorithm_list();
      await get_data_manager();
    })
    .catch((err) => {
      console.error(err);
      if (err.response.status === 404 || err.response.status === 401) {
        router.push("/login");
      } else if (err.response.status === 403) {
        // 无权限，回到自己的主页
        router.push("/my");
      }
    });
};

export const get_all_my_tasks = () => {
  axios
    .get("/api/tasks/")
    .then((res) => {
      task_list.value = res.data.tasks;
    })
    .catch((err) => {
      console.error(err);
    });
};
