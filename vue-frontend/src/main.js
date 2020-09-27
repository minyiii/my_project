// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from "vue";
import App from "./App";
import router from "./router";
import { BootstrapVue, IconsPlugin } from "bootstrap-vue";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
// Install BootstrapVue
Vue.use(BootstrapVue);
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin);

//ScrollTo
const VueScrollTo = require("vue-scrollto");
Vue.use(VueScrollTo);
Vue.config.productionTip = false;

// import 'jsmind'
import jm from "vue-jsmind";
Vue.use(jm);

// var editor = require('./editor.vue');
import mavonEditor from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'
// use
Vue.use(mavonEditor)

import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios, axios)
Vue.prototype.$axios = axios;

// 以下開始不確定是否要加
// axios.defaults.baseURL = baseURL
// http request 拦截器
// axios.interceptors.request.use(
//   config => {
//     if (localStorage.JWT_TOKEN) {  // 判断是否存在token，如果存在的话，则每个http header都加上token
//       config.headers.Authorization = `token ${localStorage.JWT_TOKEN}`
//     }
//     return config
//   },
//   err => {
//     return Promise.reject(err)
//   })

// // http response 拦截器
// axios.interceptors.response.use(
//   response => {
//     return response
//   },
//   error => {
//     if (error.response) {
//       console.log('axios:' + error.response.status)
//       switch (error.response.status) {
//         case 401:
//           // 返回 401 清除token信息并跳转到登录页面
//           store.commit('LOG_OUT')
//           router.replace({
//             path: '/login',
//             query: { redirect: router.currentRoute.fullPath }
//           })
//       }
//     }
//     return Promise.reject(error.response.data)   // 返回接口返回的错误信息
//   })
// Vue.prototype.$http = axios;
// 以上不確定是否要加


/* eslint-disable no-new */
new Vue({
  el: "#app",
  // render: h => h(editor),
  router,
  components: { App },
  template: "<App/>"
});
