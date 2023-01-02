<template>
  <h1>Home page</h1>

  <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
    {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
  </div>
  <br/>
  <br/>
  <button type="button">
    <router-link to="/NewQuizPage">Démarrer le quiz !</router-link>
  </button>

</template>

<script>
import quizApiService from "@/services/QuizApiService";

export default {
  name: "HomePage",
  data() {
    return {
      registeredScores : []
    };
  },
  async created() {
    console.log("Composant Home page 'created'");
    var score = await quizApiService.getQuizInfo();
    this.registeredScores = score.data['score'];
    
    var value = quizApiService.getQuizInfo();
  }
};
</script>
