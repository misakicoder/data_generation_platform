import router from "@/router/router";
import axios from "axios";
import { ref } from "vue";

export interface ITask {
  task_id: string;
  idea: string;
  movie_type: string;
  frame_num: number;
  status: "pending" | "ready" | "error";
  story: string;
  scripts: string[];
  speeches: string[];
  scenes: string[];
  videos: string[];
  music_description_zh: string;
  music: string;
  movie: string;
}

export const task_list = ref<ITask[]>([]);

export const current_task = ref<ITask>({
  task_id: "",
  idea: "",
  movie_type: "",
  frame_num: 0,
  status: "ready",
  story: "",
  scripts: [],
  speeches: [],
  scenes: [],
  videos: [],
  music_description_zh: "",
  music: "",
  movie: "",
});

export const update_current_task = () => {
  current_task.value.status = "pending";

  const update_current_task_interval = setInterval(() => {
    axios
      .get("/api/task/", { params: { task_id: current_task.value.task_id } })
      .then((res) => {
        Object.assign(current_task.value, res.data);

        if (current_task.value.status === "ready") {
          clearInterval(update_current_task_interval);
        }
      });
  }, 4000);
};

export const get_current_task = () => {
  axios
    .get("/api/task/", { params: { task_id: current_task.value.task_id } })
    .then((res) => {
      Object.assign(current_task.value, res.data);

      // 处理 story
      let story = res.data.story;
      story.replace(/\"/g, "");
      story = story.replace(/\\n/g, "\n");
      current_task.value.story = story;
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
    .get("/api/account/movies/")
    .then((res) => {
      task_list.value = res.data.tasks_list;
    })
    .catch((err) => {
      console.error(err);
    });
};
