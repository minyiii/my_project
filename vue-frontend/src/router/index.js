import Vue from "vue";
import Router from "vue-router";
import Home from "../views/Home.vue";


Vue.use(Router);

export default new Router({
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
