import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import AboutUs from '../views/AboutUs.vue'
import NewQuizPage from '../views/NewQuizPage.vue'
import QuestionsManager from '../views/QuestionsManager.vue'
import ScoresPage from '../views/ScoresPage.vue'
import ConnexionPage from '../views/ConnexionPage.vue'
import Admin from '../views/Admin.vue'
import AddQuestion from '../views/AddQuestion.vue'
import AdminInterface from '../views/AdminInterface.vue'
import DeleteQuestion from '../views/DeleteQuestion.vue'
import DeleteAllQuestions from '../views/DeleteAllQuestions.vue'
import DeleteAllParticipations from '../views/DeleteAllParticipations.vue'
import UpdateQuestion from '../views/UpdateQuestion.vue'

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
        path: "/admin",
        name: "admin",
        component: Admin
    },
    {
        path: "/addQuestion",
        name: "addQuestion",
        component: AddQuestion
    },
    {
      path: "/scoresPage",
      name: "scoresPage",
      component: ScoresPage
    },
    {
        path: "/adminInterface",
        name: "adminInterface",
        component: AdminInterface
    },
    {
        path: "/deleteQuestion",
        name: "deleteQuestion",
        component: DeleteQuestion
    },
    {
        path: "/deleteAllQuestions",
        name: "deleteAllQuestions",
        component: DeleteAllQuestions
    },
    {
        path: "/deleteAllParticipations",
        name: "deleteAllParticipations",
        component: DeleteAllParticipations
    },
    {
        path: "/updateQuestion",
        name: "updateQuestion",
        component: UpdateQuestion
    }
  ]
})

export default router
