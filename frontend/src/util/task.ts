import router from "@/router/router";
import axios from "axios";
import { ref } from "vue";

export interface ITask {
  task_id: string;
  task_type: string;
  task_stated: "pending" | "running" | "ready"| "error";
  task_name: string;
}

export const task_list = ref<ITask[]>([]);

export const current_task = ref<ITask>({
  task_id: "",
  task_type: "",
  task_stated: "ready",
  task_name: "",
});

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
  axios
    .get("/api/task/", { params: { task_id: current_task.value.task_id } })
    .then((res) => {
      Object.assign(current_task.value, res.data.task);
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
