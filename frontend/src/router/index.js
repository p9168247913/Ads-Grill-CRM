import { createRouter, createWebHistory } from "vue-router";
import Dashboard from "../views/Dashboard.vue";
import projectView from "../components/projectView.vue";
import investMent from "../components/investMent.vue";
import salesView from "../components/salesView";
import leadsView from "../components/leadsView";
import LeadInfo from "../components/LeadInfo.vue"
import profitView from "../components/profitView";
import requestAccess from "../components/requestAccess";
import Profile from "../views/Profile.vue";
import Signup from "../views/Signup.vue";
import Signin from "../views/Signin.vue";
import GetEmployee from "../components/GetEmployee.vue"
import IssuesPage from '../components/Issues/IssuesPage.vue'
import Backlogs from '../components/Backlogs/BackLogs.vue'
import ActiveSprint from '../components/ActiveSprint/ActiveSprint.vue'
import ClientSignin from '.././views/ClientSignin.vue'

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
    path: "/requestaccess",
    name: "Request Access",
    component: requestAccess,
  },
  {
    path: "/projects",
    name: "Projects",
    component: projectView,
  },

  {
    path: "/investment",
    name: "Investment",
    component: investMent,
  },
  {
    path: "/leads",
    name: "Leads",
    component: leadsView,
  },
  {
    path: "/leadinfo",
    name: "Lead Info",
    component: LeadInfo,
  },
  {
    path: "/sales",
    name: "Sales",
    component: salesView,
  },
  {
    path: "/profit",
    name: "Profit",
    component: profitView,
  },
  {
    path: "/issues",
    name: "Issues",
    component: IssuesPage,
  },
  {
    path: "/backlogs",
    name: "Backlogs",
    component: Backlogs,
  },
  {
    path: "/active-sprints/:key?",
    name: "Active Sprint",
    component: ActiveSprint,
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
    path: "/client-signin",
    name: "Client Signin",
    component: ClientSignin,
  },
  {
    path: "/signup",
    name: "Signup",
    component: Signup,
  },
  {
    path: "/employees/:val",
    name: 'Employees/',
    component: GetEmployee,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
  linkActiveClass: "active",
});

router.beforeEach((to, from, next) => {
  const loggedIn = localStorage.getItem('token');
  const role = localStorage.getItem('role');

  if (to.path !== '/signin' && to.path !== '/signup' && to.path !== '/client-signin') {
    if (!loggedIn || loggedIn === "") {
      if (role !== "client") {
        next('/signin');
      } else {
        next('/client-signin');
      }
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;
