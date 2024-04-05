<!-- 剧本 -->
<template>
        <el-upload
            ref="upload"
            class="upload-demo"
            action="/api/data/"
            method = "post"
            :data="jsonData"
            :limit="1"
            :on-exceed="handleExceed"
            :on-change="selectFile"
            :auto-upload="false"
            :on-success="success_info"
            :on-error="error_info"
        >
        <template #trigger>
            <el-button type="primary">请选择需要上传的文件</el-button>
        </template>
        <el-button class="ml-3" type="success" @click="submitUpload">
            上传到服务器
        </el-button>
        <div style="margin-top:10px;">
        <input v-model="data_description" id="input-email-label" class="py-3 px-4 block w-4/5 border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600" placeholder="请输入数据相关描述">
        </div>
        <template #tip>
        <div class="el-upload__tip text-red">
            注意：只能上传一个文件，格式为csv文件
        </div>
        </template>
  </el-upload>
</template>

<script lang="ts" setup>
import { ref,computed } from 'vue'
import { UploadFilled } from '@element-plus/icons-vue'
import { current_task, update_current_task } from '@/util/task';
import axios from 'axios';
import { onMounted } from 'vue';
import { genFileId, uploadProps } from 'element-plus'
import type { UploadInstance, UploadProps, UploadRawFile } from 'element-plus'
import { tr } from 'element-plus/es/locale';
import { error } from 'console';
import router from "@/router/router";
import { json } from 'stream/consumers';


const raw_file = ref<UploadRawFile>()
const data_description = ref('')
const upload = ref<UploadInstance>()
const handleExceed: UploadProps['onExceed'] = (files) => {
  upload.value!.clearFiles()
  const file = files[0] as UploadRawFile
  file.uid = genFileId()
  upload.value!.handleStart(file)
}


const jsonData = computed(() => {
  return {
    body: JSON.stringify({
      data_description: data_description.value,
      task_id: current_task.value.task_id,
      data_type: current_task.value.task_type
  })
  };
});




const selectFile : UploadProps['onChange'] =  (uploadFile) => {
  if(uploadFile.raw?.type !== 'text/csv') {
    alert("上传文件格式错误，请上传csv文件")
    upload.value!.clearFiles()
    upload.value!.handleStart(raw_file.value!)
    return
  }
  raw_file.value = uploadFile.raw
}

const submitUpload = () => {
  if (data_description.value === '') {
    alert('请输入数据相关描述')
    return
  }
  if (raw_file.value === undefined) {
    alert('请选择文件')
    return
  }
  upload.value!.submit()
}

const success_info: UploadProps['onSuccess'] = (response, file, fileList) => {
  console.log(response,file,fileList)
  alert("文件上传成功")
  upload.value!.clearFiles()
}

const error_info: UploadProps['onError'] = (err, file, fileList) => {
  console.log(err, file, fileList)
  alert("文件上传失败")
  upload.value!.clearFiles()
}


</script>