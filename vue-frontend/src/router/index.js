import Vue from "vue";
import Router from "vue-router";
import Home from "../views/Home.vue";


Vue.use(Router);

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: "/",
      name: "Home",
      component: Home
    },
    {
      path: "/login",
      name: "Login",
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () =>
        import(/* webpackChunkName: "about" */ "../views/Login.vue")
    },
    {
      path: "/register",
      name: "Register",
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () =>
        import(/* webpackChunkName: "about" */ "../views/Register.vue")
    },
    {
      path: "/convert",
      name: "Convert",
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () =>
        import(/* webpackChunkName: "about" */ "../views/Convert.vue")
    },
    {
      path: "/settings",
      name: "Settings",
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () =>
        import(/* webpackChunkName: "about" */ "../views/Settings.vue")
    },
    {
      path: "/mindmap",
      name: "MindMap",
      component: () => import("../views/MindMap.vue"),
      // redirect: "/mindmap/mmedit",
      // children: [
      //   {
      //     path: "mmedit",
      //     name: "MMEdit",
      //     component: () => import("../views/MMEdit.vue"),
      //   }
      // ]
    },
    {
      path: "/mmedit/:index",
      name: "MMEdit",
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ "../views/MMEdit.vue"),
    },
    {
      path: '*',
      redirect: "/"
    },

  ]
});

// 以下不確定寫法
// router.beforeEach((to, from, next) => {
//   // 获取 JWT Token
//   if (to.meta.requiresAuth) {
//     // 判断该路由是否需要登录权限
//     if (localStorage.getItem('JWT_TOKEN')) {
//       // 通过获取当前的token是否存在
//       next()
//     } else {
//       next({
//         path: '/login',
//         query: { redirect: to.fullPath }
//         // 将跳转的路由path作为参数，登录成功后跳转到该路由
//       })
//     }
//   } else {
//     next()
//   }
// })

export default router