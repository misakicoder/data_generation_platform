<template>
    <div class="flex flex-col">
  <div class="-m-1.5 overflow-x-auto">
    <div class="p-1.5 min-w-full inline-block align-middle">
      <div class="overflow-hidden">
        <table class="min-w-full divide-y divide-gray-200 dark:divide-neutral-700">
          <thead>
            <tr>
              <th scope="col" class="px-6 py-3 text-start text-xs font-medium text-gray-500 uppercase dark:text-neutral-500">数据描述</th>
              <th scope="col" class="px-6 py-3 text-start text-xs font-medium text-gray-500 uppercase dark:text-neutral-500">数据类型</th>
              <th scope="col" class="px-6 py-3 text-end text-xs font-medium text-gray-500 uppercase dark:text-neutral-500">下载</th>
              <th scope="col" class="px-6 py-3 text-end text-xs font-medium text-gray-500 uppercase dark:text-neutral-500">删除</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-200 dark:divide-neutral-700" v-for="data in data_list">
            <tr class="hover:bg-gray-100 dark:hover:bg-neutral-700">
              <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-800 dark:text-neutral-200">{{ data.data_description }}</td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-800 dark:text-neutral-200">{{ data.data_type }}</td>
              <td class="px-6 py-4 whitespace-nowrap text-end text-sm font-medium">
                <button type="button" class="inline-flex items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent text-blue-600 hover:text-blue-800 disabled:opacity-50 disabled:pointer-events-none dark:text-blue-500 dark:hover:text-blue-400"
                @click="download_data(data.data_id,data.data_description)">下载</button>
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-end text-sm font-medium">
                <button type="button" class="inline-flex items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent text-blue-600 hover:text-red-800 disabled:opacity-50 disabled:pointer-events-none dark:text-red-500 dark:hover:text-red-400"
                @click="delete_data(data.data_id)">删除</button>
              </td>
            </tr>

          </tbody>
        </table>
      </div>
    </div>
  </div>
</div>
</template>

<script lang="ts" setup>

import axios from 'axios';
import { onMounted } from 'vue';
import { ref } from 'vue';
const data_list = ref<Array<{[key: string]: any}>>([])
onMounted(async () => {
    axios.get('/api/data/').then(res => {
        data_list.value = res.data.data
    })
})

const delete_data = (data_id: string) => {
    axios.delete('/api/data/', {data: {data_id: data_id}}).then(res => {
        if (res.data.status == 'success') {
            alert('删除成功')
        } else {
            alert('删除失败')
        }
        axios.get('/api/data/').then(res => {
            data_list.value = res.data.data
        })
    })
}

const download_data = (data_id: string,data_description :string) => {
    axios.put('/api/data/', {data_id: data_id}).then(res => {
        const url = window.URL.createObjectURL(new Blob([res.data]));
        const link = document.createElement('a');
        link.href = url;
        link.setAttribute('download', data_description+'.csv'); // or any other extension
        document.body.appendChild(link);
        link.click();
    })
}

</script>