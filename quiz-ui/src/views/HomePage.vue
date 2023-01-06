<template>
    <br>
    <div class="ml-2">
      <h1>
          <span class="font-semibold text-xl">Classement général des participants</span>
      </h1>
      <br>
    </div>
    <div v-if="registeredScores.length == 0">
          <h2 class="ml-5">
              Aucun participant enregistré
          </h2>
    </div>
    <div v-else>
      <div v-for= "(scoreEntry, index) in registeredScores" v-bind:key="scoreEntry.date">
          <div v-if="index < 3"  class="flex">    
              <svg class="w-6 h-6 mr-1 ml-4" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg>
              {{ scoreEntry.playerName }} - {{ scoreEntry.score }} - {{ scoreEntry.date }}
          </div>
          <div v-else class="flex">
              <svg class="w-6 h-6 mr-1 ml-4" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" clip-rule="evenodd"></path></svg>
              {{ scoreEntry.playerName }} - {{ scoreEntry.score }} - {{ scoreEntry.date }}
          </div>
      </div>
    </div>
    <br/>
    <br/>
    <div class="ml-2">
      <h1>
          <span class="font-semibold text-xl">Quiz manga</span>
      </h1>
    </div>
    <br>
    <div class="ml-4 flex">
        <svg class="w-6 h-6 mr-1" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd"></path></svg>
        Attention : Durant ce quiz, il vous sera impossible de revenir en arrière après avoir validé une question.
    </div>
    <div class="ml-11">
        Soyez donc très attentif et amusez vous bien !
    </div>
    <br>
    <div class="ml-5 mt-3">
      <button type="button">
          <RouterLink to="/newQuizPage" class="text-sm px-5 py-5 border-2 rounded-lg text-black border-blue-600 hover:bg-opacity-40 hover:bg-blue-400 bg-sky-500/50">Démarrer le quiz !</RouterLink>
      </button>
    </div>
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
    //console.log("Composant Home page 'created'");
    try{
        var score = await quizApiService.getQuizInfo();
        //console.log(score)
        this.registeredScores = score.data['scores'];
    } catch(error){
        
    }
  }
};
</script>
