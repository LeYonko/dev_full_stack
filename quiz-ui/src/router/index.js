import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import AboutUs from '../views/AboutUs.vue'
import NewQuizPage from '../views/NewQuizPage.vue'
import QuestionsManager from '../views/QuestionsManager.vue'
import ScoresPage from '../views/ScoresPage.vue'
import ConnexionPage from '../views/ConnexionPage.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'HomePage',
      component: HomePage,
    },
    {
        path: '/aboutUs',
        name: 'aboutUs',
        component: AboutUs,
    },
    {
      path: '/newQuizPage',
      name: 'newQuizPage',
      component: NewQuizPage,
    },
    {
        path: '/connexionPage',
        name: 'connexionPage',
        component: ConnexionPage,
    },
    {
      path: "/questions",
      name: "questions",
      component: QuestionsManager
    },
    {
      path: "/scoresPage",
      name: "scoresPage",
      component: ScoresPage
    }
  ]
})

export default router
