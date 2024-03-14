// 引用 Mock
const Mock = require('mockjs')
// import Mock from "mockjs";

const latest = Mock.mock(RegExp("/api/community/latest" + ".*"), "get", {
  // 属性 list 的值是一个数组，随机生成 1 到 10 个元素
  movies: [
    {
      name: "和我一起，潜水去！",
      cover:
        "https://images.unsplash.com/photo-1682687982167-d7fb3ed8541d?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxlZGl0b3JpYWwtZmVlZHwxfHx8ZW58MHx8fHx8",
      id: "123",
      user_name: "李",
      publish_day: "2023.12.31",
      user_avatar:
        "https://plus.unsplash.com/premium_photo-1670006626745-ccaf6151cb2a?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHx8",
    },
    {
      name: "伟大的，公路之旅",
      cover:
        "https://images.unsplash.com/photo-1708852154434-d6436655b99d?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwxNHx8fGVufDB8fHx8fA%3D%3D",
      id: "123",
      user_name: "李",
      publish_day: "2023.12.31",
      user_avatar:
        "https://plus.unsplash.com/premium_photo-1670006626745-ccaf6151cb2a?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHx8",
    },
  ],
  status: "200",
  message: "ok",
});

const recommend = Mock.mock(RegExp("/api/community/recommend" + ".*"), "get", {
  // 属性 list 的值是一个数组，随机生成 1 到 10 个元素
  movies: [
    {
      name: "和我一起，潜水去！",
      cover:
        "https://images.unsplash.com/photo-1682687982167-d7fb3ed8541d?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxlZGl0b3JpYWwtZmVlZHwxfHx8ZW58MHx8fHx8",
      id: "123",
      user_name: "李",
      publish_day: "2023.12.31",
      user_avatar:
        "https://plus.unsplash.com/premium_photo-1670006626745-ccaf6151cb2a?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHx8",
    },
    {
      name: "伟大的，公路之旅",
      cover:
        "https://images.unsplash.com/photo-1708852154434-d6436655b99d?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwxNHx8fGVufDB8fHx8fA%3D%3D",
      id: "123",
      user_name: "李",
      publish_day: "2023.12.31",
      user_avatar:
        "https://plus.unsplash.com/premium_photo-1670006626745-ccaf6151cb2a?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHx8",
    },
  ],
  status: "200",
  message: "ok",
});

const search_result = Mock.mock(RegExp("/api/search/movies" + ".*"), "get", {
  // 属性 list 的值是一个数组，随机生成 1 到 10 个元素
  movies: [
    {
      name: "和我一起，潜水去！",
      cover:
        "https://images.unsplash.com/photo-1682687982167-d7fb3ed8541d?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxlZGl0b3JpYWwtZmVlZHwxfHx8ZW58MHx8fHx8",
      id: "123",
      user_name: "李",
      publish_day: "2023.12.31",
      user_avatar:
        "https://plus.unsplash.com/premium_photo-1670006626745-ccaf6151cb2a?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHx8",
    },
    {
      name: "伟大的，公路之旅",
      cover:
        "https://images.unsplash.com/photo-1708852154434-d6436655b99d?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwxNHx8fGVufDB8fHx8fA%3D%3D",
      id: "123",
      user_name: "李",
      publish_day: "2023.12.31",
      user_avatar:
        "https://plus.unsplash.com/premium_photo-1670006626745-ccaf6151cb2a?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHx8",
    },
  ],
  status: "200",
  message: "ok",
});


const account = Mock.mock(RegExp("/api/account"), "get", {
  // 属性 list 的值是一个数组，随机生成 1 到 10 个元素
  email: '22@abc.com',
  desc: 'abcd',
  username: 'www',
  user_avatar: 'https://images.unsplash.com/photo-1709642717827-9621f2a978a1?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHw0fHx8ZW58MHx8fHx8',
  status: "200",
  message: "ok",
});

const updateAccount = Mock.mock(RegExp("/api/account"), "post", {
  status: "200",
  message: "ok",
});

export default { latest, recommend, search_result, account, updateAccount };
