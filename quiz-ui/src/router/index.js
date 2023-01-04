import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import NewQuizPage from '../views/NewQuizPage.vue'
import QuestionsManager from '../views/QuestionsManager.vue'
//import scoresPage from '../views/scoresPage.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'HomePage',
      component: HomePage,
    },
    {
      path: '/newQuizPage',
      name: 'newQuizPage',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      //component: () => import('../views/NewQuizPage.vue')
      component: NewQuizPage,
    },
    {
      path: "/questions",
      name: "questions",
      component: QuestionsManager
    },
    /* {
      path: "/scorePage",
      name: "scorePage",
      component: scoresPage
    } */
  ]
})

export default router
