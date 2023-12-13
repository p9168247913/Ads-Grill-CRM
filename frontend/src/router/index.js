import { createRouter, createWebHistory } from 'vue-router';
// import store from '@/store';

const routes = [
  {
    path: "/login",
    name: "loginView",
    component: () => import("@/views/auth/loginView.vue")
  },
  {
    path: "/dashboard",
    name: "dashBoard",
    component: () => import("@/views/auth/dashBoard.vue")
  },
  {
    path: "/employees/:val",
    name: "employees",
    component: () => import("@/components/getEmployees.vue"),
  },
];

const router = createRouter({
  mode: 'history',
  history: createWebHistory(),
  routes,
});

// router.beforeEach((to, from, next) => {
//   if (typeof store.state.authToken == 'undefined' || !store.state.authToken){
//     next('/login')
//   }
//   else{
//     next()
//   }
// });

export default router;