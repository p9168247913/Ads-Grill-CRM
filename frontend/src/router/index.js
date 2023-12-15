import { createRouter, createWebHistory } from "vue-router";
import Dashboard from "../views/Dashboard.vue";
import investMent from "../components/investMent.vue";
import salesView from "../components/salesView";
import leadsView from "../components/leadsView";
import profitView from "../components/profitView";
import Profile from "../views/Profile.vue";
import Signup from "../views/Signup.vue";
import Signin from "../views/Signin.vue";
import GetEmployee from "../components/GetEmployee.vue"

const routes = [
  {
    path: "/",
    name: "/",
    redirect: "/dashboard",
  },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: Dashboard,
  },
  {
    path: "/investment",
    name: "investment",
    component: investMent,
  },
  {
    path: "/leads",
    name: "leads",
    component: leadsView,
  },
  {
    path: "/sales",
    name: "sales",
    component: salesView,
  },
  {
    path: "/profit",
    name: "profit",
    component: profitView,
  },
  {
    path: "/profile",
    name: "Profile",
    component: Profile,
  },
  {
    path: "/signin",
    name: "Signin",
    component: Signin,
  },
  {
    path: "/signup",
    name: "Signup",
    component: Signup,
  },
  {
    path: "/employees/:val",
    name: "employees",
    component: GetEmployee,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  linkActiveClass: "active",
});

export default router;
