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
    try{
        var score = await quizApiService.getQuizInfo();
        console.log(score)
        this.registeredScores = score.data['scores'];
    } catch(error){
        
    }
  }
};
</script>
